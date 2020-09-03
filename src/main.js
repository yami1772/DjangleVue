// import Vue from 'vue'
// import App from './App.vue'
//
// Vue.config.productionTip = false
//
// new Vue({
//   render: h => h(App),
// }).$mount('#app')


import Vue from 'vue'
import App from './App.vue'
// import router from './router'
// import store from './store'

import ElementUI from 'element-ui'	// 添加
import 'element-ui/lib/theme-chalk/index.css'	// 添加
import axios from 'axios'	// 添加

axios.defaults.baseURL = 'http://127.0.0.1:800'	// 指定后端的地址，也就是django运行的地址
Vue.prototype.$http = axios	// 添加
Vue.use(ElementUI)	// 添加

Vue.config.productionTip = false

new Vue({
  // router,
  // store,
  render: h => h(App)
}).$mount('#app')