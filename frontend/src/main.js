import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from "vue-router";
import ElementUI from 'element-plus';
import Route from './router';
import 'element-plus/dist/index.css';
<<<<<<< Updated upstream
import axios from 'axios';
axios.defaults.withCredentials = true;
createApp(App).use(Route).use(ElementUI).mount('#app')
=======
// import AboutUs from "./components/AboutUs";
import LOGIN from "./components/LOGIN";
import REGISTER from "./components/REGISTER";
// Define the router
const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/login",
            component: LOGIN,
        },
        {
            path: "/register",
            component: REGISTER,

        },
        // {
        //     path: "/about",
        //     component: AboutUs,
        // }
    ],
});

// Create the Vue application and use the router and ElementUI
const app = createApp(App);
app.use(router);
app.use(ElementUI);
app.mount('#app');
>>>>>>> Stashed changes
