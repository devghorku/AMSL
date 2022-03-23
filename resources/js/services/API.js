import axios from 'axios'
import store from '../store'

export default () => {
    axios.defaults.baseURL = 'http://localhost:8000/api/';
    const token = localStorage.getItem('usrToken');
    if (token) {
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
    }
    axios.interceptors.response.use(null, (error)=>{
            const originalRequest = error.config;
            if (error.response.status === 401 && !originalRequest._retry) {
                originalRequest._retry = true;
                 store.dispatch('logout')
            }
            return Promise.reject(error);
        }
    );
    return axios
}