var webpack = require('webpack');
var HtmlWebpackPlugin = require('html-webpack-plugin');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var helpers = require('./helpers');
var path = require('path');
const { AngularCompilerPlugin } = require('@ngtools/webpack');

const VERSION = process.env.Version;
const ENV = process.env.NODE_ENV;
var PROD = (ENV === 'production');

module.exports = {
    entry: {
        'polyfills': './compile/polyfills.ts',
        'vendor': './compile/vendor.ts',
        'vendor-css': './compile/vendor-css.ts',
        'css': './compile/css.js',
        'test-css': './compile/test-css.js',
        'app': './test/main.ts'
    },

    output: {
        path: path.join(__dirname, '../build/client'),
        filename: 'source/[name].js',
        publicPath: '/'
    },

    //debug: PROD ? false : true,
    node: {
        fs: "empty"
    },

    devtool: PROD ? '' : 'source-map',

    resolve: {
        extensions: ['*', '.js', '.ts']
    },

    module: {
        rules: [
            {
                "test": /\.ts$/,
                "loader": "@ngtools/webpack"
            },
            // {
            //   test: /\.ts$/,
            //   use: [
            //     { loader: 'awesome-typescript-loader?useCache=true' },
            //     { loader: 'angular-router-loader' },
            //   ]
            // },
            {
                test: /\.html$/,
                use: 'html-loader'
            },
            {
                test: /\.(png|jpe?g|gif|ico)$/,
                use: [
                    { loader: 'file?name=assets/[name].[hash].[ext]' }
                ]
            },
            {
                test: /\.css$/,
                use: [
                    { loader: "style-loader" },
                    { loader: "css-loader" }
                ]
            },
            {
                test: /\.less$/,
                use: [
                    { loader: "style-loader" },
                    { loader: "css-loader" },
                    { loader: "less-loader" }
                ]
            },
            {
                test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                use: "url-loader?name=fonts/[name].[hash].[ext]&limit=10000&mimetype=application/font-woff"
            },
            {
                test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                use: "file-loader?name=fonts/[name].[hash].[ext]"
            }
        ]
    },

    plugins: [
        new AngularCompilerPlugin({ 
            "mainPath": "lib.ts",
            "platform": 0,
            "hostReplacementPaths": {
                "environments\\environment.ts": "environments\\environment.ts"
            },
            "sourceMap": true,
            "tsConfigPath": "tsconfig.lib.json",
            "strictMetadataEmit": true,
            "skipTemplateCodegen": true,
            "flatModuleOutFile": "pm-control.lib.js",
            "flatModuleId": "pm-control",
            "annotateForClosureCompiler": true
        }),

        PROD && new webpack.optimize.UglifyJsPlugin({
            compress: { warnings: false }
        }),

        new ExtractTextPlugin('[name].css'),

        new webpack.DefinePlugin({
            'process.env': {
                'Version': JSON.stringify(VERSION),
                'ENV': JSON.stringify(ENV),
                'BaseUrl': JSON.stringify(process.env.BaseUrl || '')
            }
        }),

        new webpack.optimize.CommonsChunkPlugin({
            name: ['app', 'vendor', 'vendor-css', 'polyfills']
        }),

        new HtmlWebpackPlugin({
            template: './compile/index-template.html'
        }),

    ].filter(function (plugin) { return plugin !== false; })
};
