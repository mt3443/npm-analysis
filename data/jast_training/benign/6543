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
