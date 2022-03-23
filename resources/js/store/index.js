import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import auth from "./modules/auth";
import boot from "./modules/boot";
Vue.use(Vuex);

/* eslint-disable no-new */
const store = new Vuex.Store({
  plugins: [createPersistedState()],

  state: {
        snackbar: {
            message: '',
            type: ''
        },
    },
    mutations: {
        SET_ALERT(state, data) {
            state.snackbar.message = data.msg;
            state.snackbar.type = data.type;
        },
        RESET_ALERT(state) {
            state.snackbar.message = '';
            state.snackbar.type = '';
        }
    },
    getters: {},
    actions: {
        async set_alert({commit}, payload) {
            commit('RESET_ALERT');
            commit('SET_ALERT', payload);
            setTimeout(() => {
                commit('RESET_ALERT')
            }, 3000)
        }
    },
    modules: {
        auth,boot
    },
})

export default store
