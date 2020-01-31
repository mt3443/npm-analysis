var itertools = require('itertools');
var fs = require('fs');
var csvjson = require('csvjson');

// output file
// FOLLOWER OUTPUT FORMAT (TYPOSQUATTING PACKAGE, POPULAR PACKAGE)
var log = fs.openSync('follower_output', 'a');

// package name delimiter regex
var delimiter_regex = /[\-|\.|_]/g;
var delimiters = ['', '.', '-', '_'];

// version number regex
var version_number_regex = /^(.*?)[\.|\-|_]?\d+$/;

// packages with scope regex (@types/node)
var scope_regex = /^@(.*?)\/.+$/;

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

const popular_packages = csvjson.toObject(fs.readFileSync('../data/downloads.csv').toString());
var popular_package_names_set = new Set();
var dl_count_dict = {};

for (let p of popular_packages) {
    
    if (p['weekly_downloads'] >= 1000) {
        popular_package_names_set.add(p['package_name']);
    }

    dl_count_dict[p['package_name']] = p['weekly_downloads'];
}

// removes consecutive duplicate characters from given string
// example: 'aaabbbbcccba' -> 'abcba'
function remove_consecutive_duplicates(str) {
    let ret = ''
    Array.from(itertools.groupby(str)).forEach(char => ret += char[0]);
    return ret;
}

// check if given package name is typosquatting a popular package using repeated characters
// example: 'reeact' is typosquatting 'react'
// return: [package_name, weekly_downloads]
function repeated_characters(package_name) {
    
    let package_chars = remove_consecutive_duplicates(package_name);

    if (package_chars == package_name) {
        return null;
    }

    if (popular_package_names_set.has(package_chars)) {
            
        match1 = scope_regex.exec(package_name);

        if (match1 != null) {
            match2 = scope_regex.exec(package_chars);

            if (match2 != null && match1[1] == match2[1]) {
                return null;
            }
        }

        return {'package_name': package_chars, 'weekly_downloads': dl_count_dict[package_chars] || 0};
    }

    return null;

}

// finds popular packages that have removed one character from given package_name
// note: package_name.length must be at least 6
function omitted_chars(package_name) {
    if (package_name.length >= 6) {
        for (let i = 0; i < package_name.length; i++) {
            let new_string = package_name.slice(0, i) + package_name.slice(i + 1);

            if (popular_package_names_set.has(new_string)) {
                match1 = scope_regex.exec(package_name);

                if (match1 != null) {
                    match2 = scope_regex.exec(new_string);

                    if (match2 != null && match1[1] == match2[1]) {
                        continue;
                    }
                }

                return {'package_name': new_string, 'weekly_downloads': dl_count_dict[new_string]};
            }
        }
    }

    return null;
}

function swapped_characters(package_name) {
    for (let i = 0; i < package_name.length - 1; i++) {
        // swap chars at i and i + 1
        // check if the new string is in all_package_names_set

        let chars = package_name.split('');
        let temp_char = '';
        let int = parseInt(i);
        temp_char = chars[int];
        chars[int] = chars[int + 1];
        chars[int + 1] = temp_char;

        let swapped_package_name = chars.join('');

        if (popular_package_names_set.has(swapped_package_name)) {
            match1 = scope_regex.exec(package_name);

            if (match1 != null) {
                match2 = scope_regex.exec(swapped_package_name);

                if (match2 != null && match1[1] == match2[1]) {
                    continue;
                }
            }

            return {'package_name': swapped_package_name, 'weekly_downloads': dl_count_dict[swapped_package_name]};
        }
    }

    return null;
}

function permutations(array) {
    function p(array, temp) {
        var i, x;
        if (!array.length) {
            result.push(temp);
        }
        for (i = 0; i < array.length; i++) {
            x = array.splice(i, 1)[0];
            p(array, temp.concat(x));
            array.splice(i, 0, x);
        }
    }

    var result = [];
    p(array, []);
    return result;
}

function swapped_words(package_name) {

    if (package_name.match(delimiter_regex) == null) {
        return null;
    }

    let ret_package_name = '';
    let ret_dl_count = 0;
    let tokens = package_name.replace(delimiter_regex, ' ').split(' ');

    for (let permutation of permutations(tokens)) {
        for (let delimiter of delimiters) {
            let new_string = permutation.join(delimiter);

            if (new_string == package_name) {
                continue;
            }

            if (popular_package_names_set.has(new_string)) {
                
                match1 = scope_regex.exec(package_name);

                if (match1 != null) {
                    match2 = scope_regex.exec(new_string);
    
                    if (match2 != null && match1[1] == match2[1]) {
                        continue;
                    }
                }

                let new_dl_count = dl_count_dict[new_string] || 0;

                if (ret_package_name == '' || parseInt(new_dl_count) > parseInt(ret_dl_count)) {
                    ret_package_name = new_string;
                    ret_dl_count = new_dl_count;
                }
            }
        }
    }

    return {'package_name': ret_package_name, 'weekly_downloads': dl_count_dict[ret_package_name]};

}

function replace_at(string, index, replacement) {
    return string.substr(0, index) + replacement + string.substr(index + 1);
}

function common_typos(package_name) {
    // loop through every character in the package name
    for (let i = 0; i < package_name.length; i++) {
        // if the package name contains an unusual character (unlikely but possible)
        if (!Object.keys(typos).includes(package_name[i])) {
            // ignore it
            continue;
        }

        // loop through every possible typo for that character
        for (let replaced_char of typos[package_name[i]]) {

            // make the typo
            let temp_package = replace_at(package_name, i, replaced_char); // popular package name

            if (popular_package_names_set.has(temp_package)) {
                match1 = scope_regex.exec(package_name);

                if (match1 != null) {
                    match2 = scope_regex.exec(temp_package);

                    if (match2 != null && match1[1] == match2[1]) {
                        continue;
                    }
                }

                return {'package_name': temp_package, 'weekly_downloads': dl_count_dict[temp_package]};
            }
        }
    }
    return null;
}


function version_numbers(package_name) {
    // check if the package fits the version number typosquatting format
    let match = version_number_regex.exec(package_name);
    
    // if it doesn't, return
    if (match == null) {
        return null;
    }

    // look for the a package with the same name but without the version number
    if (popular_package_names_set.has(match[1])) {

        // make sure its not in the same scope
        match1 = scope_regex.exec(package_name);

        if (match1 != null) {
            match2 = scope_regex.exec(match[1]);

            if (match2 != null && match1[1] == match2[1]) {
                return null;
            }
        }

        return {'package_name': match[1], 'weekly_downloads': dl_count_dict[match[1]]};
    } else {
        return null;
    }
}

// runs typosquatting tests on a given package name, logs results
function run_tests(package_name) {

    // ignore popular packages
    if (popular_package_names_set.has(package_name)) {
        return null;
    }

    let repeated_characters_result = repeated_characters(package_name);
    let omitted_chars_result = omitted_chars(package_name);
    let swapped_characters_result = swapped_characters(package_name);
    let swapped_words_result = swapped_words(package_name);
    let common_typos_result = common_typos(package_name);
    let version_number_result = version_numbers(package_name);

    let results = []

    if (repeated_characters_result != null) {
        results.push(repeated_characters_result);
    }

    if (omitted_chars_result != null) {
        results.push(omitted_chars_result);
    }

    if (swapped_characters_result != null) {
        results.push(swapped_characters_result);
    }

    if (swapped_words_result != null) {
        results.push(swapped_words_result);
    }

    if (common_typos_result != null) {
        results.push(common_typos_result);
    }

    if (version_number_result != null) {
        results.push(version_number_result);
    }

    // ignore packages that set off 0 tests
    if (results.length == 0) {
        return null;
    } else {
        results.sort((a, b) => {return b['weekly_downloads'] - a['weekly_downloads']});

        if (results[0]['weekly_downloads'] >= 1000) {
            return results[0]['package_name'];
        }

        return null;
    }
}

function scan(package_name) {

    let results = run_tests(package_name);

    if (results != null) {
        fs.writeSync(log, package_name + ',' + results + '\n');
    }

}

module.exports = {scan: scan};