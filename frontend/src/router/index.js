import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';
import BooksPage from '@/views/BooksPage.vue';
import Login from "@/views/Login.vue";
import Register from '@/views/Register.vue';
import Cart from "@/components/Cart.vue";
import Payment from "@/views/Payment.vue";
import Confirmation from "@/views/Confirmation.vue";
import Orders from "@/views/Orders.vue";

const routes = [
    { path: '/', component: Home, meta: { requiresAuth: true } },
    { path: '/Books', name: 'books', component: BooksPage, meta: { requiresAuth: true } },
    { path: '/Login', name: 'Login', component: Login },
    { path: '/Register', name: 'Register', component: Register },
    { path: '/cart', name: 'Cart', component: Cart, meta: { requiresAuth: true } },
    { path: '/payment', name: 'Payment', component: Payment, meta: { requiresAuth: true } },
    { path: '/confirmation', name: 'Confirmation', component: Confirmation, meta: { requiresAuth: true } },
    { path: '/orders', name: 'Orders', component: Orders, meta: { requiresAuth: true } },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});


router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('authToken');


    if (to.meta.requiresAuth && !token) {
        return next('/Login');
    }


    if ((to.path === '/Login' || to.path === '/Register') && token) {
        return next('/Books');
    }

    next();
});

export default router;