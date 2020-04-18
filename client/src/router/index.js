import Vue from 'vue'
import Router from 'vue-router'

// Configure Vue routes
const routerOptions = [
  { path: '/', component: 'Registration' },
  { path: '/register', component: 'Registration' },
  { path: '*', component: 'NotFound' }
]

// Setup routing
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

// Add routes to Vue app
Vue.use(Router)

// Export router
export default new Router({
  routes,
  mode: 'history'
})
