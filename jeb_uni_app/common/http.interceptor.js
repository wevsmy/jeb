// 获取token
const getTokenStorage = () => {
	let token = ''
	try {
		token = uni.getStorageSync('token')
	} catch (e) {
		//TODO handle the exception
	}
	return token
}

// 这里的vm，就是我们在vue文件里面的this，所以我们能在这里获取vuex的变量，比如存放在里面的token
// 同时，我们也可以在此使用getApp().globalData，如果你把token放在getApp().globalData的话，也是可以使用的
const install = (Vue, vm) => {
	if (process.env.NODE_ENV === 'development') {
		// 开发环境
		Vue.prototype.$u.http.setConfig({
			// baseUrl: 'http://172.18.137.180:3000',
			// baseUrl: 'https://dev.weii.ink',
			// baseUrl: 'https://www.fastmock.site/mock/0d5bcb071b3e4ca35dd3b78d04ef8191/mock',

			// #ifdef H5
			baseUrl: 'http://172.18.137.178:8011',
			// baseUrl: 'http://192.168.2.100:8011',
			// baseUrl: 'http://api.m.weii.ink',
			// baseUrl: 'https://www.fastmock.site/mock/0d5bcb071b3e4ca35dd3b78d04ef8191/mock',
			// #endif

			// #ifdef MP-WEIXIN
			baseUrl: 'https://dev.weii.ink',
			// #endif

			// #ifdef APP-PLUS
			baseUrl: 'https://www.fastmock.site/mock/0d5bcb071b3e4ca35dd3b78d04ef8191/mock',
			// #endif

			method: 'POST',
			// 设置为json，返回后会对数据进行一次JSON.parse()
			dataType: 'json',
			showLoading: true, // 是否显示请求中的loading
			loadingText: '努力加载中~', // 请求loading中的文字提示
			loadingTime: 800, // 在此时间内，请求还没回来的话，就显示加载中动画，单位ms
			originalData: true, // 是否在拦截器中返回服务端的原始数据
			loadingMask: true, // 展示loading的时候，是否给一个透明的蒙层，防止触摸穿透
			// 如果将此值设置为true，拦截回调中将会返回服务端返回的所有数据response，而不是response.data
			// 设置为true后，就需要在this.$u.http.interceptor.response进行多一次的判断，请打印查看具体值
			// originalData: true, 
		});
	} else {
		// 生产环境
		Vue.prototype.$u.http.setConfig({
			baseUrl: 'https://m.okeuu.com',

			method: 'POST',
			// 设置为json，返回后会对数据进行一次JSON.parse()
			dataType: 'json',
			showLoading: true, // 是否显示请求中的loading
			loadingText: '请求中...', // 请求loading中的文字提示
			loadingTime: 800, // 在此时间内，请求还没回来的话，就显示加载中动画，单位ms
			originalData: true, // 是否在拦截器中返回服务端的原始数据
			loadingMask: true, // 展示loading的时候，是否给一个透明的蒙层，防止触摸穿透
			// 如果将此值设置为true，拦截回调中将会返回服务端返回的所有数据response，而不是response.data
			// 设置为true后，就需要在this.$u.http.interceptor.response进行多一次的判断，请打印查看具体值
			// originalData: true, 
		});
	}
	// 请求拦截，配置Token等参数
	Vue.prototype.$u.http.interceptor.request = (config) => {
		// config.header.token = 'xxxxxx';
		config.header.token = getTokenStorage();

		// 方式一，存放在vuex的token，假设使用了uView封装的vuex方式，见：https://uviewui.com/components/globalVariable.html
		// config.header.token = vm.token;

		// 方式二，如果没有使用uView封装的vuex方法，那么需要使用$store.state获取
		// config.header.token = vm.$store.state.token;

		// 方式三，如果token放在了globalData，通过getApp().globalData获取
		// config.header.token = getApp().globalData.username;

		// 方式四，如果token放在了Storage本地存储中，拦截是每次请求都执行的，所以哪怕您重新登录修改了Storage，下一次的请求将会是最新值
		// const token = uni.getStorageSync('token');
		// config.header.token = token;

		// 可以对某个url进行特别处理，此url参数为this.$u.get(url)中的url值
		// if (config.url == '/user/login') config.header.noToken = true;
		// 如果return一个false值，则会取消本次请求
		// if(config.url == '/user/rest') return false; // 取消某次请求

		// 最后需要将config进行return
		return config;
	}
	// 响应拦截，判断状态码是否通过
	Vue.prototype.$u.http.interceptor.response = (res) => {
		if (process.env.NODE_ENV === 'development') {
			console.log('全局响应拦截:', res);
		}

		// 如果把originalData设置为了true，这里得到将会是服务器返回的所有的原始数据
		// 判断可能变成了res.statueCode，或者res.data.code之类的，请打印查看结果
		if (res.statusCode == 200) {
			// res为服务端返回值，可能有code，result等字段
			// 这里对res.result进行返回，将会在this.$u.post(url).then(res => {})的then回调中的res的到
			// 如果把originalData设置为了true，这里return回什么，this.$u.post的then回调中就会得到什么

			return res.data;

		} else if (res.statusCode == 201) {
			// nest 框架 post 请求默认返回201
			return res.data;
		} else if (res.statusCode == 401) {
			// 401为token失效，这里跳转登录

			vm.$u.toast('验证失败，请重新登录');
			setTimeout(() => {
				// 此为uView的方法，详见路由相关文档
				// vm.$u.route('/pages/login/login')
			}, 1500)
			return false;

		} else {
			// 如果返回false，则会调用Promise的reject回调，
			// 并将进入this.$u.post(url).then().catch(res=>{})的catch回调中，res为服务端的返回值
			return false;
		}
	}
}

export default {
	install
}
