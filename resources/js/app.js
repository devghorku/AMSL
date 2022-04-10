window.Vue = require('vue');
import Vue from 'vue'
Vue.use(require('vue-moment'));
import vuetify from './plugins/vuetify'
import _ from 'lodash'
import API from './services/API'
import GlobalFunc from './services/helper'
import store from './store'
Vue.prototype.$api = API();
Vue.prototype.$globalFunc = GlobalFunc;
import router from './routes'
import axiosRetry from 'axios-retry';

axiosRetry(API(), {retries: 2});


new Vue({
    el: '#app',
    router,
    vuetify,
    store,
    delimiters: ['{', '}'],
    data() {
        return {}
    },
    created() {
    },

    mounted() {

    },
});
