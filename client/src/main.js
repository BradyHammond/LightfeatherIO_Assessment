import Vue from 'vue'
import vuetify from '@/plugins/vuetify'
import App from './App'
import router from './router'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  vuetify,
  router,
  render: h => h(App)
})
