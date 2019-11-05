var radic = require('radic'),
    inquirer = require('inquirer'),
    util = radic.util,
    path = require('path'),
    _ = require('lodash'),
    fs = require('fs-utils'),
    yaml = require('js-yaml');

/**
 * @namespace lib
 * @type {{RadicReport: (RadicReport|exports), getFrontMatterYaml: Function, replaceHighlightToGithubPages: Function, prompt: (exports.prompt|*)}}
 */
var lib = module.exports = {
    RadicReport: require('./istanbul-radic-report'),

    getFrontMatterYaml: function(filePath){
        return yaml.safeLoad(fs.readFileSync(filePath, 'utf-8').replace(/---/g, ''));
    },

    replaceHighlightToGithubPages: function(str){
        return str
            .replace(/```(?=\w)(\w*)/g, '{% highlight $1 %}')
            .replace(/```\n/g, '{% endhighlight %}\n');
    },

    prompt: inquirer.prompt
};
