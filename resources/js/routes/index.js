import DashboardLayout from '../layout/dashboardLayout'
import AuthLayout from '../layout/authLayout'
import Vue from 'vue'
import VueRouter from 'vue-router'
import store from "../store";
import Home from '../views/dashboard'
import ExpenseCategory from '../views/expenseCategory'
import IncomeCategory from '../views/incomeCategory'
import Expense from '../views/expense'
import Income from '../views/income'
import Login from '../views/login'
import Employee from "../views/employee"
import EmployeeCategory from "../views/employeeCategory"
import Payroll from "../views/payroll"
import Invoice from "../views/invoice/create"
import InvoiceView from "../views/invoice/view"
import InvoiceList from "../views/invoice/list"


// import globalFunc from '../services/helper'

Vue.use(VueRouter);
const ifNotAuthenticated = (to, from, next) => {
    if (!store.getters.isLoggedIn) {
        next();
        return;
    }
    next("/");
};

const ifAuthenticated = (to, from, next) => {

    if (store.getters.isLoggedIn) {
        if (!store.getters.currentUser.username) {
            store.dispatch('getCurrentUser')
        }
        next();
        return;
    }
    next("/login");
};
const router = new VueRouter({
    mode: 'history',
    scrollBehavior(to, from, savedPosition) {
        return {x: 0, y: 0}
    },
    routes: [
        {
            path: '/',
            redirect: 'home',
            component: DashboardLayout,
            beforeEnter: ifAuthenticated,
            children: [

                {
                    path: '',
                    name: 'home',
                    component: Home,
                },
                {
                    path: 'expense',
                    name: 'expense',
                    component: Expense,
                },
               {
                    path: 'expense-category',
                    name: 'expenseCategory',
                    component: ExpenseCategory,
                },
                {
                    path: 'income',
                    name: 'income',
                    component: Income,
                },
               {
                    path: 'income-category',
                    name: 'incomeCategory',
                    component: IncomeCategory,
                },
                {
                    path: 'employee',
                    name: 'employee',
                    component: Employee,
                },
               {
                    path: 'employee-category',
                    name: 'employeeCategory',
                    component: EmployeeCategory,
                },
                {
                    path: 'payroll',
                    name: 'payroll',
                    component: Payroll,
                },
                {
                    path: 'invoice',
                    name: 'invoice',
                    component: Invoice,
                },
                {
                    path: 'invoice-list',
                    name: 'invoiceItems',
                    component: InvoiceList,
                },
                {
                    path: 'invoice-view',
                    name: 'view',
                    component: InvoiceView,
                },
            ]
        },
        {
            path: '/',
            redirect: 'login',
            component: AuthLayout,
            beforeEnter: ifNotAuthenticated,
            children: [
                {
                    path: '/login',
                    name: 'login',
                    component: Login,
                },
            ]
        },
        {
            path: '/403',
            name: 'forbidden',
            component: require('../views/errors/403').default
        },
        {
            path: '/*',
            name: 'not-found',
            component: require('../views/errors/404').default
        }
    ]
});

// router.beforeEach((to, from, next) => {
//     if (to.meta.permissions) {
//         if (store.getters.currentUser.username) {
//             if (globalFunc.isPermit(to.meta.permissions)) {
//                 next()
//             } else {
//                 next('/403')
//             }
//         } else {
//             store.dispatch('getCurrentUser').then(() => {
//                 if (globalFunc.isPermit(to.meta.permissions)) {
//                     next()
//                 } else {
//                     next('/403')
//                 }
//             })
//         }
//         next()
//     } else {
//         next()
//     }
// });
export default router