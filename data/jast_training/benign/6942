var Jasmine = require('jasmine');
var jrunner = new Jasmine();
var SpecReporter = require('jasmine-spec-reporter');
var noop = function () { };
jrunner.configureDefaultReporter({ print: noop });
jasmine.getEnv().addReporter(new SpecReporter());
jrunner.loadConfigFile('spec/support/jasmine.json');
jrunner.onComplete(function (passed) {
    if (passed) {
        console.log('All specs have passed');
    }
    else {
        console.log('At least one spec has failed');
    }
});
jrunner.execute();
process.exit();
//# sourceMappingURL=jasmine.js.map