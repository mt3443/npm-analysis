/*global module:false*/

var _ = require('lodash');

module.exports = function (grunt) {

    //require('./tasks/testbuilder')(grunt);

    var configFilePath = grunt.option('configfile') || '_config.yml';
    require('load-grunt-tasks')(grunt);

    var pkg = grunt.file.readJSON('package.json');

    var config = grunt.file.readYAML(configFilePath);

    var defaults = config.builds[config.default];

    // Project configuration.
    grunt.initConfig({
        publish: {
            npm: true,
            bower: true
        },
        config: config,
        radicjs: {
            filename: defaults.filename
        },
        // The actual grunt server settings
        // The actual grunt server settings
        connect: {
            options: {
                port: 9009,
                // Change this to '0.0.0.0' to access the server from outside.
                hostname: 'localhost',
                livereload: 35729
            },
            livereload: {
                options: {
                    open: true,
                    base: 'test'
                },
                dist: {
                    options: {
                        open: true,
                        base: 'test'
                    }
                }
            }
        },
        wiredep: {
            task: {
                src: [
                    'test/index.html'
                ]
            }
        },
        build: {
            all: {
                src: 'src/',

                dest: "<%= config.dest %>/<%= radicjs.filename %>.js",
                minimum: [
                    "core",
                    "base"
                ],
                // Exclude specified modules if the module matching the key is removed
                removeWith: {
                    a: ["v/a", "b"]
                }
            }
        },
        copy: {
            test: {
                src: '<%= config.dest %>/radic.js',
                dest: 'test/radic.js'
            },
            packer: {
                src: 'src/tpl/_pack.js',
                dest: '<%= config.dest %>/_pack.js'
            }
        },
        clean: {
            tmp: ['.tmp'],
            dist: ['dist'],
            lodash: ['src/tpl/_lodash.js', 'src/tpl/_lodash.min.js'],
            packer: ['src/tpl/_pack.js', '<%= config.dest %>/_pack.js']
        },
        preprocess: {
            options: {
                context: {
                    DEBUG: true,
                    srcDir: require('path').join(__dirname, 'src')
                }
            },
            html: {
                src: 'test/pages/index.html',
                dest: '<%= config.dest %>/index.html'
            },
            lodash: {
                src: 'src/tpl/lodash.js',
                dest: 'src/core/getlodash.js'
            },
            packer: {
                options: {
                    context: '<%= radicjs.packer %>'
                },
                src: '<%= config.dest %>/_pack.js',
                dest: '<%= config.dest %>/packed/<%= radicjs.filename %>.packed.js'
            }
        },
        'string-replace': {
            lodash: {
                files: {
                    'src/core/getlodash.js': 'src/core/getlodash.js'
                },
                options: {
                    replacements: [
                        // place files inline example
                        {
                            pattern: /;\(function\(\)(?:\s+|)\{/,
                            replacement: ''
                        },
                        {
                            pattern: /}\.call\(this\)\);/,
                            replacement: ''
                        }
                    ]
                }
            },
            packer: {
                files: {
                    'src/tpl/_pack.js': 'src/tpl/pack.js'
                },
                options: {
                    replacements: [
                        // place files inline example
                        {
                            pattern: /_FILENAME_/,
                            replacement: '<%= radicjs.filename %>.js'
                        }
                    ]
                }

            }
        },
        uglify: {
            options: {
                report: 'gzip'
            },
            dist: {
                files: {
                    '<%= config.dest %>/radic.min.js': ['<%= config.dest %>/radic.js']
                }
            },
            radicjs: {
                files: {
                    '<%= config.dest %>/<%= radicjs.filename %>.min.js': ['<%= config.dest %>/<%= radicjs.filename %>.js']
                }
            },
            packer: {
                files: {
                    '<%= config.dest %>/packed/<%= radicjs.filename %>.packed.min.js': ['<%= config.dest %>/packed/<%= radicjs.filename %>.packed.js']
                }
            }
        },
        shell: {
            lodash: {
                options: {
                    stdout: false,
                    callback: function(err, stdout, stderr, cb) {
                        grunt.log.ok('Created custom lodash functions.');
                        cb();
                    }
                },
                command: 'lodash underscore include=<%= radicjs.lodash %> exports=none -o src/tpl/_lodash.js'
            },
            test: {
                command: 'nodeunit test/*.js'
            },
            radicjs: {
                command: '<%= radicjs.buildCommand %>' //
            }
        },
        watch: {
            options: {
                liverreload: true
            },
            js: {
                files: ['src/**'],
                tasks: ['build', 'copy:test', 'uglify'],
                options: {
                    liverreload: true
                }
            },

            livereload: {
                options: {
                    livereload: '<%= connect.options.livereload %>'
                },
                files: [
                    'src/**/*'
                ]
            }
        }
    });

    grunt.loadTasks("tasks");


    grunt.registerTask('test', 'Run tests', function (target) {

    });
    grunt.registerTask('docs:build', 'Build documentation', function (target) {

    });
    grunt.registerTask('docs:publish', 'Commit and push all documentation to gh-pages', function (target) {

    });
    grunt.registerTask('publish', 'Commit and push all to master, push all tags, publish npm and bower.', function (target) {

    });

    grunt.registerTask('dist', [ 'build', 'uglify', 'copy:test' ]);

    grunt.registerTask('serve', 'Create a test server hosting the code with LiveReload enabled', function (target) {
        if (target === 'dist') {
            return grunt.task.run(['build', 'connect:dist:keepalive']);
        }
        grunt.task.run([
            'dist',
            'connect:livereload',
            'watch'
        ]);
    });

    //require('./tasks')
};
