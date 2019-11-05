/////////////////////////////////////////////////////////////////////////////////////

// status

/////////////////////////////////////////////////////////////////////////////////////

var ENV = require('./_config/modules/status')
var PROD = ENV === 'production'

console.log('\n' + 'status ----\n\n' + ENV + '\n\n----')

/////////////////////////////////////////////////////////////////////////////////////

// requirement

/////////////////////////////////////////////////////////////////////////////////////

// common
var ExtractTextPlugin = require('extract-text-webpack-plugin')
var webpack = require('webpack')
var path = require('path')
// var BrowserSyncPlugin = require('browser-sync-webpack-plugin')

/////////////////////////////////////////////////////////////////////////////////////

// config

/////////////////////////////////////////////////////////////////////////////////////

var config = require('./_config')
var projectRoot = config.projectRoot
var options = config.webpack
var dir = config.dir
var entry = require('./_config/modules/entry') // entry file's object

/////////////////////////////////////////////////////////////////////////////////////

// plugins

/////////////////////////////////////////////////////////////////////////////////////

var plugins = PROD ? [

  new webpack.optimize.AggressiveMergingPlugin(),
  new webpack.optimize.OccurrenceOrderPlugin()

] : [

  new webpack.NoEmitOnErrorsPlugin()

]

var commonPlugins = [
  // new BrowserSyncPlugin(options.BrowserSyncPlugin),
  new ExtractTextPlugin('[name]'),
  new webpack.LoaderOptionsPlugin(options.LoaderOptionsPlugin)
  // new webpack.LoaderOptionsPlugin(options.pugLoader)

]
plugins = plugins.concat(commonPlugins)

/////////////////////////////////////////////////////////////////////////////////////

// output a list like 'entryFile => bundleFile' to the console

/////////////////////////////////////////////////////////////////////////////////////

var bundleLog = require('./_config/modules/bundle-log')
bundleLog()

/////////////////////////////////////////////////////////////////////////////////////

// webpack.config

/////////////////////////////////////////////////////////////////////////////////////

module.exports = {

  resolve: {
    modules: [
      'node_modules'
    ],
    alias: {

    }
  },

  cache: !PROD,
  entry: entry,

  output: {
    path: dir.abs.dist,
    filename: '[name]'
  },

  plugins: plugins,

  externals: {
    jquery: 'jQuery'
  },

  module: {
    rules: [
      {
        test: /\.scss$/,
        use: ExtractTextPlugin.extract([
          {
            loader: 'css-loader',
            options: options.cssLoader
          },
          {
            loader: 'pleeease-loader'
          },
          {
            loader: 'resolve-url-loader'
          },
          {
            loader: 'sass-loader',
            options: options.sassLoader
          }
        ])
      },
      {
        test: /\.css$/,
        use: [
          {
            loader: 'css-loader'
          }
        ]
      },
      {
        test: /\.(jpe?g|png|gif|svg)$/,
        use: [
          {
            loader: 'url-loader',
            options: options.urlLoader
          },
          {
            loader: 'img-loader',
            options: options.imgLoader
          }
        ]
      },
      {
        test: /\.(ttf|otf|eot|woff(2)?)(\?[a-z0-9]+)?$/,
        use: {
          loader: 'url-loader',
          options: options.urlLoader
        }
      }
    ]
  }
}
