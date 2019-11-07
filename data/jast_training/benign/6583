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

var yaml = require('js-yaml');
module.exports = function (grunt) {

    // Please see the Grunt documentation for more information regarding task
    // creation: http://gruntjs.com/creating-tasks


    grunt.registerMultiTask('radic_jsdoc', 'Documentation generator using jsdoc3.', function () {
        var self = this;
        var taskDone = this.async();

        var options = this.options({
            dir: 'docs',
            readmePath: 'README.md',
            themePath: path.join(__dirname, '..', 'lib/jsdoctheme'),
            configPath: 'jsdoc.json',
            frontMatterPath: 'docs/.front-matter.yml',
            jsdocBin: './node_modules/jsdoc/jsdoc.js'
        });

        var ascmd = function(cmd){
            return function(next){
                exec(cmd, function(err, stdin, stdout){
                    console.log(err, stdin, stdout);
                    next(err);
                });
            }
        };

        var cwd = process.cwd();
        function chdirReset(){
            process.chdir(cwd);
        }

        var dir = path.join(cwd, options.dir);
        var tmpReadmePath = path.join(dir, '..', '_TMPREADME.md');
        var tmpConfPath = path.join(dir, '..', '_jsdoc.conf.json');

        async.waterfall([
            function(next){
                var frontMatter = yaml.safeLoad(fs.readFileSync(path.join(cwd, options.frontMatterPath), 'utf-8').replace(/---/g, ''));
                var jsdocConfig = fs.readJSONFileSync(options.configPath);
                jsdocConfig.templates.frontMatter = frontMatter;
                fs.outputJSONSync(tmpConfPath, jsdocConfig);
                next(null);
            },
            function(next){
                var readme = fs.readFileSync(options.readmePath, 'utf-8');
                  //  .replace(/```(?=\w)(\w*)/g, '{% highlight $1 %}')
                  //  .replace(/```\n/g, '{% endhighlight %}\n');

                fs.outputFileSync(tmpReadmePath, readme, 'utf-8');

                next(null);
            },
            ascmd(options.jsdocBin + ' -t ' + options.themePath + ' -c ' + tmpConfPath),
            function(next){
                fs.unlinkSync(tmpReadmePath);
                fs.unlinkSync(tmpConfPath);
                var indexfile = path.join(dir, "index.html");
                if(fs.existsSync(indexfile)){
                    fs.unlinkSync(indexfile);
                }
                next();
            },
            function(next){
                chdirReset();
                next();
            }
        ], function(err, result){
            if(err) throw new Error(err);
            taskDone();
            console.log('done');
        });

    });

};
