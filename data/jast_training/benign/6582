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


    grunt.registerMultiTask('radic_ghpages_publish', 'Documentation generator using jsdoc3.', function () {
        var self = this;
        var taskDone = this.async();

        var cwd = process.cwd();
        function chdirReset(){
            process.chdir(cwd);
        }

        var msg = Date(Date.now());

        var options = this.options({
            dir: 'docs',
            indexName: 'index.md',
            frontMatterPath: path.join(cwd, 'docs/.front-matter.yml'),
            readmePath: path.join(cwd, 'README.md'),
            replacer: '# radic'
        });

        var ascmd = function(cmd, cb){
            return function(next){
                exec(cmd, function(err, stdout, stderr){
                   // console.log(cmd, err, stdout, stderr);
                    if(typeof cb === 'function'){
                        cb(err, stdout, stderr);
                    }
                    next(err);
                });
            }
        };

        async.waterfall([
            function(next){
                var fm = "---\n" + fs.readFileSync(options.frontMatterPath, 'utf-8') + "\n---\n";
                var readme = fs.readFileSync(options.readmePath, 'utf-8')
                    .replace(options.replacer, fm)
                    .replace(/```(?=\w)(\w*)/g, '{% highlight $1 %}')
                    .replace(/```\n/g, '{% endhighlight %}\n');

                fs.outputFileSync(path.join(cwd, options.dir, options.indexName), readme, 'utf-8');
                process.chdir(path.join(cwd, options.dir));
                next(null);
            },
            ascmd('git add -A'),
            ascmd('git commit -m "' + msg + '"', function(err, stdout){
                //grunt.log.writeln(stdout);
            }),
            ascmd('git push -u origin gh-pages'),
            function(next){
                chdirReset();
                next();
            }
        ], function(err, result){
            if(err) throw new Error(err);

            console.log('done');
            taskDone();
        });

    });

};
