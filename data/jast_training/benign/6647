/////////////////////////////////////////////////////////////////////////////////////

// status

/////////////////////////////////////////////////////////////////////////////////////

var ENV = require('./modules/status')
var PROD = ENV === 'production'
var path = require('path')
var projectRoot = path.resolve(__dirname, '../') // project root dir

var dir = {
  root:     projectRoot,
  src:      '_src',
  dist:     'dist',
  sass:     'scss',
  css:      'css',
  js:       'js',
  pug:      'pug',
  html:     '',
  img:      'images',
  assets:   '',
  others:   'others',
  archives: '_archives',
  cache:    'cache',
  all:      '**'
}

var rel = {
  src: dir.src,
  dist: dir.dist,
  archives: dir.archives
}

dir.rel = rel

var abs = {}

Object.keys(rel).forEach(function (key) {
  abs[key] = path.join(projectRoot, this[key])
}, rel)

dir.abs = abs

var ext = {
  sass:   '.scss',
  css:    '.css',
  js:     '.js',
  php:    '.php',
  jpg:    '.jpg',
  allSrc: '.*'
}

var file = {
  all: '*'
}

Object.keys(ext).forEach(function (key) {
  file[key] = '!(_)*' + this[key]
}, ext)

module.exports = {

  projectRoot: projectRoot,
  dir:  dir,
  ext:  ext,
  file:  file,

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
        dist: path.join(dir.assets, dir.js)
      },
      name: path.join(dir.all, file.js)
    }
  },

  webpack: {

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
    }
  },

  browserSync: {
    ui: {
      port: 3000
    },
    // files: path.join(dir.dist, dir.all, file.all),
    server: dir.dist,
    // proxy: {
    //   target: 'http://lovemac.lo'
    // },
    files: [
      path.join(projectRoot, dir.dist, dir.all, file.all)
    ],
    open: false,
    reloadDebounce: 2000,
    reloadThrottle: 2000
  }
}
