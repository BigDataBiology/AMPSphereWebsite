import qs from 'qs'
import { createApp } from 'vue'
import VueAxios from 'vue-axios'
import axios from 'axios'
import echarts from 'echarts'
import ElementPlus from 'element-plus'
import './style/theme/index.css';
import locale from 'element-plus/lib/locale/lang/en'
import App from './App.vue'
import router from './router'
import store from './store'


const app = createApp({router, store, render: h => h(App)})
app.use(ElementPlus, {locale})
app.use(VueAxios, axios)

app.config.productionTip = false
axios.defaults.baseURL = 'http://127.0.0.1:8000';
app.prototype.$baseURL = axios.defaults.baseURL;
app.prototype.$echarts = echarts
app.prototype.$qs = qs

app.mount('#app')