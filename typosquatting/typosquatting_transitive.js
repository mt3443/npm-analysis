var itertools = require('itertools');
var fs = require('fs');
var levenshtein = require('fast-levenshtein');
var csvjson = require('csvjson');
var ls = require('npm-remote-ls').ls;
var config = require('npm-remote-ls').config;

// node name
var node_name = process.argv[2];

// starting index DEBUG
// var starting_index = parseInt(process.argv[3]);

// get packages that the node was assigned
var machine_packages = fs.readFileSync('/users/m139t745/npm-analysis/typosquatting/transitive_package_names/' + node_name).toString().split(/\s+/);

// output file
var log = fs.openSync('/volatile/m139t745/transitive_output/' + node_name, 'a');

// package name delimiter regex
var delimiter_regex = /[\W|_]/;

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

// load list of all packages (user ../data/downloads.csv for local debugging)
const all_packages_json_array = csvjson.toObject(fs.readFileSync('/dev/shm/npm/data/downloads.csv').toString());

var all_package_names_set = new Set();
var dl_count_dict = {};

for (let obj of all_packages_json_array) {
    all_package_names_set.add(obj['package_name']);
    dl_count_dict[obj['package_name']] = obj['weekly_downloads'];
}

delete all_packages_json_array;

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

    if (all_package_names_set.has(package_chars)) {
            
        match1 = scope_regex.exec(package_name);

        if (match1 != null) {
            match2 = scope_regex.exec(package_chars);

            if (match2 != null && match1[1] == match2[1]) {
                continue;
            }
        }

        return {'package_name': package_chars, 'weekly_downloads': dl_count_dict[package_chars]};
    }

    return null;

}

// finds popular packages with edit distance of 1
// note: package_name.length must be at least 7
function edit_distance(package_name) {
    if (package_name.length >= 7) {
        for (let popular_package of all_packages_json_array) {

            if (Math.abs(popular_package.length - package_name.length) > 1) {
                continue;
            }

            // ignore the package being inspected when looking for typosquatting
            if (popular_package['package_name'] == package_name) {
                continue;
            }

            if (levenshtein.get(package_name, popular_package['package_name']) == 1) {

                match1 = scope_regex.exec(package_name);

                if (match1 != null) {
                    match2 = scope_regex.exec(popular_package['package_name']);
    
                    if (match2 != null && match1[1] == match2[1]) {
                        continue;
                    }
                }

                return popular_package;
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

        if (all_package_names_set.has(swapped_package_name)) {
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

function swapped_words(package_name) {

    if (package_name.match(delimiter_regex) == null) {
        return null;
    }

    let s1 = package_name.replace(delimiter_regex, ' ').split(' ').sort().join(' ');

    for (let popular_package of all_packages_json_array) {

        if (popular_package['package_name'].match(delimiter_regex) == null) {
            continue;
        }

        // ignore the package being inspected when looking for typosquatting
        if (popular_package['package_name'] == package_name) {
            continue;
        }

        let s2 = popular_package['package_name'].replace(delimiter_regex, ' ').split(' ').sort().join(' ');

        if (s1 == s2) {

            match1 = scope_regex.exec(package_name);

            if (match1 != null) {
                match2 = scope_regex.exec(popular_package['package_name']);

                if (match2 != null && match1[1] == match2[1]) {
                    continue;
                }
            }

            return popular_package;
        }
    }

    return null;
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

            if (all_package_names_set.has(temp_package)) {
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
    if (all_package_names_set.has(match[1])) {

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

    let repeated_characters_result = repeated_characters(package_name);
    let edit_distance_result = edit_distance(package_name);
    let swapped_characters_result = swapped_characters(package_name);
    let swapped_words_result = swapped_words(package_name);
    let common_typos_result = common_typos(package_name);
    let version_number_result = version_numbers(package_name);

    let results = []

    if (repeated_characters_result != null) {
        results.push(repeated_characters_result);
    }

    if (edit_distance_result != null) {
        results.push(edit_distance_result);
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
        return results[0];
    }
}

// ignore development dependencies
config({
    development: false
});

function get_packages_to_be_installed(dependency_tree) {
    
    let temp_set = new Set();

    for (let package of dependency_tree) {

        // remove version number
        let package_name = null;
        if (package[0] == '@') {
            let at_index = package.indexOf('@', 1);
            package_name = package.substring(0, at_index);
        } else {
            package_name = package.split('@')[0];
        }

        // add package name to set
        temp_set.add(package_name);

    }

    return Array.from(temp_set);
}

function make_call(i) {

    let package_being_analyzed = machine_packages[i];

    ls(package_being_analyzed, 'latest', true, (r) => {
        
        // get all packages to be installed
        let packages_to_be_installed = get_packages_to_be_installed(r);

        // scan packages for typosquatting, record results
        fs.writeSync(log, package_being_analyzed);
        for (let p of packages_to_be_installed) {
            let result = run_tests(p);

            if (result != null) {
                fs.writeSync(log, ',' + result['package_name'] + ',' + result['weekly_downloads']);
            }

        }
        fs.writeSync(log, '\n');

        if (i != machine_packages.length - 1) {
            make_call(i + 1);
        }

    });
}

// for all packages
// get dependencies (async)
// scan dependencies
// find most popular typosquatting targets for each dependency
    // record results


// for cdf, count packages (A) with dependencies (B) that are typosquatting a package (C) with download counts

// start analysis
make_call(0);