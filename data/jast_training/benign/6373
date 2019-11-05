/*
Github Profile jquery widget
http://robinradic.github.io/github-profile-widget

Copyright © 2014 Robin Radic - MIT License (http://radic.mit-license.org)

Copyright © 2014 Piotr Lewandowski
Original idea from https://github.com/piotrl/github-profile-widget
Complete javascript rewrite
Uses most of the original CSS
*/
(function() {
  var template = Handlebars.template, templates = Handlebars.templates = Handlebars.templates || {};
templates['github.profile'] = template({"1":function(depth0,helpers,partials,data) {
  var stack1, lambda=this.lambda, escapeExpression=this.escapeExpression;
  return "            <div class=\"profile\">\n                <img src=\""
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.user : depth0)) != null ? stack1.avatar_url : stack1), depth0))
    + "\" class=\"avatar\">\n                <a href=\""
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.user : depth0)) != null ? stack1.html_url : stack1), depth0))
    + "\" class=\"name\">"
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.user : depth0)) != null ? stack1.name : stack1), depth0))
    + "</a>\n\n                <div class=\"followMe\">\n                    <a href=\""
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.user : depth0)) != null ? stack1.html_url : stack1), depth0))
    + "\" class=\"follow-button\">Follow @"
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.user : depth0)) != null ? stack1.login : stack1), depth0))
    + "</a>\n                    <span class=\"followers\">"
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.user : depth0)) != null ? stack1.followers : stack1), depth0))
    + "</span>\n                </div>\n            </div>\n";
},"3":function(depth0,helpers,partials,data) {
  var stack1, buffer = "            <div class=\"languages\">\n                ";
  stack1 = helpers['if'].call(depth0, ((stack1 = (depth0 != null ? depth0.options : depth0)) != null ? stack1.languagesHeaderText : stack1), {"name":"if","hash":{},"fn":this.program(4, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  buffer += "\n                <table class=\"languages-list\">\n                    <thead>\n                    <tr>\n                        <th>Language</th>\n                        <th>Lines of code</th>\n                    </tr>\n                    </thead>\n                    <tbody>\n";
  stack1 = helpers.each.call(depth0, (depth0 != null ? depth0.languages : depth0), {"name":"each","hash":{},"fn":this.program(6, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + "                    </tbody>\n                </table>\n            </div>\n";
},"4":function(depth0,helpers,partials,data) {
  var stack1, lambda=this.lambda, escapeExpression=this.escapeExpression;
  return "<span class=\"header\">"
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.options : depth0)) != null ? stack1.languagesHeaderText : stack1), depth0))
    + "</span>";
},"6":function(depth0,helpers,partials,data) {
  var helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;
  return "                        <tr>\n                            <td>"
    + escapeExpression(((helpers.arrayIndex || (depth0 && depth0.arrayIndex) || helperMissing).call(depth0, depth0, 0, {"name":"arrayIndex","hash":{},"data":data})))
    + "</td>\n                            <td>\n                                <small>"
    + escapeExpression(((helpers.arrayIndex || (depth0 && depth0.arrayIndex) || helperMissing).call(depth0, depth0, 1, {"name":"arrayIndex","hash":{},"data":data})))
    + "</small>\n                            </td>\n                        </tr>\n";
},"8":function(depth0,helpers,partials,data) {
  var stack1, buffer = "            <div class=\"repos\">\n                ";
  stack1 = helpers['if'].call(depth0, ((stack1 = (depth0 != null ? depth0.options : depth0)) != null ? stack1.repositoriesHeaderText : stack1), {"name":"if","hash":{},"fn":this.program(9, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  buffer += "\n";
  stack1 = helpers.each.call(depth0, (depth0 != null ? depth0.repositories : depth0), {"name":"each","hash":{},"fn":this.program(11, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + "            </div>\n";
},"9":function(depth0,helpers,partials,data) {
  var stack1, lambda=this.lambda, escapeExpression=this.escapeExpression;
  return "<span class=\"header\">"
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.options : depth0)) != null ? stack1.repositoriesHeaderText : stack1), depth0))
    + "</span>";
},"11":function(depth0,helpers,partials,data) {
  var helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;
  return "                    <a href=\""
    + escapeExpression(((helper = (helper = helpers.html_url || (depth0 != null ? depth0.html_url : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"html_url","hash":{},"data":data}) : helper)))
    + "\" class=\"repo-link\" data-repository=\""
    + escapeExpression(((helper = (helper = helpers.name || (depth0 != null ? depth0.name : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"name","hash":{},"data":data}) : helper)))
    + "\" title=\""
    + escapeExpression(((helper = (helper = helpers.description || (depth0 != null ? depth0.description : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"description","hash":{},"data":data}) : helper)))
    + "\">\n                        <span class=\"repo-name\">"
    + escapeExpression(((helper = (helper = helpers.name || (depth0 != null ? depth0.name : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"name","hash":{},"data":data}) : helper)))
    + "</span><span class=\"updated\">Updated: "
    + escapeExpression(((helper = (helper = helpers.updated_at_formatted || (depth0 != null ? depth0.updated_at_formatted : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"updated_at_formatted","hash":{},"data":data}) : helper)))
    + "</span><span class=\"star\">"
    + escapeExpression(((helper = (helper = helpers.stargazers_count || (depth0 != null ? depth0.stargazers_count : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"stargazers_count","hash":{},"data":data}) : helper)))
    + "</span>\n                    </a>\n";
},"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, lambda=this.lambda, escapeExpression=this.escapeExpression, buffer = "<script type=\"text/x-handlebars-template\">\n    <div data-username=\""
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.user : depth0)) != null ? stack1.login : stack1), depth0))
    + "\" class=\""
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.options : depth0)) != null ? stack1.className : stack1), depth0))
    + "\">\n";
  stack1 = helpers['if'].call(depth0, ((stack1 = (depth0 != null ? depth0.options : depth0)) != null ? stack1.showProfile : stack1), {"name":"if","hash":{},"fn":this.program(1, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  stack1 = helpers['if'].call(depth0, ((stack1 = (depth0 != null ? depth0.options : depth0)) != null ? stack1.showLanguages : stack1), {"name":"if","hash":{},"fn":this.program(3, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  buffer += "\n";
  stack1 = helpers['if'].call(depth0, ((stack1 = (depth0 != null ? depth0.options : depth0)) != null ? stack1.showRepositories : stack1), {"name":"if","hash":{},"fn":this.program(8, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + "    </div>\n</script>\n";
},"useData":true});
})();
;
/** @fileoverview githubProfile - A jQuery plugin that shows a user profile with it's top repos/languages
 *
 * jQuery Github Profile Widget is a plugin that shows a github user profile with top repositories, languages, followers etc.
 * Highly customizable options. Multiple ways to build and include into your project.
 *
 *
 * @author Robin Radic
 * @copyright Robin Radic 2014
 * @license MIT License
 * @link https://github.com/robinradic/jquery-github-widgets
 * @link http://radic.mit-license.org
 * @version 0.0.1
 * @summary A jQuery plugin that shows a user profile with it's top repos/languages
 */
(function (factory) {

        factory(jQuery, radic);

}(function ($, R) {
    R.template.registerHelper('arrayIndex', function (context, ndx) {
        return context[ndx];
    });

    /**
     * @namespace radic
     * @namespace radic.githubProfile
     */
    $.widget('radic.githubProfile', $.github.widget, /** @lends radic.githubProfile */ {
        version: '0.0.1',

        /**
         * Default options
         * @property {Object}  options - the default options
         * @property {String}  options.username - the user login name or id
         * @property {Boolean}  options.showProfile - Show user details
         * @property {Boolean}  options.showFollow - Show follow button
         * @property {Boolean}  options.showLanguages - Show top langauges
         * @property {String}  options.showRepositories - Show top repositories
         * @property {String}  options.template - Template id used by Handlebars
         * @property {String}  options.className - Root element class name
         * @property {Boolean}  options.spinner - Use spinner while loading
         * @property {Object}  options.spinnerOptions - Spinner options
         * @property {String}  options.sortBy - 'stars' or 'updateTime'
         * @property {String}  options.repositoriesHeaderText - Header caption
         * @property {Number}  options.repositoriesLimit - Limit the amount of repositories shown
         * @property {String}  options.languagesHeaderText - Header caption
         * @property {Number}  options.languagesLimit - Limit the amount of languages shown
         */
        options: {
            username: null,

            showProfile: true,
            showFollow: true,
            showLanguages: true,
            showRepositories: true,

            template: 'github.profile',
            className: 'gh-profile-widget',


            sortBy: 'stars', // possible: 'stars', 'updateTime'
            repositoriesHeaderText: 'Most starred repositories',
            repositoriesLimit: 5,

            languagesHeaderText: 'Top languages',
            languagesLimit: 5
        },
        /**
         * Events
         * @property {Function}  options.create - Limit the amount of languages shown
         */

        /**
         * Refreshes the data and repaints the widget. Usefull in case of option changes
         * @example
         * $('#thewidget').githubProfile('refresh');
         */
        refresh: function(){
            var self = this;
            self.data = {};
            self._trigger('refresh');
            self.element.html('');
            self._spin();
            self._getData(function () {
                self._spin(false);
                self.repaint();
                self._trigger('refreshed');
            });
        },

        /**
         * Repaints the widget. Usefull in case of option changes
         */
        repaint: function(){
            var self = this;
            self._trigger('repaint');
            self.element.html('');
            var $template = self._compile(self.options.template, $.extend({ options: self.options }, self.data));
            self.element.html($template);
            $template.find('.repo-link').on('click', function(e){
                self._trigger('onRepositoryClick', null, $(this).data('repository'));
            });
            self._trigger('repainted');
        },

        _create: function () {
            if(this.options.username === null || ! R.isString(this.options.username)){
                console.error('githubProfile widget has been initialized without the required username option');
                return;
            }

            this.refresh();
        },

        _sortLanguages: function (languages) {
            var self = this;
            var topLangs = [];
            for (var k in languages) {
                topLangs.push([k, languages[k]]);
            }
            topLangs.sort(function (a, b) {
                return b[1] - a[1];
            });
            return topLangs.slice(0, this.options.languagesLimit);
        },

        _sortRepositories: function (repositories) {
            var self = this;
            repositories.sort(function (a, b) {
                if (self.options.sortBy == 'stars') {
                    return b.stargazers_count - a.stargazers_count;
                } else {
                    return new Date(b.updated_at).getTime() - new Date(a.updated_at).getTime();
                }
            });
            return repositories.slice(0, self.options.repositoriesLimit);
        },

        _getData: function (callback) {
            var self = this;
            var username = this.options.username;

            R.async.waterfall([
                function (done) {
                    //sR.github.setTransport('')
                    var u = R.github.users(username, function (userData, second) {
                        self.data.user = userData;
                        self._trigger('onReceivedUser'); //, null, self.options);
                        //console.info('even more data', userData, R.defined(second) ? second : 'no second');

                        done(null);
                    });
                    console.log('u2', u);
                },
                function (done) {

                    R.github.users.repos(username, null, 1, 100, function (repositories) {
                        self.data.repositories = repositories;
                        self._trigger('onReceivedRepositories'); //, null, {repoData:repoData}, self.options);
                        done(null); //, {user: userData, repos: repoData});
                    })
                },
                function (done) {
                    self.data.languages = {};

                    R.async.each(self.data.repositories, function(repo, next){

                        repo.updated_at_formatted = radic.time.ago(repo.updated_at);
                        var doLang = function(langData){
                            $.each(langData, function(i, lang){
                                if(typeof self.data.languages[i] === 'undefined'){
                                    self.data.languages[i] = lang;
                                } else {
                                    self.data.languages[i] += lang;
                                }
                            });
                        };

                        var cached = R.storage.get('github-profile-widget-languages', {json: true});
                        if(cached) {
                            self.data.languages = cached.languages;
                            next();
                        } else {
                            R.github.repos.languages(username, repo.name, function (langData) {
                                doLang(langData);
                                R.storage.set('github-profile-widget-languages', {languages: self.data.languages}, {expires: 60, json: true});
                                next();
                            });
                        }
                    }, function(){

                        done(null)
                    })
                },
                function (done) {
                    self._trigger('beforeSortRepositories');
                    self.data.repositories = self._sortRepositories(self.data.repositories);
                    self._trigger('afterSortRepositories');
                    done(null)
                },
                function (done) {
                    self._trigger('beforeSortLanguages');
                    self.data.languages = self._sortLanguages(self.data.languages);
                    self._trigger('afterSortLanguages');
                    done(null);

                }
            ], function(err, result){
                callback();
            })
        },


        _destroy: function () {
            this.element.html('');
            this._trigger('destroyed', null);
        },

        _setOption: function (key, value) {

            this._super(key, value);


            if(key === 'username'){
                this.refresh();
            }
        },

        /**
         * Get or set an option
         * @param {String} key
         * @param value
         * @example
         * var username = $('#mywidget').githubProfile('option', 'username');
         * $('#mywidget').githubProfile('option', 'username', 'AwesomeJohn');
         */
        option: function(key, value){
            this._super(key, value);
        }
    });

}));
