var ls = require('npm-remote-ls').ls;
var config = require('npm-remote-ls').config;
var fs = require('fs');

let positives_log = fs.createWriteStream('/dev/shm/npm/transitive/positive')
let negatives_log = fs.createWriteStream('/dev/shm/npm/transitive/negative')

let machine_packages = fs.readFileSync('/users/m139t745/npm-analysis/typosquatting/transitive_package_names/' + process.argv[2]).toString().split(/\s+/);

let typosquatting_candidates = new Set(fs.readFileSync('/dev/shm/npm/data/typosquatting_candidates.txt').toString().split(/\s+/));

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

for (let package_name of machine_packages) {
    if (package_name != '') {
        ls(package_name, 'latest', true, (dependency_tree) => {
            // get packages from dependency tree
            let packages_to_be_installed = get_packages_to_be_installed(dependency_tree);
            let typosquatting = false;
            for (let dependency of packages_to_be_installed) {
                if (typosquatting_candidates.has(dependency)) {
                    fs.writeSync(positives_log, package_name + '\n');
                    typosquatting = true;
                    break;
                }
            }

            if (!typosquatting) {
                fs.writeSync(negatives_log, package_name + '\n');
            }

        });
    }
}