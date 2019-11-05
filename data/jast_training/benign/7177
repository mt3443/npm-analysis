const path = require('path');
const CopyWebpackPlugin = require('copy-webpack-plugin');

const CLIENT_SRC_DIR = path.resolve(__dirname, 'src');
const CLIENT_DIST_DIR = path.resolve(__dirname, 'dist');

const moduleTemplate = {
  loaders: [
    {
      test: /\.jsx?$/,
      exclude: [/node_modules/, 'src/env/env.json'],
      loader: 'babel-loader',
      query: {
        "presets": [
          ["env", {
            "targets": {
              "browsers": ["last 2 versions"]
            }
          }],
          'react',
          'stage-3',
        ],
      },
    },
    {
      test: /\.css$/,
      loader: 'style-loader!css-loader',
    },
    {
      test: /\.scss$/,
      loaders: [{
        loader: 'style-loader',
      }, {
        loader: 'css-loader',
      }, {
        loader: 'sass-loader',
        options: {
          outputStyle: 'compressed',
          includePaths: ['./node_modules'],
        },
      }],
    },
    {
      test: /\.less$/,
      loader: 'style-loader!css-loader!sass-loader',
    },
  ],
};

const config = [
  {
    entry: {
      'app': [CLIENT_SRC_DIR + '/index.js'],
    },
    output: {
      path: CLIENT_DIST_DIR + '/javascripts',
      filename: '[name].bundle.js',
    },
    devtool: 'source-map',
    devServer: {
      contentBase: 'dist/'
    },
    module: moduleTemplate,
    plugins: [
      new CopyWebpackPlugin([
        {
          from: CLIENT_SRC_DIR + '/index.html',
          to: CLIENT_DIST_DIR + '/index.html',
        },
        {
          from: CLIENT_SRC_DIR + '/favicon.ico',
          to: CLIENT_DIST_DIR + '/favicon.ico',
        },
        {
          from: CLIENT_SRC_DIR + '/env/env.json',
          to: CLIENT_DIST_DIR + '/env/env.json',
        },
      ]),
    ],
  },
];

module.exports = config;
