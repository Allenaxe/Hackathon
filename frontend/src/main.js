import { createApp } from 'vue';
import App from './App.vue';
import ElementUI from 'element-plus';
import Route from './router';
import 'element-plus/dist/index.css';
import axios from 'axios';
axios.defaults.withCredentials = true;
createApp(App).use(Route).use(ElementUI).mount('#app')
