import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import './style.css'
import App from './App.vue'
import Home from './components/Home.vue'
import Features from './components/Features.vue'
import Download from './components/Download.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/features', component: Features },
  { path: '/download', component: Download }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

createApp(App).use(router).mount('#app')
