var crosscheck = require('./typosquatting.min.js').crosscheck;
var fs = require('fs');

var package_names = fs.readFileSync('known_typosquatting').toString().split('\r\n');

crosscheck(package_names);