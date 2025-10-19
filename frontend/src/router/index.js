import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import BooksPage from '@/views/BooksPage.vue'
import Login from "@/views/Login.vue";

const routes = [
    { path: '/', component: Home },
    { path: '/Books', component: BooksPage },
    { path: '/Login', component: Login },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router