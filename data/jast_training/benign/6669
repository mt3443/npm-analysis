const path 				 = require('path');
const gulp 				 = require('gulp');
const gutil 			 = require("gulp-util");
const gulpts 			 = require('gulp-typescript');
const typescript 		 = require('typescript');
const webpack 			 = require('webpack');
const webpackStream 	 = require('webpack-stream');
const del 				 = require('del');
const gulpNgConfig 		 = require('gulp-ng-config');
const sync 				 = require('run-sequence');
const browserSync 		 = require('browser-sync');
const package 			 = require('./package.json');

var source 				= 'source';
var test 				= 'test';
var vendor 				= 'vendor';
var outputBuild 		= 'build/client';
var outputDist 			= 'dist';
var outputPublish		= 'dist/*';
var outputFolder		= 'build/*';

var reloadClient = function () {
	return browserSync.reload()
};

// map of all our paths
var paths = {
	sourcejs: [ path.join(source, '**/*.js') ],
	testjs: [ path.join(test, '**/*.js') ],
	sourcets: [ path.join(source, '**/*.ts') ],
	testts: [ path.join(test, '**/*.ts') ],
	sourcecss: [ path.join(source, '**/*.css') ],
	testcss: [ path.join(test, '**/*.css') ],
	img: path.join(source, 'img/**/*.*'),
	sourcehtml: path.join(source, '**/*.html'),
	testhtml: path.join(test, '**/*.html'),
	json: path.join(source, '**/*.json'),
	vendor: path.join(vendor, '**/*.*'),
	client: source,
	outputBuild: outputBuild,
	outputDist: outputDist,
	outputFolder: outputFolder,
	outputPublish: outputPublish,
};

gulp.task('clean', () => {
  return del([paths.outputFolder], {dot: true, force: true}, () => {
  });  
});

gulp.task('vendor-files', () => {
  return gulp.src([paths.vendor])  
	.pipe(gulp.dest(paths.outputBuild));
});

gulp.task('dist-source-files', () => {
  return gulp.src([paths.json])  
	.pipe(gulp.dest(paths.outputDist));
});

gulp.task('files', () => {
  return gulp.src([paths.sourcehtml, paths.testhtml, paths.json])  
	.pipe(gulp.dest(paths.outputBuild));
});

gulp.task('img', () => {
  return gulp.src(paths.img)
    .pipe(gulp.dest(paths.outputBuild + "/img"));
});

gulp.task('client-files', done => {
	sync(['files', 'vendor-files', 'img'], done);
});

gulp.task('webpack-source', () => {
	var config = require('./compile/webpack.source.config');

	return gulp.src(paths.client)
		.pipe(webpackStream(config, webpack))
		.pipe(gulp.dest(paths.outputBuild));
});

gulp.task('webpack-lib', () => {
	var config = require('./compile/webpack.lib.config');

	return gulp.src(paths.client)
		.pipe(webpackStream(config, webpack))
		.pipe(gulp.dest(paths.outputBuild));
});

gulp.task('serve-client', () => {
	browserSync.init({
		port: process.env.PORT || 3100,
		open: true,
		ghostMode: false,
		server: {
			baseDir: outputBuild,
			index: 'index.html'
		},
		logPrefix: "PM Controls"		
	});
});

gulp.task('watch-html-img', () => {
	var allPaths = [].concat(		
		[paths.img],
		[paths.testhtml]
	);
	
	gulp.watch(allPaths, ['client-files', 'label', reloadClient]);
});

gulp.task('watch-ts-js', () => {
	var allPaths = [].concat(
		[paths.sourcehtml],
		[paths.sourcecss],
		[paths.testcss],
		[paths.sourcejs],
		[paths.testjs],
		[paths.sourcets],
		[paths.testts]
	);
		
	gulp.watch(allPaths, ['webpack-source', 'label', reloadClient]);
});

gulp.task('typings', done => {
	var project = gulpts.createProject('tsconfig.json', {
		typescript: typescript,
		declaration: true,
	});
	return gulp.src(paths.sourcets)
		.pipe(project())
		.pipe(gulp.dest('./lib'));
});
gulp.task('client', done => {
	sync('client-files', 'webpack-source', 'typings', 'watch-html-img', 'watch-ts-js', 'serve-client', 'label', done);
});

gulp.task('output', () => {
	gutil.log('\n\n' 
	+ gutil.colors.bgRed('   PM-Controls   ') + '\n' 
	+ gutil.colors.yellow('NODE_ENV     ') + gutil.colors.bgYellow(process.env.NODE_ENV) + '\n' 
	+ gutil.colors.yellow('outputBuild  ') + gutil.colors.bgYellow(paths.outputBuild) + '\n'
	+ gutil.colors.yellow('outputFolder ') + gutil.colors.bgYellow(paths.outputFolder) + '\n');
});

gulp.task('label', () => {
	gutil.log('\n\n' 
	+ gutil.colors.bgRed('   PM-Controls   ') + '\n');
});

gulp.task('deploy', done => {
	process.env.NODE_ENV = 'development';
	process.env.Version = package.version;
	sync('output', 'client-files', 'webpack-source', done);
});

gulp.task('default', done => {
	process.env.NODE_ENV = 'development';
	process.env.Version = package.version;
	sync('output', 'clean', 'client', done);
});

gulp.task('lib', done => {
	process.env.NODE_ENV = 'production';
	process.env.Version = package.version;
	sync('output', 'clean', 'client-files', 'webpack-lib', 'typings', 'label', done);
});