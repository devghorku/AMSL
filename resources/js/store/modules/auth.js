import Api from '../../services/API'
import axios from 'axios'
import router from '../../routes'

const state = {
    token: localStorage.getItem("usrToken") || "",
    refreshToken: localStorage.getItem('refresh_token') || null,
    user: {},
};

const getters = {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.user,
};

const actions = {
    login({commit, dispatch}, user) {
        return new Promise((resolve, reject) => {
            Api().post('token/', user)
                .then(resp => {
                    const token = resp.data.access;
                    const refresh_token = resp.data.refresh;
                    localStorage.setItem('usrToken', token);
                    localStorage.setItem('refresh_token', refresh_token);
                    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
                    commit('auth_success', token, refresh_token);
                    dispatch('set_alert', {msg: 'login success', type: 'success'});
                    dispatch('getCurrentUser');
                    router.push({name: 'home'});
                    resolve(resp)

                })
                .catch(err => {
                    dispatch('set_alert', {msg: err.response.data.detail, type: 'error'})
                    localStorage.removeItem('usrToken');
                    localStorage.removeItem('refresh_token');
                    reject(err)
                })
        })
    },
    getCurrentUser({commit}) {
        return new Promise((resolve, reject) => {
            Api().get('get-user/').then(response => {
                commit('set_user', response.data);
                resolve(response.data)
            })
                .catch(err => {
                    commit('set_user', {});
                    reject(err)
                })
        })
    },
    logout({commit}) {
        return new Promise((resolve) => {
            commit('logout');
            localStorage.removeItem('usrToken');
            localStorage.removeItem('refresh_token');
            delete axios.defaults.headers.common['Authorization'];
            if (router.currentRoute.name !== 'login') {
                router.push('/login')
            }

            resolve()
        })
    },
    refreshToken({commit, state}) {
        return new Promise((resolve, reject) => {
            Api().post('token/refresh/', {
                refresh: state.refreshToken
            }).then(resp => {
                const token = resp.data.access;
                localStorage.setItem('usrToken', token);
                axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
                commit('auth_success', token, state.refreshToken);
                resolve(resp.data.access)
            })
                .catch(err => {
                    router.push({name: 'login'});
                    reject(err)
                })
        })
    },
};

const mutations = {
    auth_success(state, token, refresh_token) {
        state.token = token;
        state.refresh_token = refresh_token;
    },
    set_user(state, payload) {
        state.user = payload;
    },
    logout(state) {
        state.token = '';
        state.refresh_token = '';
        state.user = {};
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};