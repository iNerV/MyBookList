var gulp = require('gulp');

var concat = require('gulp-concat');
var less = require('gulp-less');
var path = require('path');
var csso = require('gulp-csso');
var coffee = require('gulp-coffee');
var rename = require('gulp-rename');


gulp.task('coffee', function() {
  gulp.src('./static/src/coffee/*.coffee')
    .pipe(coffee({bare: true}).on('error', gutil.log))
    .pipe(gulp.dest('./static/js/'));
});


gulp.task('scripts', function() {
  return gulp.src('./static/src/js/*.js')
    .pipe(concat('main.js'))
    .pipe(gulp.dest('./static/'));
});

gulp.task('less', function () {
  gulp.src('./static/src/less/common.less')
    .pipe(less())
    .pipe(concat('main.css'))
    .pipe(gulp.dest('./static/'))
    .pipe(csso())
    .pipe(rename({suffix: ".min"}))
    .pipe(gulp.dest('./static/'));
});

gulp.task('colors', function () {
  gulp.src('./static/src/less/_colors.less')
    .pipe(less())
    .pipe(concat('colors.css'))
    .pipe(gulp.dest('./static/'))
    .pipe(csso())
    .pipe(rename({suffix: ".min"}))
    .pipe(gulp.dest('./static/'));
});



gulp.task('bootstrap', function () {
  gulp.src('./static/src/bootstrap/less/bootstrap.less')
    .pipe(less())
    .pipe(concat('bootstrap.css'))
    .pipe(gulp.dest('./static/css/'))
    .pipe(csso())
    .pipe(rename({suffix: ".min"}))
    .pipe(gulp.dest('./static/css/'));
});

gulp.task('main', function () {
  gulp.src('./static/src/application.less')
    .pipe(less())
    .pipe(concat('mbl.css'))
    .pipe(gulp.dest('./static/css/'))
    .pipe(csso())
    .pipe(rename({suffix: ".min"}))
    .pipe(gulp.dest('./static/css/'));
});