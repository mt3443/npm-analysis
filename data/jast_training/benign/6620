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
    grunt.registerMultiTask('git', 'Git commands.', function () {
        var self = this;
        var taskDone = this.async();
        var cwd = process.cwd();
        var ok = grunt.log.ok;
        var options = this.options({
            output: true,
            cwd: false,
            ignoreErrors: false
        });
        var commands = this.data.commands;
        var git = radic.binwraps.create('git');

        if(options.cwd !== false){
            process.chdir(options.cwd);
        }

        commands.forEach(function(command){
            var result = git.apply(git, command);
            if(result.code === 1 && options.ignoreErrors === false){
                grunt.verbose.error('Error: ' + result.stdout);
                grunt.fail.fatal('Executing the git command resulted in an error');
            }
            if(options.output === true){
                grunt.log.writeln(result.stdout);
            }
        });

        process.chdir(cwd);
        ok('Git commands executed');
        taskDone();
    });

};
