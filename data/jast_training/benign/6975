define([
    "./core"
], function( radic ) {

    radic.template = Handlebars;
    radic.template.get = function(name, data){
        var template = radic.template.templates[name];
        if(radic.isUndefined(data)){
            return template;
        }
        var html = template(data);
        return $($(html).html().trim());
    };


    return radic;

});
