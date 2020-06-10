import Vue from 'vue'
import App from './App'

// 挂载 Vue.prototype
// 将一些使用频率较高的常量或者方法，直接扩展到 Vue.prototype 上，每个 Vue 对象都会“继承”下来。
// 注意这种方式只支持vue页面
Vue.config.productionTip = false
App.mpType = 'app'

// 引入全局uView
import uView from 'uview-ui'
Vue.use(uView)

// // 引入uView提供的对vuex的简写法文件
// let vuexStore = require('@/store/$u.mixin.js')
// Vue.mixin(vuexStore)

// 引入uView对小程序分享的mixin封装
let mpShare = require('uview-ui/libs/mixin/mpShare.js');
Vue.mixin(mpShare)

const app = new Vue({
	...App
})

// http拦截器，此为需要加入的内容，如果不是写在common目录，请自行修改引入路径
import httpInterceptor from '@/common/http.interceptor.js'
// 这里需要写在最后，是为了等Vue创建对象完成，引入"app"对象(也即页面的"this"实例)
Vue.use(httpInterceptor, app)

// http接口API抽离，免于写url或者一些固定的参数
import httpApi from '@/common/http.api.js'
Vue.use(httpApi, app)

app.$mount()
