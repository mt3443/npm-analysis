/////////////////////////////////////////////////////////////////////////////////////

// requirement

/////////////////////////////////////////////////////////////////////////////////////

var gulp = require('gulp');
var $ = require('gulp-load-plugins')();
var del = require('del');
var path = require('path');
var minimist = require('minimist');
var mv = require('mv');
var pngquant = require('imagemin-pngquant');
var mozjpeg = require('imagemin-mozjpeg');

/////////////////////////////////////////////////////////////////////////////////////

// config

/////////////////////////////////////////////////////////////////////////////////////

var config = require('./_config');
var dir = config.dir;
var file = config.file;
var imgmin = config.imgmin;

var options = {
  imagemin: [
    pngquant(imgmin.pngquant),
    mozjpeg(imgmin.mozjpeg),
    $.imagemin.svgo(imgmin.svgo),
    $.imagemin.gifsicle(imgmin.gifsicle)
  ]
};

var argv = minimist(process.argv.slice(2));

/////////////////////////////////////////////////////////////////////////////////////

// tasks

/////////////////////////////////////////////////////////////////////////////////////

// imagemin
gulp.task('img', function(){
  var src = path.join(dir.rel.src, dir.img, dir.all, file.img);
  var dist = path.join(dir.rel.dist, dir.assets, dir.img);

  return gulp.src(src)
    .pipe($.changed(dist))
    .pipe($.imagemin(options.imagemin))
    .pipe($.rename(function(file){
      file.extname = file.extname.toLowerCase();
    }))
    .pipe(gulp.dest(dist));
});

// clean assets file
gulp.task('clean', function(){

  var src = {
    css: path.join(dir.assets, dir.css, dir.all, file.all),
    js: path.join(dir.assets, dir.js, dir.all, file.all),
    img: path.join(dir.assets, dir.img, dir.all, file.all),
    assets: path.join(dir.assets, dir.all, file.all),
    site: path.join(dir.site, dir.all, file.all),
    defaults: path.join(dir.all, file.defaults.dist)
  };

  var deleteFiles = [
    src.css,
    src.js
  ];

  if(argv.images || argv.img){
    deleteFiles = [src.img];

  } else {

    if(argv.assets) deleteFiles = [src.assets];
    if(argv.site) deleteFiles.push(src.site);
    if(argv.defaults) deleteFiles.push(src.defaults);
    if(argv.all){
      deleteFiles = [
        src.assets,
        src.site,
        src.defaults
      ];
    }
  }

  console.log('Deleted files: ' + deleteFiles);
  del(deleteFiles);
});

gulp.task('create', function(){

  if(argv.defaults){
    return gulp.src(file.defaults.src)
      .pipe($.rename({suffix: '.default'}))
      .pipe(gulp.dest('./'));
  }
});

gulp.task('archive', function(){

  var src = argv.file;

  if(src){
    var dist = path.join(dir.archives, src);

    return mv(src, dist, {mkdirp: true},function(err){
      if(err) console.error(err);
      else {
        console.log('\n' + '> archive success.');
        console.log('> mv ' + src + ' => ' + dist);
      }
    });

  } else {

    var dirname;

    if(argv.pages){
      src = path.join(dir.pages, dir.all, file.pages);
      dirname = dir.pages;

      gulp.src(src)
        .pipe($.rename({dirname: dirname}))
        .pipe(gulp.dest(dir.archives));
    }

    if(argv.posts){
      src = path.join(dir.posts, dir.all, file.pages);
      dirname = dir.posts;

      gulp.src(src)
        .pipe($.rename({dirname: dirname}))
        .pipe(gulp.dest(dir.archives));
    }

    console.log('\n' + '> archive success.');
    console.log('> mv ' + src + ' => ' + path.join(dir.archives, src));
  }
});

gulp.task('watch', function(){

  var img = path.join(dir.src, dir.img, dir.all, file.img);

  $.watch(img, function(){
    gulp.start(['img']);
  });
});
