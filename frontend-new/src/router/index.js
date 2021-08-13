import VueRouter from 'vue-router'


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
        path: '/amps',
        name: 'AMPs',
        component: () => import(/* webpackChunkName: "about" */ '../views/AMP_list.vue')
    },
    {
        path: '/amp',
        name: 'AMP',
        component: () => import(/* webpackChunkName: "about" */ '../views/AMP_card.vue')
    },
    {
        path: '/family',
        name: 'Family',
        component: () => import(/* webpackChunkName: "about" */ '../views/Family_card.vue')
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
