import store from '../store'

export default {
    getOrder(sortBy, sortDesc) {
        if (sortDesc[0] === undefined) {
            return null
        } else if (sortDesc[0]) {
            return sortBy ? sortBy.toString() : null
        } else {
            return sortBy ? '-' + sortBy.toString() : null
        }
    },
    errorAlert(response, msg = '') {
        if (response && response.status === 403) {
            if (response.data.detail) {
                store.dispatch('set_alert', {msg: response.data.detail, type: 'error'})
            } else {
                store.dispatch('set_alert', {msg: 'Access Denied', type: 'error'})
            }

        } else if (response && response.data && response.data.name) {
            store.dispatch('set_alert', {msg: response.data.name[0], type: 'error'})
        } else if (msg) {
            store.dispatch('set_alert', {msg: msg, type: 'error'})
        } else {
            store.dispatch('set_alert', {msg: 'action error', type: 'error'})
        }
    }
}