var _ = require('lodash');
var exec = require('child_process').exec;
var async = require('async');
var fs = require('fs-extra');
var path = require('path');

module.exports = function (grunt) {

    var origHeader = grunt.log.header;

    grunt.log.header = function () {
    };

    function getVersion() {
        var v = grunt.file.readJSON('package.json').version.split('.');
        return {
            full: v.join('.'),
            major: v[0],
            minor: v[1],
            patch: v[2],
            split: v
        };
    }

    function publishVersion(type, callback) {

        var publish = grunt.config('publish');

        var oldVersion = getVersion();
        var newVersion = oldVersion.split;
        if (type === 'patch') newVersion[2]++;
        if (type === 'minor') {
            newVersion[2] = 0;
            newVersion[1]++;
        }
        if (type === 'major') {
            newVersion[2] = 0;
            newVersion[1] = 0;
            newVersion[0]++;
        }
        newVersion = newVersion.join('.');

        var tasks = {

            bowerVersion: function (done) { // FIRST
                var bwfile = path.join(process.cwd(), 'bower.json');
                var bw = fs.readJsonFileSync(bwfile);
                bw.version = newVersion;
                fs.outputJSONSync(bwfile, bw);
                done(null);
            },
            npmVersion: function (done) { // SECOND
                exec('npm version ' + type, function (error, stdout) {
                    done(error);
                });
            },
            gitPush: function (done) { // THIRD
                exec('git push -u origin v' + newVersion, function (error, stdout) {
                    grunt.log.ok('Created and pushed new version: ' + newVersion);
                    done(error);
                });
            },
            npmPublish: function (done) {
                exec('npm publish', function (error, stdout) {
                    grunt.log.ok('Published NPM package');
                    done(error);
                });
            }
        };
        var steps = [];
        steps.push(tasks.bowerVersion, tasks.npmVersion, tasks.gitPush);
        if (publish.npm === true) steps.push(tasks.npmPublish);

        async.waterfall(steps, function (err) {
            if (err) return grunt.fail.fatal(err);
            callback();
        });


    }

    grunt.registerTask('publish:patch', 'Publish a new version. Increase patch version by 1.', function () {
        publishVersion('patch', this.async());
    });
    grunt.registerTask('publish:minor', 'Publish a new version. Increase minor version by 1.', function () {
        publishVersion('minor', this.async());
    });
    grunt.registerTask('publish:major', 'Publish a new version. Increase major version by 1.', function () {
        publishVersion('major', this.async());
    });

    grunt.registerTask('publish:docs', 'Build & Publish documentation.', function () {
        //  var taskDone = this.async();
        //exec('npm version major', createTag(taskDone));
    });

    grunt.config('availabletasks', {           // task
        tasks: {
            options: {
                filter: 'exclude',
                showTasks: ['user'],
                tasks: ['default', 'showtime', 'header', 'build', 'custom', 'dist', 'lodash', 'packer'],
                groups: {
                    'Development': ['watch', 'serve', 'radicjs', 'docs:build'],
                    'Testing': ['test'],
                    'Deploying': ['publish:patch', 'publish:minor', 'publish:major', 'publish:docs']
                }
            }
        }
    });


    grunt.registerTask('showtime', function () {
        require('time-grunt')(grunt);
    });

    grunt.registerTask('default', 'Overview', function () {
        grunt.task.run(['availabletasks']);
    });
    grunt.registerTask('header', function (target) {
        grunt.log.header = target == 'enable' ? origHeader : function () {
        };
    });

    var origRun = grunt.task.run;
    grunt.task.run = function () {
        var args = _.toArray(arguments);
        if (args[0] !== 'default' && args[0][0] !== 'availabletasks' && args[0] !== 'availabletasks:tasks') {
            //grunt.log.header = origHeader;
        }
        // console.log(_.toArray(arguments));
        origRun.apply(grunt.task, args);
    };
};
