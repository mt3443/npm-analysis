/*
 * grunt-minscript-tpl
 *
 *
 * Copyright (c) 2014 Robin Radic
 * Licensed under the MIT license.
 */

'use strict';
var lib = require('../lib');
var util = require('util');
var path = require('path');
var _ = require('lodash'),
//    chalk = require('chalk'),
    gradic = require('../lib'),
    Handlebars = require('handlebars'),
    fs = require('fs-extra'),
    async = require('async'),
    exec = require('child_process').exec;

module.exports = function (grunt) {

    // Please see the Grunt documentation for more information regarding task
    // creation: http://gruntjs.com/creating-tasks


    grunt.registerMultiTask('radic_coverage', 'Coverage generation using istanbul/mocha and a custom template.', function () {
        var self = this;
        var taskDone = this.async();

        var options = this.options({
            dir: 'docs/coverage',
            exclude: [],
            useFrontMatter: true,
            frontMatterPath: path.join(__dirname, '..', 'lib/istanbul-radic-report/templates/front-matter.yml'),
            templateDir: path.join(__dirname, '..', 'lib/istanbul-radic-report/templates'),
            vendorDir: path.join(__dirname, '..', 'lib/istanbul-radic-report/vendor')
        });

        var exclude = '';
        if(options.exclude.length > 0){
            exclude = ' -x "' + options.exclude.join(' -x "') + '"';
            //'lib/cli/_celeri/**'
        }
        var dir =  path.join(process.cwd(), options.dir);

        var command = "./node_modules/.bin/istanbul cover --dir " + dir + " --report none" + exclude + " ./node_modules/.bin/_mocha -- -R spec";

        exec(command, function(err, stdout, stderr){
           // grunt.log.writeln(command);
           // grunt.log.writeflags(options);

            var istanbul = require('istanbul');
            var Report = istanbul.Report;
            Report.register(gradic.RadicReport);

            var report = Report.create('radic', {
                    dir: dir,
                    useFrontMatter: options.useFrontMatter,
                    frontMatterPath: options.frontMatterPath,
                    templateDir: options.templateDir,
                    vendorDir: options.vendorDir
                }),
                collector = new istanbul.Collector;

            collector.add(JSON.parse(fs.readFileSync(path.join(dir, 'coverage.json'), 'utf8')));

            //grunt.log.writeln(dir);
            report.on('done', function () { console.log('done'); taskDone(); });
            report.writeReport(collector);

        });

    });

};
