/**
 * Copyright 2014 Robin Radic - All rights reserved.
 */
(function (factory) {
    factory(jQuery, radic);
}(function ($, R) {
    var texts = {
        _compile: function (template, data, options) {
            options = options || {};
            return $(Handlebars.templates['github.events.' + template](data)).html();
        },
        issue: function (issue, options) {
            options = options || {};
            return this._compile('actor', $.extend({actor: actor}, options));
        },
        tag: function (payload, options) {
            options = options || {};
            return this._compile('tag', $.extend({tag: payload.ref, description: payload.description, decorator: this}, options));
        },
        user: function (user, options) {
            options = options || {};
            return this._compile('user', $.extend(user, options));
        },

        repo: function (repo, options) {
            options = options || {};
            return this._compile('repo', $.extend({repo: repo}, options));
        },
        commits: function (event, options) {
            options = options || {};
            return this._compile('commits', $.extend({event: event}, options));
        },
        branch: function (event, options) {
            options = options || {};
            return this._compile('branch', $.extend({event: event}, options));
        }
    };

    $.widget('radic.githubEvents', $.github.widget, {
        version: '0.0.1',
        options: {
            username: '',
            template: 'github.events',
            className: 'gh-events-widget',
            max: 60,
            height: 300,
            output: {
                events: {
                    default: {
                        icon: 'fa fa-info',
                        text: 'A github event has been triggered',
                        iconColor: 'default',
                        link: false
                    },
                    CommitCommentEvent: {
                        icon: 'fa fa-edit',
                        text: 'New comment on a commit'
                    },
                    CreateEvent: {
                        icon: 'fa fa-plus',
                        iconColor: 'warning',
                        text: function (event) {
                            var str = '';

                            if (event.payload.ref_type === 'tag') {
                                this.icon = 'fa fa-tag';
                                this.iconColor = 'green';
                                str += texts.tag(event.payload);
                                str += " tagged by ";
                            }

                            str += '<div class="btn-group">';
                            str += texts.user(event.actor, {icon: true, class: 'btn btn-xs btn-orange'});
                            str += texts.repo(event.repo, {class: 'btn btn-xs btn-primary'});
                            str += '</div>';
                            //console.log('create event text', str);
                            // str += event.repo.;
                            //console.warn(this);
                            return str.replace("\n", "");

                        }
                    },
                    DeleteEvent: {
                        icon: 'fa fa-trash',
                        iconColor: 'default',
                        text: 'A branch or tag has been deleted'
                    },
                    DeploymentEvent: {
                        icon: 'fa fa-',
                        iconColor: 'default',
                        text: ''
                    },
                    DeploymentStatusEvent: {
                        icon: 'fa fa-',
                        iconColor: 'default',
                        text: ''
                    },
                    DownloadEvent: {
                        icon: 'fa fa-cloud-download',
                        iconColor: 'default',
                        text: 'A new download has been created'
                    },
                    FollowEvent: {
                        icon: 'fa fa-bullhorn',
                        iconColor: 'default',
                        text: 'A user started following me'
                    },
                    ForkEvent: {
                        icon: 'fa fa-code-fork',
                        iconColor: 'default',
                        text: 'A repository was forked'
                    },
                    ForkApplyEvent: {
                        icon: 'fa fa-code-fork',
                        iconColor: 'default',
                        text: ''
                    },
                    GistEvent: {
                        icon: 'fa fa-git',
                        iconColor: 'default',
                        text: 'A gist has been created or updated'
                    },
                    GollumEvent: {
                        icon: 'fa fa-git',
                        iconColor: 'default',
                        text: 'A wiki page has been created or updated'
                    },
                    IssueCommentEvent: {
                        icon: 'fa fa-comment-o',
                        iconColor: 'info',
                        text: 'An issue received a new comment'
                    },
                    IssuesEvent: {
                        icon: 'fa fa-exclamation-triangle',
                        iconColor: 'warning',
                        text: function (event) {
                            /*
                             var action = event.payload.action;
                             action = action === 'started' ? 'starred' : action;
                             return texts.actor(event.actor) + ' ' + action + ' ' + texts.issue(event.payload.issue);
                             */
                            return 'IssuesEvent has occured';
                        }
                    },
                    MemberEvent: {
                        icon: 'fa fa-sitemap',
                        iconColor: 'default',
                        text: 'A user is added as collaborator to a repository'
                    },
                    PageBuildEvent: {
                        icon: 'fa fa-file-o',
                        iconColor: 'default',
                        text: ''
                    },
                    PublicEvent: {
                        icon: 'fa fa-users',
                        iconColor: 'default',
                        text: ''
                    },
                    PullRequestEvent: {
                        icon: 'fa fa-sort-desc',
                        iconColor: 'default',
                        text: ''
                    },
                    PullRequestReviewCommentEvent: {
                        icon: 'fa fa-random',
                        iconColor: 'default',
                        text: ''
                    },
                    PushEvent: {
                        icon: 'fa fa-save',
                        text: function (event) {

                            return $(document.createElement('span'))
                                .append(texts.user(event.actor, {icon: true}))
                                .append(
                                $(document.createElement('div')).addClass('btn-group')

                                    .append(texts.branch(event))
                                    .append(texts.commits(event))
                            )
                                .append(' to ')
                                .append(texts.repo(event.repo))
                                .html();

                            // return 'PushEvent has occured';
                        },
                        iconColor: 'success'
                    },
                    ReleaseEvent: {
                        icon: 'fa fa-chain-broken',
                        text: 'A new release has been published',
                        iconColor: 'default'
                    },
                    StatusEvent: {
                        icon: 'fa fa-info',
                        text: 'The status of a Git commit has changed',
                        iconColor: 'default'
                    },
                    TeamAddEvent: {
                        icon: 'fa fa-plus',
                        text: 'A user has been added to the team',
                        iconColor: 'default'
                    },
                    WatchEvent: {
                        icon: 'fa fa-star',
                        text: function (event) {
                            /*
                             var action = event.payload.action;
                             action = action === 'started' ? 'starred' : action;
                             return texts.actor(event.actor) + ' ' + action + ' ' + texts.repo(event.repo);
                             */
                            return 'WatchEvent has occured';
                        },
                        iconColor: 'warning'
                    }
                }
            }
        },

        _data: {
            eventData: {},
            eventTypes: {}
        },

        repaint: function () {
            var self = this;
            self._trigger('repaint');
            var $template = self._compile(self.options.template, self.data);
            self.element.html($template);
            self._trigger('repainted');
        },

        refresh: function () {
            var self = this;
            self._trigger('refresh');
            self.element.html('');
            self._spin();
            self._fetchEventData(function (data) {
                self._spin(false);
                self.data = $.extend({options: self.options}, data);
                self.repaint();
                self._trigger('refreshed');
            });
        },

        _create: function () {
            var self = this;

            self._data = {
                eventData: {},
                eventTypes: {}
            };

            this.$widget = null;

            // Create a seperate copy of all event triggers and merge the defaults
            $.each(this.options.output.events, function (type, event) {
                if (type === 'default') return;
                self._data.eventTypes[type] = $.extend(R.cloneDeep(self.options.output.events.default), event);
            });

            this.refresh();
        },


        getEvent: function (eventID) {
            return this._data.eventData[eventID];
        },

        _fetchEventData: function (callback) {
            var self = this;
            R.github.users.events(this.options.username, 0, this.options.max, function (events) {

                var eventData = [];
                for (var i = 0; i < events.length; i++) {
                    var event = self._getProcessedEvent(events[i]);
                    eventData.push(event);
                    self._data.eventData[event.id] = event;
                }

                callback({events: eventData});
            });
        },

        _getProcessedEvent: function (eventData) {
            var self = this;
            var event = R.cloneDeep(self._data.eventTypes[eventData.type]);
            if (R.isFunction(event.text)) {
                event.text = event.text.apply(event, [eventData]);
            }
            event.id = eventData.id;
            event.raw = eventData;
            event.timeAgo = R.time.ago(eventData.created_at);
            event.time = eventData.created_at;
            return event;
        },


        _destroy: function () {
            this.element.html('');
        }


    });

}));
