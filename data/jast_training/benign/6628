#!/usr/bin/env node


var path = require('path');
var cpx = require('cpx');
var mkdirp = require('mkdirp');
var glob = require('glob');
var del = require('del');
var mv = require('mv');
var minimist = require('minimist');
var argv = minimist(process.argv.slice(2));

var config = require('../_config');
var dir = config.dir;
var file = config.file;

var src = path.resolve(__dirname, '../**/*');

var dist = 'docs';


if(argv.build){
  cpx.copy(src, dist, function(err){
    del(path.join(dist, '/bin/**'));
    if(err) console.log(err);
  });
}

var deleteDefaultSuffix = function(fileName){
  return fileName.replace(/\.default\./, '.');
};

if(argv.init){

  var defaults = path.join('docs', dir.all, file.defaults.dist);
  glob.sync(defaults).map(function(val){
    var rename = deleteDefaultSuffix(val);
    mv(val, rename, {
      mkdirp: true,
      clobber: false
    }, function(err){
      if(err) console.error(err);
      else console.log(val + ' => ' + rename);
    });
  });

  var mkdirps = {
    posts: path.join('docs', dir.posts),
    pages: path.join('docs', dir.pages)
  };

  Object.keys(mkdirps).forEach(function(val){
    var dirname = this[val];
    mkdirp(dirname, function(err){
      if(err) console.error(err);
      else console.log('mkdir: ' + dirname);
    });
  }, mkdirps);
}
