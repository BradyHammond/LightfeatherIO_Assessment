import Vue from 'vue'
import App from './App'
import router from './router'
import vuetify from '@/plugins/vuetify'

// Set config variables
Vue.config.productionTip = false

// Initialize Vue app
new Vue({
  el: '#app',
  router,
  vuetify,
  render: h => h(App)
})
