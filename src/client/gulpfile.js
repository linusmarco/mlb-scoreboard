var gulp = require('gulp');
var concat = require('gulp-concat');
var cleanCSS = require('gulp-clean-css');
var sourcemaps = require('gulp-sourcemaps');
var SystemBuilder = require('systemjs-builder');

gulp.task('rxjs.bundle', function () {
    var builder = new SystemBuilder('./', {
        paths: { "rxjs/*": "node_modules/rxjs/*.js" },
        map: { "rxjs": "node_modules/rxjs" },
        packages: { "rxjs": { main: 'Rx.js', defaultExtension: "js" } }
    });

    builder.bundle('rxjs', '../../dist/VendorScripts/Rx.min.js', {
        sourceMaps: true,
        minify: true,
        mangle: true
    });
});

gulp.task('buildCSS', function () {
    gulp.src('app/core/content/**/*.css')
        .pipe(concat('app.min.css'))
        .pipe(sourcemaps.init())
        .pipe(cleanCSS())
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('../../dist'));

    return gulp.src('app/**/**/*.css')
       .pipe(sourcemaps.init())
       .pipe(cleanCSS())
       .pipe(sourcemaps.write())
       .pipe(gulp.dest('../../dist'));
});

gulp.task('buildScripts', function () {
    gulp.src(['node_modules/core-js/client/shim.min.js',
             'node_modules/zone.js/dist/zone.js',
             'node_modules/reflect-metadata/Reflect.js',
             'node_modules/systemjs/dist/system.src.js',
             'node_modules/angular-in-memory*/bundles/*.umd.js',
             'node_modules/rxjs*/*.js',
             'node_modules/rxjs*/**/*.js',
             'node_modules/@angula*/material/core/theming/prebuilt/deeppurple-amber.css',
             'node_modules/@angula*/**/bundles/*.umd.js'])
    .pipe(gulp.dest('../../dist/VendorScripts'));

    gulp.src('systemjs.config.js')
        .pipe(gulp.dest('../../dist'));
});

gulp.task('moveHTML', function () {
    return gulp.src(['index.html', 'app/**/*.html', 'app/**/*.json', 'app/**/*.svg'])
      .pipe(gulp.dest('../../dist'));
});

gulp.task('watch', function () {
    gulp.watch('app/content/styles/*.css', ['buildCSS']);
    gulp.watch('app/**/**/*.css', ['buildCSS']);
    gulp.watch('app/index.html', ['moveHTML']);
    gulp.watch('app/**/*.html', ['moveHTML']);
    gulp.watch('app/**/*.svg', ['moveHTML']);
    gulp.watch('app/**/*.json', ['moveHTML']);
});

gulp.task('build', ['rxjs.bundle', 'buildScripts', 'buildCSS', 'moveHTML']);

gulp.task('default', ['build', 'watch']);