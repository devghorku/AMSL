const mix = require('laravel-mix')
require('vuetifyjs-mix-extension')
/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel application. By default, we are compiling the Sass
 | file for the application as well as bundling up all the JS files.
 |
 */
mix.setPublicPath('static/')
mix.setResourceRoot('../')

mix.js('resources/js/app.js', 'static/js').vuetify()
   .sass('resources/sass/app.scss', 'static/css')
    .browserSync({proxy:'127.0.0.1:8000'})
