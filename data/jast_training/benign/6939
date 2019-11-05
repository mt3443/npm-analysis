var gulp = require('gulp'),
    uglify = require('gulp-uglify'),
    rename = require('gulp-rename'),
    babel = require('gulp-babel');
 
gulp.task('jsmin', function () {
    gulp.src('lib/jquery-pyramid-proportion.js')
    		.pipe(babel({
    			presets: ['env']
    		}))
    		.pipe(rename({suffix: '.min'}))
        .pipe(uglify())
        .pipe(gulp.dest('lib'));
});