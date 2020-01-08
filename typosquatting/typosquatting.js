var itertools = require('itertools');
var fs = require('fs');
var fuzz = require('fuzzball');
var fuzzyset = require('fuzzyset.js');

// output file names
var positives_file_name = '/dev/shm/npm/typosquatting/typosquatting_positives.csv';
var negatives_file_name = '/dev/shm/npm/typosquatting/typosquatting_negatives.csv';

// output csv file column headers
var output_file_column_headers = 'package_name,repeated_chars,omitted_chars,swapped_chars,swapped_words,common_typos,version_number\n';

// package name delimiter regex
var delimiter_regex = /[\W|_]/gm;

// version number regex
var version_number_regex = /(.+?)(?:[\-|_|\.])?(?:\d+)(?:[\-|_|\.]\d+)*/gm;

// allowed omitted characters
var max_omitted_chars = 2;

// set up log file, return log file stream
function init_log_file(log_file_name) {
    let new_file = !fs.existsSync(log_file_name);
    let stream = fs.openSync(log_file_name, 'a');
    if (new_file) {
        fs.writeSync(stream, output_file_column_headers);
    }
    return stream;
}

// output file write streams
var positives_log = init_log_file(positives_file_name);
var negatives_log = init_log_file(negatives_file_name);

// common typos based on keyboard locality and appearance
var typos = {
    '@': ['2', 'a', '1', 'q', 'w', 'e', '3'],
    '1': ['2', 'w', 'q', 'i', 'l'],
    '2': ['1', 'q', 'w', 'e', '3'],
    '3': ['2', 'w', 'e', 'r', '4'],
    '4': ['3', 'e', 'r', 't', '5', 'a'],
    '5': ['4', 'r', 't', 'y', '6', 's'],
    '6': ['5', 't', 'y', 'u', '7'],
    '7': ['6', 'y', 'u', 'i', '8'],
    '8': ['7', 'u', 'i', 'o', '9'],
    '9': ['8', 'i', 'o', 'p', '0'],
    '0': ['9', 'o', 'p', '-', '_'],
    '-': ['_', '0', 'p', '.'],
    '_': ['-', '0', 'p', '.'],
    'q': ['1', '2', 'w', 's', 'a'],
    'w': ['1', '2', '3', 'e', 'd', 's', 'a', 'q', 'vv'],
    'e': ['2', '3', '4', 'r', 'f', 'd', 's', 'w'],
    'r': ['3', '4', '5', 't', 'g', 'f', 'd', 'e'],
    't': ['4', '5', '6', 'y', 'h', 'g', 'f', 'r'],
    'y': ['5', '6', '7', 'u', 'j', 'h', 'g', 't', 'i'],
    'u': ['6', '7', '8', 'i', 'k', 'j', 'h', 'y'],
    'i': ['1', '7', '8', '9', 'o', 'l', 'k', 'j', 'u', 'y'],
    'o': ['8', '9', '0', 'p', 'l', 'k', 'i'],
    'p': ['9', '0', '-', '_', 'l', 'o'],
    'a': ['q', 'w', 's', 'x', 'z'],
    's': ['q', 'w', 'e', 'd', 'c', 'x', 'z', 'a', '5'],
    'd': ['w', 'e', 'r', 'f', 'v', 'c', 'x', 's'],
    'f': ['e', 'r', 't', 'g', 'b', 'v', 'c', 'd'],
    'g': ['r', 't', 'y', 'h', 'n', 'b', 'v', 'f'],
    'h': ['t', 'y', 'u', 'j', 'm', 'n', 'b', 'g'],
    'j': ['y', 'u', 'i', 'k', 'm', 'n', 'h'],
    'k': ['u', 'i', 'o', 'l', 'm', 'j'],
    'l': ['i', 'o', 'p', 'k', '1'],
    'z': ['a', 's', 'x'],
    'x': ['z', 'a', 's', 'd', 'c'],
    'c': ['x', 's', 'd', 'f', 'v'],
    'v': ['c', 'd', 'f', 'g', 'b'],
    'b': ['v', 'f', 'g', 'h', 'n'],
    'n': ['b', 'g', 'h', 'j', 'm'],
    'm': ['n', 'h', 'j', 'k', 'rn'],
    '.': ['-', '_'],
    '/': ['1', 'l', 'i']
};

// get the names of popular packages, load into set for increased performance
var popular_packages = fs.readFileSync('../data/popular_packages.txt').toString().split('\r\n');
var popular_packages_set = new Set(popular_packages);

// get the names of all packages to detect new package uploads
var all_packages_set = new Set();
var all_packages_json = JSON.parse(fs.readFileSync('_all_docs.json', 'utf8'))['rows'];
for (let temp_package of all_packages_json) {
    all_packages_set.add(temp_package['id']);
}
delete all_packages_json;

// removes consecutive duplicate characters from given string
// example: 'aaabbbbcccba' -> 'abcba'
function remove_consecutive_duplicates(str) {
    let ret = ''
    Array.from(itertools.groupby(str)).forEach(char => ret += char[0]);
    return ret;
}

// check if given package name is typosquatting a popular package using repeated characters
// example: 'reeact' is typosquatting 'react'
// param: an unpopular package name
// return: array [bool, string], bool is true if possible typosquatting is detected, string contains
//         name of package being typosquatted, 'n/a' if false
function repeated_characters(package_name) {
    
    let package_chars = remove_consecutive_duplicates(package_name);

    for (index in popular_packages) {
        let popular_package_chars = remove_consecutive_duplicates(popular_packages[index]);

        if (popular_package_chars == package_chars) {
            return popular_packages[index];
        }
    }

    return 'n/a';

}

// check if given package name is typosquatting a popular package name by omitting characters
// example: 'ract' is typosquatting 'react'
// param: an unpopular package name
// return: array [bool, string], bool is true if possible typosquatting is detected, string contains
//         name of package being typosquatted, 'n/a' if false
function omitted_characters(package_name) {
    // consider setting a max number of omitted characters allowed
    // so, for instance, 're' won't be typosquatting 'react-native'
    // feeling like 2 omissions is fine

    for (let popular_package of popular_packages_set) {

        if (package_name.legnth >= popular_package.length || (popular_package.length - package_name.length) > max_omitted_chars) {
            continue
        }

        let m = popular_package.length;
        let i = 0;
        let j = 0;
        let n_omitted = 0;
        
        while (i < m) {
            if (popular_package[i] == package_name[j]) {
                i++;
                j++;
            } else {
                i++;
                n_omitted++;

                if (n_omitted == 2) {
                    break;
                }
            }
        }
        if (popular_package.substr(i, popular_package.length) == package_name.substr(j, package_name.length)) {
            return popular_package;
        }
    }
    return 'n/a';
}

function rearranged_characters(str1, str2) {
    return str1.split('').sort().join('') == str2.split('').sort().join('');
}

function swapped_characters(package_name) {
    for (let popular_package of popular_packages) {

        if (!rearranged_characters(package_name, popular_package)) {
            continue;
        }

        for (let j in package_name) {
            if (package_name[j] != popular_package[j]) {
                // swap two chars
                let chars = package_name.split('');
                let temp_char = '';
                let int = parseInt(j);
                temp_char = chars[int];
                chars[int] = chars[int + 1];
                chars[int + 1] = temp_char;

                if (chars.join('') == popular_package) {
                    return popular_package;
                }
            }
        }
    }
    return 'n/a';
}

function swapped_words(package_name) {

    if (package_name.match(delimiter_regex) == null) {
        return 'n/a';
    }

    let s1 = package_name.replace(delimiter_regex, ' ').split(' ').sort().join(' ');

    for (i in popular_packages) {
        let popular_package = popular_packages[i];
        let s2 = popular_package.replace(delimiter_regex, ' ').split(' ').sort().join(' ');

        if (s1 == s2) {
            return popular_package;
        }
    }

    return 'n/a';
}

function replace_at(string, index, replacement) {
    return string.substr(0, index) + replacement + string.substr(index + 1);
}

function common_typos(package_name) {
    for (let i = 0; i < package_name.length; i++) {
        if (!Object.keys(typos).includes(package_name[i])) {
            continue;
        }
        for (let replaced_char of typos[package_name[i]]) {
            if (popular_packages_set.has(replace_at(package_name, i, replaced_char))) {
                return replace_at(package_name, i, replaced_char);
            }
        }
    }
    return 'n/a';
}

function version_numbers(package_name) {
    let match = version_number_regex.exec(package_name);
    
    if (match == null) {
        return 'n/a';
    }

    if (popular_packages_set.has(match[1])) {
        return match[1];
    } else {
        return 'n/a';
    }
}

// runs typosquatting tests on a given package name, logs results
function run_tests(package_name) {

    let repeated_characters_result = repeated_characters(package_name);
    let omitted_characters_result = omitted_characters(package_name);
    let swapped_characters_result = swapped_characters(package_name);
    let swapped_words_result = swapped_words(package_name);
    let common_typos_result = common_typos(package_name);
    let version_number_result = version_numbers(package_name);

    // TODO: run general edit distance, fuzzywuzzy, fuzzyset
    //       flag new packages with highly suspicious results
    //       check for install scripts

    let result_row = repeated_characters_result + ',' +
                     omitted_characters_result + ',' +
                     swapped_characters_result + ',' +
                     swapped_words_result + ',' +
                     common_typos_result + ',' +
                     version_number_result;

    let all_tests_negative = repeated_characters_result == 'n/a' &&
                             omitted_characters_result == 'n/a' &&
                             swapped_characters_result == 'n/a' &&
                             swapped_words_result == 'n/a' &&
                             common_typos_result == 'n/a' &&
                             version_number_result == 'n/a';

    // ignore packages that set off 0 tests
    if (all_tests_negative) {
        fs.writeSync(negatives_log, package_name + ',' + result_row + '\n');
    } else {
        fs.writeSync(positives_log, package_name + ',' + result_row + '\n');
    }
}

// high level typosquatting detection function, runs all checks
function detect_typosquatting(package_name) {

    // ignore updates to popular packages
    if (popular_packages_set.has(package_name)) {
        return;
    }

    // if the couchDB change is an update to an existing package, ignore it
    if (all_packages_set.has(package_name)) {
        return

    // brand new package upload
    } else {
        // check for typosquatting
        run_tests(package_name);

        // add to all_packages_set
        all_packages_set.add(package_name);
    }
}

function scan_all(machine_name) {

    // get the packages assigned to the node
    let machine_packages = fs.readFileSync('/users/m139t745/npm-analysis/typosquatting/package_names/' + machine_name).toString().split('\r\n');

    for (let package_name of machine_packages) {
        // if the package is not popular
        if (!popular_packages_set.has(package_name)) {
            // scan it
            run_tests(package_name);
        }
    }
}

module.exports = {detect_typosquatting: detect_typosquatting, scan_all: scan_all}
