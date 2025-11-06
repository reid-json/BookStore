import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import BooksPage from '@/views/BooksPage.vue'
import Login from "@/views/Login.vue"
import Register from '@/views/Register.vue'

const routes = [
    { path: '/', component: Home, meta: { requiresAuth: true } },
    { path: '/Books', name: 'books', component: BooksPage, meta: { requiresAuth: true } },
    { path: '/Login', name: 'Login', component: Login },
    { path: '/Register', name: 'Register', component: Register },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

// 🔐 Navigation Guard
router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('authToken')

    // Block access to protected routes
    if (to.meta.requiresAuth && !token) {
        return next('/Login')
    }

    // Redirect logged-in users away from Login/Register
    if ((to.path === '/Login' || to.path === '/Register') && token) {
        return next('/Books')
    }

    next()
})

export default router