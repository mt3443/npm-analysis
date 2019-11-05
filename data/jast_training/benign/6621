
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



    grunt.registerMultiTask('radic_jsdoc', 'Documentation generator for github pages projects using jsdoc3.', function () {
        // http://gruntjs.com/creating-tasks

        var self = this;
        var taskDone = this.async();
        var cwd = process.cwd();
        var ok = grunt.log.ok;

        var options = this.options({
            docsPath: path.resolve(cwd, 'docs'),
            readmePath: path.resolve(cwd, 'docs'),
            jsdocThemePath: path.resolve(__dirname, '../lib/jsdoctheme'),
            frontMatterPath: path.resolve(cwd, 'docs/front-matter.yml'),
            jsdocConfig: path.resolve(cwd, 'jsdoc.json'),
            jsdocBinPath: path.resolve(__dirname, '../node_modules/.bin/jsdoc')
        });

        // Load files
        var frontMatter = lib.getFrontMatterYaml(options.frontMatterPath);
        var jsdocConfig = fs.readJSONSync(options.jsdocConfig);
        var tmpConfigFile = temp.openSync('radic_jsdoc_config');

        // Write temporary config
        jsdocConfig.templates.frontMatter = frontMatter;
        fs.writeJSONSync(tmpConfigFile.path, jsdocConfig);
        ok('Created temporary jsdoc.json config file');

        // Generate jsdoc
        radic.sh.execSync(options.jsdocBinPath + ' -t ' + options.jsdocThemePath + ' -c ' + tmpConfigFile.path);
        ok('Generated jsdoc');

        // Cleanup temporary files
        temp.cleanupSync();
        ok('Cleaned up temporary files');

        // Done
        taskDone();
    });

};
