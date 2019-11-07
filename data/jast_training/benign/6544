
var _ = require('lodash');

module.exports = function(grunt){

    return;
    var origHeader = grunt.log.header;

    grunt.config('availabletasks', {           // task
        tasks: {
            options: {
                filter: 'exclude',
                showTasks: ['user'],
                tasks: ['default', 'showtime', 'header'],
                groups: {
                    'Deploy': ['demo:build', 'demo:publish', 'publish'],
                    'Build tasks': ['build:all', 'build:dep', 'build:widgets', 'widget'],
                    'Development': ['watch']
                }
            },
            descriptions: {
                'build:all': '',
                'build:dep': '',
                'widget': '',
                'watch': 'Task',
                'demo:build': ''
            }
        }
    });

    grunt.log.header = function () {
    };

    grunt.registerTask('showtime', function () {
        require('time-grunt')(grunt);
    });


    grunt.registerTask('default', 'Overview', function () {
        origHeader('jQuery Github Widgets');
        grunt.task.run(['availabletasks']);
    });
    grunt.registerTask('header', function (target) {
        grunt.log.header = target == 'enable' ? origHeader : function(){};
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
