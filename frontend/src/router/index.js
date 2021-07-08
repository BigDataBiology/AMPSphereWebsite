import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import(/* webpackChunkName: "about" */ '../views/Home.vue')
    },
    {
        path: '/home',
        name: 'Home',
        component: () => import(/* webpackChunkName: "about" */ '../views/Home.vue')
    },
    {
        path: '/amp',
        name: 'AMP',
        component: () => import(/* webpackChunkName: "about" */ '../views/AMP.vue')
    },
    {
        path: '/amp_card',
        name: 'AMP_Card',
        component: () => import(/* webpackChunkName: "about" */ '../views/AMP_Card.vue')
    },
    {
        path: '/family',
        name: 'Family',
        component: () => import(/* webpackChunkName: "about" */ '../views/Family.vue')
    },
    {
        path: '/environment',
        name: 'Environment',
        component: () => import(/* webpackChunkName: "about" */ '../views/Environment.vue')
    },
    {
        path: '/blastp',
        name: 'Blastp',
        component: () => import(/* webpackChunkName: "about" */ '../views/Blastp.vue')
    },
    {
        path: '/hmm',
        name: 'Hmm',
        component: () => import(/* webpackChunkName: "about" */ '../views/Hmm.vue')
    },
    {
        path: '/macrel',
        name: 'Macrel',
        component: () => import(/* webpackChunkName: "about" */ '../views/Macrel.vue')
    },
    {
        path: '/download',
        name: 'Download',
        component: () => import(/* webpackChunkName: "about" */ '../views/Download.vue')
    },
    {
        path: '/contact',
        name: 'Contact',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/Contact.vue')
    }
]

const router = new VueRouter({
    routes
})

export default router
