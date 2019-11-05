/////////////////////////////////////////////////////////////////////////////////////

// status

/////////////////////////////////////////////////////////////////////////////////////

var ENV = require('./modules/status');
var PROD = ENV === "production";
var path = require('path');
var projectRoot = path.resolve(__dirname, '../'); // project root dir
// var gulpImagemin = require('gulp-imagemin');
// var pngquant = require('imagemin-pngquant');
// var mozjpeg = require('imagemin-mozjpeg');

var dir = {
  root:     projectRoot,
  src:      '_src',
  dist:     '',
  sass:     'scss',
  css:      'css',
  js:       'js',
  pug:      'pug',
  html:     '',
  img:      'images',
  site:     '_site',
  pages:     'pages',
  posts:    '_posts',
  assets:   'assets',
  others:   'others',
  archives: '_archives',
  all:      '**'
};

var rel = {
  src: dir.src,
  dist: dir.dist,
  archives: dir.archives,
};

dir.rel = rel;

var abs = {};

Object.keys(rel).forEach(function(key){
  abs[key] = path.join(projectRoot, this[key]);
}, rel);

dir.abs = abs;

var ext = {
  sass:   '.scss',
  css:    '.css',
  js:     '.js',
  pug:    '.pug',
  php:    '.php',
  html:   '.html',
  jpg:    '.jpg',
  png:    '.png',
  gif:    '.gif',
  svg:    '.svg',
  img:    '.{jpg,png,gif,svg}',
  pdf:    '.pdf',
  gzip:   '.gz',
  pages:   '.{html,md,markdown}',
  allSrc: '.*'
};

var file = {
  all: '*',
};

Object.keys(ext).forEach(function(key){
  file[key] = '!(_)*' + this[key];
}, ext);

var jekyll = [
  path.join(dir.pages, dir.all, file.pages),
  path.join(dir.posts, dir.all, file.pages),
  path.join(dir.assets, dir.all, file.allSrc),
  '_config.yml'
];

file.jekyll = jekyll;

var defaults = {
  src: [
    '**/style.scss',
    '**/scripts.js',
    '_config.yml',
    '**/front-page-overview.html',
    '**/sidebar.html',
    '**/my-theme/_config.scss',
    '**/my-theme/_project.scss'
    ],

  dist: '**/*.default.*'
};

file.defaults = defaults;


var imgmin = {

  pngquant: {
    speed: 1
  },

  mozjpeg: {
    quality:85,
    progressive: false,
    arithmetic: false
  },

  svgo: {
    plugins: [
      {
        removeTitle: true
      },
      {
        convettPathData: false
      }
    ]
  },

  gifsicle: {
    interlaced: false
  }
};

module.exports = {

  appName: 'jfgp',
  projectRoot: projectRoot,
  dir:  dir,
  ext:  ext,
  file:  file,
  imgmin: imgmin,

  entryFiles: {

    sass: {
      dir: {
        src: path.join(dir.sass),
        dist: path.join(dir.assets, dir.css)
      },
      name: path.join(dir.all, file.sass),
      ext: ext.css
    },

    js: {
      dir: {
        src: path.join(dir.js),
        dist: path.join(dir.assets,dir.js)
      },
      name: path.join(dir.all, file.js)
    }
  },

  webpack: {

    CompressionPlugin: {
      asset: '[path].gz[query]',
      algorithm: "gzip",
      test: /\.(js|css)$/,
      threshold: 10240,
      minRatio: 0.8
    },

    BrowserSyncPlugin: {
      host: 'localhost',
      port: 3000,
      server: {
        baseDir: dir.site
      },
      files: [
        path.join(projectRoot, dir.site, dir.all, file.all)
      ],
      open: false
    },

    ProvidePlugin: {
      jQuery: "jquery",
      $: "jquery"
    },

    LoaderOptionsPlugin: {
      test: /\.scss$/,
      options: {
        pleeease: {
          autoprefixer: {
            browsers: ['last 2 versions']
          },
          minifier: PROD,
          mqpacker: true,
          sass: false,
          sourcemap: !PROD,
          pseudoElements: false,
          rebaseUrls: false //must
        }
      }
    },

    cssLoader: {
      url: true
    },

    sassLoader: {
      outputStyle: 'expanded',
      sourceMap: true
    },

    urlLoader: {
      limit: 10000,
      name: path.join('/', dir.assets, dir.img, '[name].[ext]')
    },

    imgLoader: {
      enabled: PROD,
      gifsicle: imgmin.gifsicle,
      mozjpeg: imgmin.mozjpeg,
      pngquant: imgmin.pngquant,
      svgo: imgmin.svgo,
      optipng: false
    }
  },

  browserSync: {
    ui: {
      port: 3000,
    },
    files: path.join(dir.site, 'index.html'),
    server: dir.site
  }
};
