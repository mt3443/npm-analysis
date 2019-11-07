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
templates['github.events.branch'] = template({"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, lambda=this.lambda, escapeExpression=this.escapeExpression, helperMissing=helpers.helperMissing;
  return "<script type=\"text/x-handlebars-template\">\n    <a href=\"https://github.com/"
    + escapeExpression(lambda(((stack1 = ((stack1 = (depth0 != null ? depth0.event : depth0)) != null ? stack1.repo : stack1)) != null ? stack1.name : stack1), depth0))
    + "/commits/"
    + escapeExpression(((helpers.branchName || (depth0 && depth0.branchName) || helperMissing).call(depth0, (depth0 != null ? depth0.event : depth0), {"name":"branchName","hash":{},"data":data})))
    + "\" target=\""
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0.target : depth0), "_blank", {"name":"default","hash":{},"data":data})))
    + "\" class=\"btn branch "
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0['class'] : depth0), "btn-xs btn-blue-grey", {"name":"default","hash":{},"data":data})))
    + "\">\n        <i class=\"fa fa-code-fork\">&nbsp;</i>"
    + escapeExpression(((helpers.branchName || (depth0 && depth0.branchName) || helperMissing).call(depth0, (depth0 != null ? depth0.event : depth0), {"name":"branchName","hash":{},"data":data})))
    + "\n    </a>\n</script>\n\n";
},"useData":true});
templates['github.events.commits'] = template({"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, lambda=this.lambda;
  return "<script type=\"text/x-handlebars-template\">\n    <a href=\""
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0.href : depth0), "javascript:;", {"name":"default","hash":{},"data":data})))
    + "\" data-github-event=\""
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.event : depth0)) != null ? stack1.id : stack1), depth0))
    + "\" target=\""
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0.target : depth0), "_blank", {"name":"default","hash":{},"data":data})))
    + "\"\n       title=\"Commit details\" class=\"commits btn "
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0['class'] : depth0), "btn-xs btn-teal", {"name":"default","hash":{},"data":data})))
    + "\">\n        "
    + escapeExpression(lambda(((stack1 = ((stack1 = (depth0 != null ? depth0.event : depth0)) != null ? stack1.payload : stack1)) != null ? stack1.size : stack1), depth0))
    + " commit"
    + escapeExpression(((helpers.pushName || (depth0 && depth0.pushName) || helperMissing).call(depth0, (depth0 != null ? depth0.event : depth0), {"name":"pushName","hash":{},"data":data})))
    + "\n    </a>\n</script>\n\n";
},"useData":true});
templates['github.events.commits.popover'] = template({"1":function(depth0,helpers,partials,data) {
  var stack1, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, lambda=this.lambda;
  return "            <li class=\""
    + escapeExpression(((helpers.evenOdd || (depth0 && depth0.evenOdd) || helperMissing).call(depth0, (data && data.index), "in", "out", {"name":"evenOdd","hash":{},"data":data})))
    + "\">\n                <img class=\"avatar\" src=\""
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.author : depth0)) != null ? stack1.avatar_url : stack1), depth0))
    + "\" alt=\"Avatar\" />\n                <div class=\"commit-message\">\n                    <span class=\"arrow\"></span>\n                    <a href=\"#\" class=\"commit-author\">"
    + escapeExpression(lambda(((stack1 = ((stack1 = (depth0 != null ? depth0.commit : depth0)) != null ? stack1.author : stack1)) != null ? stack1.name : stack1), depth0))
    + "</a>\n                    <span class=\"pull-right\">\n                    <span class=\"label label-success\">+"
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.stats : depth0)) != null ? stack1.additions : stack1), depth0))
    + "</span>\n                    <span class=\"label label-danger\">-"
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.stats : depth0)) != null ? stack1.deletions : stack1), depth0))
    + "</span>\n                        </span>\n                    <br>\n                    <span class=\"commit-body\">"
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.commit : depth0)) != null ? stack1.message : stack1), depth0))
    + "</span>\n                </div>\n            </li>\n";
},"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, lambda=this.lambda, escapeExpression=this.escapeExpression, helperMissing=helpers.helperMissing, buffer = "<script type=\"text/x-handlebars-template\">\n    <div class=\"github-events-commits-popover\">\n        <div>\n            <h4>"
    + escapeExpression(lambda(((stack1 = ((stack1 = (depth0 != null ? depth0.event : depth0)) != null ? stack1.actor : stack1)) != null ? stack1.login : stack1), depth0))
    + "</h4>\n            <span class=\"commit-desc\"> Pushed "
    + escapeExpression(lambda(((stack1 = ((stack1 = (depth0 != null ? depth0.event : depth0)) != null ? stack1.payload : stack1)) != null ? stack1.size : stack1), depth0))
    + " commits. </span>\n            <div class=\"commit-info\">\n                <i class=\"fa fa-github\"></i>\n                <span>"
    + escapeExpression(lambda(((stack1 = ((stack1 = (depth0 != null ? depth0.event : depth0)) != null ? stack1.repo : stack1)) != null ? stack1.name : stack1), depth0))
    + "</span>\n            </div>\n            <div class=\"commit-info\">\n                <i class=\"fa fa-code-fork\"></i>\n                <span>"
    + escapeExpression(((helpers.branchName || (depth0 && depth0.branchName) || helperMissing).call(depth0, (depth0 != null ? depth0.event : depth0), {"name":"branchName","hash":{},"data":data})))
    + "</span>\n            </div>\n        </div>\n\n        <ul class=\"commit-commits\">\n";
  stack1 = helpers.each.call(depth0, (depth0 != null ? depth0.commits : depth0), {"name":"each","hash":{},"fn":this.program(1, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + "        </ul>\n    </div>\n</script>\n";
},"useData":true});
templates['github.events'] = template({"1":function(depth0,helpers,partials,data) {
  var stack1, helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, lambda=this.lambda, buffer = "                <tr data-event-id=\""
    + escapeExpression(((helper = (helper = helpers.id || (depth0 != null ? depth0.id : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"id","hash":{},"data":data}) : helper)))
    + "\" data-event-index=\""
    + escapeExpression(lambda((data && data.key), depth0))
    + "\" class=\"gh-event\">\n                    <td class=\"gh-events-icon\">\n                        <div class=\"label label-sm label-"
    + escapeExpression(((helper = (helper = helpers.iconColor || (depth0 != null ? depth0.iconColor : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"iconColor","hash":{},"data":data}) : helper)))
    + "\">\n                            <i class=\""
    + escapeExpression(((helper = (helper = helpers.icon || (depth0 != null ? depth0.icon : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"icon","hash":{},"data":data}) : helper)))
    + "\"></i>\n                        </div>\n                    </td>\n                    <td class=\"gh-events-text\">";
  stack1 = ((helper = (helper = helpers.text || (depth0 != null ? depth0.text : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"text","hash":{},"data":data}) : helper));
  if (stack1 != null) { buffer += stack1; }
  return buffer + "</td>\n                    <td class=\"gh-events-time\"><time datetime=\""
    + escapeExpression(((helper = (helper = helpers.timeAgo || (depth0 != null ? depth0.timeAgo : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"timeAgo","hash":{},"data":data}) : helper)))
    + "\">"
    + escapeExpression(((helper = (helper = helpers.timeAgo || (depth0 != null ? depth0.timeAgo : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"timeAgo","hash":{},"data":data}) : helper)))
    + "</time> <i class=\"fa fa-clock-o\"></i></td>\n                </tr>\n";
},"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, lambda=this.lambda, escapeExpression=this.escapeExpression, buffer = "<script type=\"text/x-handlebars-template\">\n    <div  class=\""
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.options : depth0)) != null ? stack1.className : stack1), depth0))
    + "\" style=\"height: "
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.options : depth0)) != null ? stack1.height : stack1), depth0))
    + "px;\">\n            <table>\n";
  stack1 = helpers.each.call(depth0, (depth0 != null ? depth0.events : depth0), {"name":"each","hash":{},"fn":this.program(1, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + "            </table>\n    </div>\n</script>\n";
},"useData":true});
templates['github.events.issue'] = template({"1":function(depth0,helpers,partials,data) {
  var stack1, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;
  return "<span class=\"label label-success\">@</span>"
    + escapeExpression(((((stack1 = (depth0 && depth0.decorator)) && stack1.user) || helperMissing).call(depth0, ((stack1 = (depth0 != null ? depth0.issue : depth0)) != null ? stack1.user : stack1), {"name":"decorator.user","hash":{},"data":data})));
},"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, lambda=this.lambda, escapeExpression=this.escapeExpression, buffer = "<script type=\"text/x-handlebars-template\">\n    <a href=\"https://github.com/"
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.issue : depth0)) != null ? stack1.html_url : stack1), depth0))
    + "\" title=\""
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.issue : depth0)) != null ? stack1.title : stack1), depth0))
    + "\" data-github-issue=\""
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.issue : depth0)) != null ? stack1.id : stack1), depth0))
    + "\" target=\"_blank\" class=\"btn btn-xs yellow\">Issue "
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.issue : depth0)) != null ? stack1.number : stack1), depth0))
    + "</a>\n    ";
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.createUserLink : depth0), {"name":"if","hash":{},"fn":this.program(1, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + "\n</script>\n";
},"useData":true});
templates['github.events.repo'] = template({"1":function(depth0,helpers,partials,data) {
  var stack1, helper, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, functionType="function";
  return "        <a href=\"https://github.com/"
    + escapeExpression(((helpers.repoOwner || (depth0 && depth0.repoOwner) || helperMissing).call(depth0, ((stack1 = (depth0 != null ? depth0.repo : depth0)) != null ? stack1.name : stack1), {"name":"repoOwner","hash":{},"data":data})))
    + "\" target=\""
    + escapeExpression(((helper = (helper = helpers.target || (depth0 != null ? depth0.target : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"target","hash":{},"data":data}) : helper)))
    + "\" class=\"repo "
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0.ownerClass : depth0), "btn btn-xs btn-deep-orange", {"name":"default","hash":{},"data":data})))
    + "\"><i class=\"fa fa-github-alt\"></i> "
    + escapeExpression(((helpers.repoOwner || (depth0 && depth0.repoOwner) || helperMissing).call(depth0, ((stack1 = (depth0 != null ? depth0.repo : depth0)) != null ? stack1.name : stack1), {"name":"repoOwner","hash":{},"data":data})))
    + "</a>\n";
},"3":function(depth0,helpers,partials,data) {
  var stack1, helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = "    <a href=\""
    + escapeExpression(((helper = (helper = helpers.href || (depth0 != null ? depth0.href : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"href","hash":{},"data":data}) : helper)))
    + "\" target=\""
    + escapeExpression(((helper = (helper = helpers.target || (depth0 != null ? depth0.target : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"target","hash":{},"data":data}) : helper)))
    + "\" class=\"repo "
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0['class'] : depth0), "btn btn-xs btn-orange", {"name":"default","hash":{},"data":data})))
    + "\" title=\""
    + escapeExpression(((helper = (helper = helpers.description || (depth0 != null ? depth0.description : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"description","hash":{},"data":data}) : helper)))
    + "\">\n        ";
  stack1 = helpers.unless.call(depth0, (depth0 != null ? depth0.owner : depth0), {"name":"unless","hash":{},"fn":this.program(4, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + " "
    + escapeExpression(((helpers.repoName || (depth0 && depth0.repoName) || helperMissing).call(depth0, ((stack1 = (depth0 != null ? depth0.repo : depth0)) != null ? stack1.name : stack1), {"name":"repoName","hash":{},"data":data})))
    + "\n    </a>\n";
},"4":function(depth0,helpers,partials,data) {
  return "<i class=\"fa fa-github-alt\"></i>";
  },"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, buffer = "<script type=\"text/x-handlebars-template\">\n";
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.owner : depth0), {"name":"if","hash":{},"fn":this.program(1, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.repo : depth0), {"name":"if","hash":{},"fn":this.program(3, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + "</script>\n\n";
},"useData":true});
templates['github.events.tag'] = template({"1":function(depth0,helpers,partials,data) {
  return "<i class=\"fa fa-tag\"></i>";
  },"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, helper, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, functionType="function", buffer = "<script type=\"text/x-handlebars-template\">\n    <a href=\""
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0.href : depth0), "#", {"name":"default","hash":{},"data":data})))
    + "\" target=\""
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0.target : depth0), "_blank", {"name":"default","hash":{},"data":data})))
    + "\" class=\"tagged "
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0['class'] : depth0), "label label-xs label-green badge", {"name":"default","hash":{},"data":data})))
    + "\" title=\""
    + escapeExpression(((helper = (helper = helpers.description || (depth0 != null ? depth0.description : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"description","hash":{},"data":data}) : helper)))
    + "\">\n        ";
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.icon : depth0), {"name":"if","hash":{},"fn":this.program(1, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + " "
    + escapeExpression(((helper = (helper = helpers.tag || (depth0 != null ? depth0.tag : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"tag","hash":{},"data":data}) : helper)))
    + "</a>\n</script>\n";
},"useData":true});
templates['github.events.user'] = template({"1":function(depth0,helpers,partials,data) {
  var helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;
  return "<img src=\""
    + escapeExpression(((helper = (helper = helpers.avatar || (depth0 != null ? depth0.avatar : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"avatar","hash":{},"data":data}) : helper)))
    + "\">";
},"3":function(depth0,helpers,partials,data) {
  return "            <i class='fa fa-user'></i>\n";
  },"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, helper, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, functionType="function", buffer = "<script type=\"text/x-handlebars-template\">\n\n    <a href=\"https://github.com/"
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0.login : depth0), (depth0 != null ? depth0.username : depth0), {"name":"default","hash":{},"data":data})))
    + "\" target=\""
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0.target : depth0), "_blank", {"name":"default","hash":{},"data":data})))
    + "\" class=\""
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0['class'] : depth0), "btn btn-xs btn-primary", {"name":"default","hash":{},"data":data})))
    + "\"  "
    + escapeExpression(((helper = (helper = helpers.attributes || (depth0 != null ? depth0.attributes : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"attributes","hash":{},"data":data}) : helper)))
    + " >\n        ";
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.avatar : depth0), {"name":"if","hash":{},"fn":this.program(1, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  buffer += "\n";
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.icon : depth0), {"name":"if","hash":{},"fn":this.program(3, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + "        "
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0.login : depth0), (depth0 != null ? depth0.username : depth0), {"name":"default","hash":{},"data":data})))
    + "\n    </a>\n</script>\n\n";
},"useData":true});
templates['github.events.user.modal'] = template({"1":function(depth0,helpers,partials,data) {
  var helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;
  return "                        <div class=\"profile-usertitle-job\">"
    + escapeExpression(((helper = (helper = helpers.company || (depth0 != null ? depth0.company : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"company","hash":{},"data":data}) : helper)))
    + "</div>";
},"3":function(depth0,helpers,partials,data) {
  var helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;
  return "                        <div class=\"profile-usertitle-job\">"
    + escapeExpression(((helper = (helper = helpers.location || (depth0 != null ? depth0.location : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"location","hash":{},"data":data}) : helper)))
    + "</div>";
},"5":function(depth0,helpers,partials,data) {
  var helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;
  return "                        <span class=\"profile-desc-text\">"
    + escapeExpression(((helper = (helper = helpers.bio || (depth0 != null ? depth0.bio : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"bio","hash":{},"data":data}) : helper)))
    + "</span>\n";
},"7":function(depth0,helpers,partials,data) {
  var helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;
  return "                        <div class=\"margin-top-20 profile-desc-link\">\n                            <i class=\"fa fa-pencil\"></i>\n                            <a href=\""
    + escapeExpression(((helper = (helper = helpers.blog || (depth0 != null ? depth0.blog : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"blog","hash":{},"data":data}) : helper)))
    + "\">Blog</a>\n                        </div>\n";
},"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = "<script type=\"text/x-handlebars-template\">\n    <div>\n        <div class=\"row row-col-border-right\">\n            <div class=\"col-md-3\">\n                <div class=\"profile-userpic\">\n                    <img src=\""
    + escapeExpression(((helper = (helper = helpers.avatar_url || (depth0 != null ? depth0.avatar_url : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"avatar_url","hash":{},"data":data}) : helper)))
    + "\" class=\"img-responsive\" alt=\"\">\n                </div>\n                <div class=\"profile-usertitle\">\n                    <div class=\"profile-usertitle-name\">\n                        "
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0.name : depth0), (depth0 != null ? depth0.login : depth0), {"name":"default","hash":{},"data":data})))
    + "\n                    </div>\n\n";
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.company : depth0), {"name":"if","hash":{},"fn":this.program(1, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  buffer += "\n\n";
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.location : depth0), {"name":"if","hash":{},"fn":this.program(3, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  buffer += "\n\n                </div>\n            </div>\n            <div class=\"col-md-4\">\n                <div class=\"row list-separated profile-stat\">\n                    <div class=\"col-md-4 col-sm-4 col-xs-6\">\n                        <div class=\"uppercase profile-stat-title\">\n                            "
    + escapeExpression(((helper = (helper = helpers.public_repos || (depth0 != null ? depth0.public_repos : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"public_repos","hash":{},"data":data}) : helper)))
    + "\n                        </div>\n                        <div class=\"uppercase profile-stat-text\">\n                            Repositories\n                        </div>\n                    </div>\n                    <div class=\"col-md-4 col-sm-4 col-xs-6\">\n                        <div class=\"uppercase profile-stat-title\">\n                            "
    + escapeExpression(((helper = (helper = helpers.public_gists || (depth0 != null ? depth0.public_gists : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"public_gists","hash":{},"data":data}) : helper)))
    + "\n                        </div>\n                        <div class=\"uppercase profile-stat-text\">\n                            Gists\n                        </div>\n                    </div>\n                    <div class=\"col-md-4 col-sm-4 col-xs-6\">\n                        <div class=\"uppercase profile-stat-title\">\n                            "
    + escapeExpression(((helper = (helper = helpers.followers || (depth0 != null ? depth0.followers : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"followers","hash":{},"data":data}) : helper)))
    + "\n                        </div>\n                        <div class=\"uppercase profile-stat-text\">\n                            Followers\n                        </div>\n                    </div>\n                </div>\n                <div>\n                    <h4 class=\"profile-desc-title\">About "
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0.name : depth0), (depth0 != null ? depth0.login : depth0), {"name":"default","hash":{},"data":data})))
    + "</h4>\n";
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.bio : depth0), {"name":"if","hash":{},"fn":this.program(5, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.blog : depth0), {"name":"if","hash":{},"fn":this.program(7, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + "                    <div class=\"margin-top-20 profile-desc-link\">\n                        <i class=\"fa fa-git\"></i>\n                        <a href=\""
    + escapeExpression(((helper = (helper = helpers.html_url || (depth0 != null ? depth0.html_url : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"html_url","hash":{},"data":data}) : helper)))
    + "\">Github overview</a>\n                    </div>\n                </div>\n            </div>\n            <div class=\"col-md-5\">\n                <div class=\"user-modal-profile\"></div>\n            </div>\n        </div>\n        <div class=\"row\">\n            <div class=\"col-md-12\">\n                <div class=\"user-modal-events\"></div>\n            </div>\n        </div>\n    </div>\n</script>\n";
},"useData":true});
templates['github.events.user.popover'] = template({"1":function(depth0,helpers,partials,data) {
  var helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;
  return "<div class=\"profile-usertitle-job\">"
    + escapeExpression(((helper = (helper = helpers.company || (depth0 != null ? depth0.company : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"company","hash":{},"data":data}) : helper)))
    + "</div>";
},"3":function(depth0,helpers,partials,data) {
  var helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;
  return "<div class=\"profile-usertitle-job\">"
    + escapeExpression(((helper = (helper = helpers.loctation || (depth0 != null ? depth0.loctation : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"loctation","hash":{},"data":data}) : helper)))
    + "</div>";
},"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = "<script type=\"text/x-handlebars-template\">\n    <div class=\"github-events-user-popover\">\n        <div class=\"profile-userpic\">\n            <img src=\""
    + escapeExpression(((helper = (helper = helpers.avatar_url || (depth0 != null ? depth0.avatar_url : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"avatar_url","hash":{},"data":data}) : helper)))
    + "\" class=\"img-responsive\" alt=\"\">\n        </div>\n        <div class=\"profile-usertitle\">\n            <div class=\"profile-usertitle-name\">\n                "
    + escapeExpression(((helpers['default'] || (depth0 && depth0['default']) || helperMissing).call(depth0, (depth0 != null ? depth0.name : depth0), (depth0 != null ? depth0.login : depth0), {"name":"default","hash":{},"data":data})))
    + "\n            </div>\n\n            ";
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.company : depth0), {"name":"if","hash":{},"fn":this.program(1, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  buffer += "\n\n            ";
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.location : depth0), {"name":"if","hash":{},"fn":this.program(3, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + "\n\n        </div>\n        <div class=\"profile-userbuttons\">\n            <span class=\"label label-info\"> Click for dropdown menu </span>\n        </div>\n    </div>\n</script>\n\n";
},"useData":true});
})();
;
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
