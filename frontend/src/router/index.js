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
  },
  {
    path: '/achievement',
    name: 'achievement',
    component: () => import('@/components/NewApi')
  },
  {
    path: '/path',
    name: 'path',
    component: () => import('@/components/LearnPath')
  },
  {
    path: '/course',
    name: 'course',
    component: () => import('@/components/LearnCourse')
  },
  {
    path: '/history',
    name: 'history',
    component: () => import('@/components/LearnedRecord')
  }
]

const router = createRouter({
  history: createWebHashHistory('/'),
  routes
})

export default router