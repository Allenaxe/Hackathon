import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'login',
    component: () => import('@/components/LoginApi')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('@/components/RegisterApi')
  },
  {
    path: '/panel',
    name: 'panel',
    component: () => import('@/components/PanelApi')
  }
]

const router = createRouter({
  history: createWebHashHistory('/login'),
  routes
})

export default router