import { createRouter, createWebHistory } from 'vue-router'
import Home from "../views/Home.vue"
import BrowseData from "../views/Browse_data.vue"
import API from '../views/API'
import Downloads from '../views/Downloads.vue'
import Help from '../views/Help.vue'
import AMP_card from '../views/AMP_card'
import About from '../views/About'
import Contact from '../views/Contact'


const routes = [
    {
        path: '/',
        redirect: 'home'
    },
    {
        path: "/home",
        name: "Home",
        component: Home,
        meta:{
            title: 'AMPSphere: Home'
        }
    },
    {
        path: "/browse_data",
        name: "Browse_data",
        component: BrowseData,
        meta:{
            title: 'AMPSphere: Browse data'
        }
    },
    {
        path: "/amp",
        name: "AMP",
        component: AMP_card,
        meta:{
            title: 'AMPSphere: AMP'
        },
    },
    {
        path: '/api',
        name: 'API',
        component: API,
        meta:{
            title: 'AMPSphere: API'
        }
    },
    {
        path: '/downloads',
        name: 'Downloads',
        component: Downloads,
        meta:{
            title: 'AMPSphere: Downloads'
        }
    },
    {
        path: '/help',
        name: 'Help',
        component: Help,
        meta:{
            title: 'AMPSphere: Help'
        }
    },
    {
        path: '/contact',
        name: 'Contact',
        component: Contact,
        meta: {
            title: 'AMPSphere: Contact'
        }
    },
    {
        path: '/about',
        name: 'About',
        component: About,
        meta: {
            title: 'AMPSphere: About'
        }
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
})

export default router
