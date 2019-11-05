$.loadPage = function(url, options, skip_state){
    var that = this;

    if(that.prevRequest){
      that.prevRequest.abort();
    }
    that.prevRequest = $.ajax(url, $.extend(options, {
      headers: {'X-Airload': 'true'},
      success:function(rsp, status, request){
        if( typeof(rsp) == "string" ){
            if(!skip_state){
              window.history.pushState(null , "" ,url);
            }
          var el = document.createElement('div');
          el.innerHTML = rsp;
          if($('title', el)){
            document.title = $('title', el).html();
          }

          for(var i in that.slot){
            var replaceBy = $(that.slot[i], el);
            if(replaceBy.length>0){
              $(that.slot[i]).replaceWith(replaceBy);
            }else{
              $(that.slot[i]).html('');
            }
          }

          $('body').scrollTop(0)
        }
        that.success();
      },
      error:function(rsp){
        if(rsp.readyState==4 && rsp.status==320){
            options.method = 'GET';
            options.data = undefined;
            $.loadPage.call(that, rsp.getResponseHeader('location'), options, skip_state);
            return;
        }
        that.error(rsp);
      },
      complete: function(){
        that.prevRequest = null;        
        that.complete();
      }
    }));
    that.start();
}

$.pageReady = function(el){
  var that = this;
  $(el).bind('submit', function(e){
    try{
      var el = e.target;
      if(el.tagName!='FORM'){
        el = $(el).parents('form');
        if(el.length==0){
          return;
        }
      }
      el = $(el);
      if(!el.hasClass('external') && !el.attr('target')){
        e.stopPropagation();
        e.preventDefault();
        var url = el.attr('action');
        if(!url){
          url = document.location.href;
        }

        var uploads = $('input[type=file]', el);
        if(uploads.length>0){
          var formData = new FormData();
          $(el.serializeArray()).each(function(i, item){
            formData.append(item.name, item.value);
          });

          uploads.each(function(i, ipt){
            formData.append($(ipt).attr('name'), ipt.files[0]);
          });

          $.loadPage.call(that, url, {
            method: el.attr('method'),
            data: formData,
            cache: false,
            processData: false,
            contentType: false
          });
        }else{
          $.loadPage.call(that, url, {
            method: el.attr('method'),
            data: el.serialize(),
          });
        }
      }
    }catch(err){
      e.stopPropagation();
      if(console && console.error)console.error(err);
      return false;
    }
  });

  $(el).bind('click', function(e){
    try{
      var el = e.target;
      if(el.tagName!='A'){
        el = $(el).parents('a');
        if(el.length==0){
          return;
        }
      }
      el = $(el);
      var href = el.attr('href');      
      if(!el.hasClass('external') && href!=undefined && !el.attr('target')){
        if( href == '' ){
          href = document.location.href;
        }
        if(href.substr(0,1)!='#' && !e.metaKey){
          e.stopPropagation();
          e.preventDefault();
          $.loadPage.call(that, href);
          return false;
        }
      }
    }catch(err){
      e.stopPropagation();
      e.preventDefault();
      if(console && console.error) console.error(err);
      return false;
    }
  });
}

$.airloadSetup = function(el, cfg){
  var context = $.extend({
      requestIdx:0,
      slot: ['.main-content'],
      success: function(){},
      start: function(){},
      error: function(rsp){
        if(rsp.responseText){
          window.history.pushState(null , "" ,url);
          document.body.innerHTML = rsp.responseText;
        }
      },
      complete: function(){}
    }, cfg);
  $.pageReady.call(context, el);
  window.onpopstate=function(s){
    $.loadPage.call(context, document.location.href, {}, true);
  }
}