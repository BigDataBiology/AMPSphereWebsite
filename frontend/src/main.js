import { createApp, h } from 'vue'
import App from './App.vue'
import ElementPLus from 'element-plus'
import './styles/theme/index.css'
import './styles/main.css';
import "quasar/dist/quasar.sass"
import locale from 'element-plus/lib/locale/lang/en'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import imageZoom from 'vue-image-zoomer'
import { Download, More } from '@element-plus/icons'
import JsonViewer from "vue3-json-viewer"
import BootstrapIcon from '@dvuckovic/vue3-bootstrap-icons'
import { Quasar, Notify } from 'quasar'
import quasarUserOptions from './quasar-user-options'
import VueGtag from "vue-gtag"


router.beforeEach((to, from, next) => {
    if (to.meta.title) {
        document.title = to.meta.title
    }
    next()
})

const app = createApp(
    {
        render: () => h(App),
        imageZoom
    }
)


app.use(router)
app.use(VueGtag, {
    config: {
        id: "G-WXMZ531P7V",
    },
}, router)
app.use(Quasar, {plugins: {Notify}, config: {notify: { /* look at QuasarConfOptions from the API card */ }}})
app.use(Quasar, quasarUserOptions)
app.use(ElementPLus, {locale})
app.use(VueAxios, axios)
app.use(JsonViewer)
//app.use(VueSidebarMenu)
const ImageZoom = require('vue-image-zoomer').default
app.component('image-zoom', ImageZoom)
app.component(More.name, More)
app.component(Download.name, Download)
app.component('BootstrapIcon', BootstrapIcon);
axios.defaults.baseURL = 'http://18.140.248.253:443/v1'
app.mount('#app')