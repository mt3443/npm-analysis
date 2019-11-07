var path = require('path'),
    fs = require('fs-extra'),

    _ = require('lodash'),

    chai = require('chai'),
    expect = chai.expect,
    assert = chai.assert,
    should = chai.should(),

    sinon = require('sinon');


describe('github-widget', function () {
    it('should be ok', function(){
        expect(true).to.eql(true);
    });

    var env = require('jsdom').env
        , html = '<html><body><h1>Hello World!</h1><p class="hello">Heya Big World!</body></html>'
        ;

    // first argument can be html string, filename, or url
    env(html, function (errors, window) {
        console.log(errors);

        var $ = require('jquery')(window);
        var githubwidget = require('../src/github-widget');
        console.log(githubwidget);
        console.log($('.hello').text());
    });
});
