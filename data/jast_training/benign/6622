
'use strict';

var lib = require('../lib'),
    path = require('path'),
    fs = require('fs-utils'),
    radic = require('radic'),
    _ = require('lodash'),
    util = radic.util,
    temp = require('temp'),
    yaml = require('js-yaml');

module.exports = function (grunt) {


    grunt.registerMultiTask('radic_jsdoc_mdpages', 'Documentation generator for github pages projects using jsdoc3.', function () {
        // http://gruntjs.com/creating-tasks

        var self = this;
        var taskDone = this.async();
        var cwd = process.cwd();
        var ok = grunt.log.ok;

        var options = this.options({
            processedFrontMatterPath: path.resolve(cwd, 'docs/processed-front-matter.yml')
        });


        this.files.forEach(function (file) {
            var frontMatter = fs.readFileSync(options.processedFrontMatterPath, 'utf-8');
            file.src.forEach(function(filePath){
                var mdFileContent = fs.readFileSync(filePath, 'utf-8');
                mdFileContent = lib.replaceHighlightToGithubPages(mdFileContent);
                fs.writeFileSync(file.dest, "---\n" + frontMatter + "\n---\n" + mdFileContent);
                ok('File processed: ' + path.basename(file.dest));
            });

        });

        // Done
        taskDone();
    });

};
