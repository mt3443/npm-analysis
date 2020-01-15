var ls = require('npm-remote-ls').ls;
var config = require('npm-remote-ls').config;
var detect_typosquatting = require('./typosquatting.min.js').detect_typosquatting;

// check args
if (process.argv[2] == undefined) {
    console.log('Usage: node dependency_check.js package_name[@version_number]');
    process.exit();
}

// ensure package name is well-formed
let at_count = process.argv[2].split('@').length - 1;
if (process.argv[2][process.argv[2].length - 1] == '@' || at_count > 2) {
    console.log('Error: invalid package name requested');
    process.exit();
}

// get requested package name and version
let requested_package = null;
let requested_version = null;

if (at_count == 1 && process.argv[2][0] == '@') {
    requested_package = process.argv[2];
    requested_version = 'latest';
} else if (at_count == 2 && process.argv[2][0] == '@') {
    let version_at_index = process.argv[2].indexOf('@', 1);
    requested_package = process.argv[2].substring(0, version_at_index);
    requested_version = process.argv[2].substring(version_at_index + 1);
} else if (at_count == 1 && process.argv[2][0] != '@') {
    let version_at_index = process.argv[2].indexOf('@');
    requested_package = process.argv[2].substring(0, version_at_index);
    requested_version = process.argv[2].substring(version_at_index + 1);
} else {
    requested_package = process.argv[2];
    requested_version = 'latest';
}

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

    return temp_set;
}

// add command line option to download dev dependencies
config({
    development: false
})

ls(requested_package, requested_version, true, (dependency_tree) => {
    // get packages from dependency tree
    let packages_to_be_installed = get_packages_to_be_installed(dependency_tree);

    // debug
    console.log('Total packages to be installed:', packages_to_be_installed.size);

    // scan all packages in set
    let n_typosquatting = 0;
    for (let package of packages_to_be_installed) {
        let typosquatting = detect_typosquatting(package);

        if (typosquatting != false) {
            console.log('Warning: "' + requested_package + '" depends on "' + package + '", which may be typosquatting "' + typosquatting + '"');
            n_typosquatting++;
        }
    }

    if (n_typosquatting == 0) {
        console.log('No typosquatting detected')
    } else {
        //console.log('Warning: ' + n_typosquatting + ' possible typosquatting packages detected in the dependency tree for "' + requested_package + '"');
        
        var stdin = process.stdin;
        stdin.setEncoding('utf-8');
        process.stdout.write('Are you sure you want to install "' + requested_package + '"? [y/n] ');

        stdin.on('data', (data) => {
            if (data.toLowerCase()[0] == 'y') {
                console.log('download package here');
            }
            process.exit();
        });
    }
});