var itertools = require('itertools');
var fs = require('fs');
var levenshtein = require('fast-levenshtein');

// output file names
var positives_file_name = process.argv[2] == undefined ? 'typosquatting_positives.csv' : '/dev/shm/npm/typosquatting/typosquatting_positives.csv';
var negatives_file_name = process.argv[2] == undefined ? 'typosquatting_negatives.csv' : '/dev/shm/npm/typosquatting/typosquatting_negatives.csv';

// output csv file column headers
var output_file_column_headers = 'package_name,repeated_chars,edit_distance,swapped_chars,swapped_words,common_typos,version_number\n';

// package name delimiter regex
var delimiter_regex = /[\W|_]/;

// version number regex
var version_number_regex = /^(.*?)[\.|\-|_]?\d+$/;

// packages with scope regex (@types/node)
var scope_regex = /^@(.*?)\/.+$/;

// set up log file, return log file stream
function init_log_file(log_file_name) {
    return fs.openSync(log_file_name, 'a');
}

// output file write streams
var positives_log = init_log_file(positives_file_name);
var negatives_log = init_log_file(negatives_file_name);

// common typos based on keyboard locality and appearance
var typos = {
    '@': ['', '2', 'a', '1', 'q', 'w', 'e', '3'],
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
    '-': ['_', '0', 'p', '.', ''],
    '_': ['-', '0', 'p', '.', ''],
    'q': ['1', '2', 'w', 's', 'a'],
    'w': ['1', '2', '3', 'e', 'd', 's', 'a', 'q', 'vv'],
    'e': ['2', '3', '4', 'r', 'f', 'd', 's', 'w'],
    'r': ['3', '4', '5', 't', 'g', 'f', 'd', 'e'],
    't': ['4', '5', '6', 'y', 'h', 'g', 'f', 'r'],
    'y': ['5', '6', '7', 'u', 'j', 'h', 'g', 't', 'i'],
    'u': ['6', '7', '8', 'i', 'k', 'j', 'h', 'y', 'v'],
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
    'v': ['c', 'd', 'f', 'g', 'b', 'u'],
    'b': ['v', 'f', 'g', 'h', 'n'],
    'n': ['b', 'g', 'h', 'j', 'm'],
    'm': ['n', 'h', 'j', 'k', 'rn'],
    '.': ['-', '_', ''],
    '/': ['1', 'l', 'i']
};

// get the names of popular packages, load into set for increased performance
var popular_packages = fs.readFileSync('../data/popular_packages.txt').toString().split('\r\n');
var popular_packages_set = new Set(popular_packages);

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
            
            match1 = scope_regex.exec(package_name);

            if (match1 != null) {
                match2 = scope_regex.exec(popular_packages[index]);

                if (match2 != null && match1[1] == match2[1]) {
                    continue;
                }
            }

            return popular_packages[index];
        }
    }

    return '';

}

// finds popular packages with edit distance of 1
// note: package_name.length must be at least 5
function edit_distance(package_name) {
    if (package_name.length >= 5) {
        for (let popular_package of popular_packages) {
            if (levenshtein.get(package_name, popular_package) == 1) {

                match1 = scope_regex.exec(package_name);

                if (match1 != null) {
                    match2 = scope_regex.exec(popular_package);
    
                    if (match2 != null && match1[1] == match2[1]) {
                        continue;
                    }
                }

                return popular_package;
            }
        }
    }

    return '';
}

function rearranged_characters(str1, str2) {
    return str1.split('').sort().join('') == str2.split('').sort().join('');
}

function swapped_characters(package_name) {
    for (let popular_package of popular_packages) {

        if (package_name.length != popular_package.length) {
            continue;
        }

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

                    match1 = scope_regex.exec(package_name);

                    if (match1 != null) {
                        match2 = scope_regex.exec(popular_package);

                        if (match2 != null && match1[1] == match2[1]) {
                            continue;
                        }
                    }

                    return popular_package;
                }
            }
        }
    }
    return '';
}

function swapped_words(package_name) {

    if (package_name.match(delimiter_regex) == null) {
        return '';
    }

    let s1 = package_name.replace(delimiter_regex, ' ').split(' ').sort().join(' ');

    for (i in popular_packages) {
        let popular_package = popular_packages[i];
        let s2 = popular_package.replace(delimiter_regex, ' ').split(' ').sort().join(' ');

        if (s1 == s2) {

            match1 = scope_regex.exec(package_name);

            if (match1 != null) {
                match2 = scope_regex.exec(popular_package);

                if (match2 != null && match1[1] == match2[1]) {
                    continue;
                }
            }

            return popular_package;
        }
    }

    return '';
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
            let temp_package = replace_at(package_name, i, replaced_char); // popular package name
            if (popular_packages_set.has(temp_package)) {

                match1 = scope_regex.exec(package_name);

                if (match1 != null) {
                    match2 = scope_regex.exec(temp_package);

                    if (match2 != null && match1[1] == match2[1]) {
                        continue;
                    }
                }

                return temp_package;
            }
        }
    }
    return '';
}

function version_numbers(package_name) {
    let match = version_number_regex.exec(package_name);
    
    if (match == null) {
        return '';
    }

    if (popular_packages_set.has(match[1])) {

        match1 = scope_regex.exec(package_name);

        if (match1 != null) {
            match2 = scope_regex.exec(match[1]);

            if (match2 != null && match1[1] == match2[1]) {
                return '';
            }
        }

        return match[1];
    } else {
        return '';
    }
}

// runs typosquatting tests on a given package name, logs results
function run_tests(package_name) {

    if (popular_packages_set.has(package_name)) {
        fs.writeSync(negatives_log, package_name + '\n');
        return;
    }

    let repeated_characters_result = repeated_characters(package_name);
    let edit_distance_result = edit_distance(package_name);
    let swapped_characters_result = swapped_characters(package_name);
    let swapped_words_result = swapped_words(package_name);
    let common_typos_result = common_typos(package_name);
    let version_number_result = version_numbers(package_name);

    let results = [];
    let positive = false;

    if (repeated_characters_result != '') {
        positive = true;
        results.push(repeated_characters_result);
    } else {
        results.push('n/a');
    }

    if (edit_distance_result != '') {
        positive = true;
        results.push(edit_distance_result);
    } else {
        results.push('n/a');
    }

    if (swapped_characters_result != '') {
        positive = true;
        results.push(swapped_characters_result);
    } else {
        results.push('n/a');
    }

    if (swapped_words_result != '') {
        positive = true;
        results.push(swapped_words_result);
    } else {
        results.push('n/a');
    }

    if (common_typos_result != '') {
        positive = true;
        results.push(common_typos_result);
    } else {
        results.push('n/a');
    }

    if (version_number_result != '') {
        positive = true;
        results.push(version_number_result);
    } else {
        results.push('n/a');
    }

    // ignore packages that set off 0 tests
    if (positive) {
        fs.writeSync(positives_log, package_name + ',' + results.join(',') + '\n');
    } else {
        fs.writeSync(negatives_log, package_name + '\n');
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
    let machine_packages = fs.readFileSync('/users/m139t745/npm-analysis/typosquatting/package_names/' + machine_name).toString().split(/\s+/);

    for (let package_name of machine_packages) {
        // if the package is not popular
        if (package_name != '') {
            // scan it
            run_tests(package_name);
        }
    }
}

module.exports = {detect_typosquatting: detect_typosquatting, scan_all: scan_all}