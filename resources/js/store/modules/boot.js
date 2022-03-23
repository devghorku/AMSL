import Api from '../../services/API'

const state = {
    expenseCategory: [],
};

const getters = {
    expenseCategoryList: state => state.expenseCategory,
};

const actions = {
    async getBoot({dispatch}) {
        await dispatch('getExpenseCategory');
    },
    async getExpenseCategory({commit}) {
        try {
            const res = await Api().get('expense-category/all/');
            commit('set_expense_category', res.data);
        } catch (e) {
        }
    },

};

const mutations = {
    set_expense_category(state, payload) {
        state.expenseCategory = payload
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};