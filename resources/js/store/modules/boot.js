import Api from '../../services/API'

const state = {
    expenseCategory: [],
    incomeCategory: [],
    employeeCategory: [],
    employees: [],
};

const getters = {
    expenseCategoryList: state => state.expenseCategory,
    incomeCategoryList: state => state.incomeCategory,
    employeeCategoryList: state => state.employeeCategory,
    employeeList: state => state.employees,
};

const actions = {
    async getBoot({dispatch}) {
        await dispatch('getExpenseCategory');
        await dispatch('getIncomeCategory');
        await dispatch('getEmployeeCategory');
        await dispatch('getEmployees');
    },
    async getExpenseCategory({commit}) {
        try {
            const res = await Api().get('expense-category/all/');
            commit('set_expense_category', res.data);
        } catch (e) {
        }
    },
    async getIncomeCategory({commit}) {
        try {
            const res = await Api().get('income-category/all/');
            commit('set_income_category', res.data);
        } catch (e) {
        }
    },
    async getEmployeeCategory({commit}) {
        try {
            const res = await Api().get('employee-category/all/');
            commit('set_employee_category', res.data);
        } catch (e) {
        }
    },
    async getEmployees({commit}) {
        try {
            const res = await Api().get('employee/all/');
            commit('set_employees', res.data);
        } catch (e) {
        }
    },

};

const mutations = {
    set_expense_category(state, payload) {
        state.expenseCategory = payload
    },
    set_income_category(state, payload) {
        state.incomeCategory = payload
    },
    set_employee_category(state, payload) {
        state.employeeCategory = payload
    },
    set_employees(state, payload) {
        state.employees = payload
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};