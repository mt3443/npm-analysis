'use strict';

var _ = require('lodash');
var fs = require('fs-extra');
var util = require('util');
var hooker = require('hooker');

module.exports = function (grunt) {

    var config = {
        widgets: ['profile', 'events'],
        radicjs: grunt.file.readYAML('radicjs.yml')
    };
    var gc = {
        config: config,
        radic_jsdoc: {
            docs: {

            }
        },
        radic_coverage: {
            docs: {
                options: {
                    frontMatterPath: 'docs/processed-front-matter.yml'
                }
            }
        },
        radic_ghpages_publish: {
            docs: {
                options: {
                    dir: 'docs',
                    indexName: 'index.md',
                    frontMatterPath: 'docs/processed-front-matter.yml',
                    readmePath: 'README.md',
                    replacer: '# github-jquery-widgets'
                }
            }
        },
        build_widget: {
            options: {
                rootDir: 'src',
                dest: 'dist'
            },
            'github-profile': {
                minify: true
            },
            'github-events': {
                minify: true
            }
        },
        subgrunt: {
            radicjs: {
                'lib/radicjs': ['radicjs:githubwidgets', '--configfile=' + process.cwd() + '/radicjs.yml', '--stack']
            }
        },
        sass: {
            options: {
                sourcemap: 'none'
            },
            bootstrap: {
                src: 'src/bootstrap.scss',
                dest: 'test/bootstrap.css'
            },
            ghwidgets: {
                src: 'src/github-widgets.scss',
                dest: 'dist/github-widgets.css'
            }
        },
        'string-replace': {
            demo: {
                files: {
                    'docs/demo/': ['docs/demo/*.html']
                },
                options: {
                    replacements: [{
                        pattern: /<!DOCTYPE html>/,
                        replacement: "---\n---\n<!DOCTYPE html>"
                    }]
                }
            }
        },
        preprocess: {
            options: {
                context: {
                    DEBUG: true
                }
            },
            previewhtml: {
                options: {
                    inline: true
                },

                src: ['preview/*.html']
            }
        },
        copy: {
            demo: {
                files: [{
                    expand: true,
                    cwd: 'preview',
                    src: '**',
                    dest: 'docs/demo/'
                },{
                    expand: true,
                    cwd: 'dist',
                    src: '**',
                    dest: 'docs/dist/'
                }]
            },
            basewidget2dist: {
                files: [{
                    expand: true,
                    cwd: 'src',
                    src: 'github-widget.js',
                    dest: 'dist/'
                }]
            },
            srcpreview2preview: {
                files: [{
                    expand: true,
                    cwd: 'src/preview',
                    src: '**',
                    dest: 'preview/'
                }]
            },
            radicjs2dist: {
                files: [{
                    expand: true,
                    cwd: 'lib/radicjs/<%= config.radicjs.dest %>',
                    src: '**/*.js',
                    dest: 'dist/dep/'
                }]
            },
            dist2demo: {
                files: [{
                    expand: true,
                    cwd: 'lib/radicjs/<%= config.radicjs.dest %>',
                    src: ['**/*.js', '*.js'],
                    dest: 'dist/dep/'
                }]
            }
        },
        clean: {
            radicjsdist: ['lib/radicjs/<%= config.radicjs.dest %>'],
            radicjsyaml: ['radicjs.yml'],
            demo: ['docs/demo/**']
        },
        watch: {
            widgets: {
                files: ['src/**/*', '!src/**/*.tpls.js'],
                tasks: ['copy:basewidget2dist', 'build:widgets']
            },
            previewhtml: {
                files: ['src/preview/**'],
                tasks: ['copy:srcpreview2preview', 'preprocess:previewhtml']
            },
            bootstrapsass: {
                files: ['src/bootstrap.scss', 'src/_base.scss'],
                tasks: ['sass:bootstrap']
            },
            ghwidgets: {
                files: ['src/github-widgets.scss'],
                tasks: ['sass:ghwidgets']
            }
        },
        publisher: {
            bower: {
                enabled: true
            },
            npm: {
                publish: true
            }
        }
    };

    require('load-grunt-tasks')(grunt);

    grunt.registerTask('widget', 'List widgets or use widget:WIDGETNAME to build the widget', function (target) {
        grunt.task.run('sass:ghwidgets');
        if (target) {
            grunt.task.run('build_widget:github-' + target);
        } else {
            origHeader('Available widget build commands');
            grunt.log.write('- widget:' + config.widgets.join('"\n- widget:'))
        }
    });

    grunt.registerTask('build:dep', 'Builds dependencies', ['subgrunt:radicjs', 'copy:radicjs2dist']); //, 'clean:radicjsdist']);

    grunt.registerTask('build:widgets', 'Builds all widgets', function (target) {
        var tasks = ['sass:ghwidgets'];
        _.each(config.widgets, function (widgetName) {
            tasks.push('build_widget:github-' + widgetName);
        });
        grunt.task.run(tasks)
    });

    grunt.registerTask('build:all', 'Builds all widgets, dependencies and creates minified versions to the dist folder', [
        'build:dep'
    ]);

    grunt.registerTask('preview:build', ['copy:srcpreview2preview', 'preprocess:previewhtml']);
    grunt.registerTask('demo:build', ['preview:build', 'clean:demo', 'copy:demo']);//, 'string-replace:demo']);
    grunt.registerTask('docs:publish', ['radic_jsdoc:docs', 'radic_coverage:docs', 'radic_ghpages_publish:docs']);



    grunt.initConfig(gc);
    require('./tasks/adjust')(grunt);
};
