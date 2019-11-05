module.exports = function(grunt) {
    'use strict';

    grunt.loadTasks('tasks');

    grunt.initConfig({
        radic_jsdoc: {
            docs: {
                docsPath: 'docs'
            }
        },
        radic_jsdoc_mdpages: {
            docs: {
                files: [{
                    cwd: 'test/mdpages',
                    src: '*.md',
                    dest: 'docs',
                    expand: true
                },{
                    src: 'README.md',
                    dest: 'docs/index.md'
                }]
            }
        },
        git: {
            docs: {
                options: {
                    cwd: 'docs',
                    ignoreErrors: true
                },
                commands: [
                    ['add', { A: true }],
                    ['commit', { m: 'Auto commit & push' }],
                    ['push', { u: 'origin' }, 'ghpages']
                ]
            }
        }
    });


    grunt.registerTask('docs', ['radic_jsdoc:docs', 'radic_jsdoc_mdpages:docs', 'git:docs']);
};
