import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import BooksPage from '@/views/BooksPage.vue'
import Login from "@/views/Login.vue";
import Register from '@/views/Register.vue'

const routes = [
    { path: '/', component: Home },
    { path: '/Books', component: BooksPage },
    { path: '/Login', component: Login },
    { path: '/Register', name: 'Register', component: Register },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router