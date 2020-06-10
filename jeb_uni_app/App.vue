<script>
	import Vue from 'vue'

	export default {
		onLaunch: function() {
			console.log('App Launch');

			// 获取系统信息
			uni.getSystemInfo({
				success: function(res) {
					// console.log(e)
					Vue.prototype.$global_systemInfo = JSON.stringify(res);
				}
			});

			// 获取网络信息
			uni.getNetworkType({
				success: function(res) {
					// console.log(res);
					Vue.prototype.$global_networkType = res.networkType;
					// console.log(res.networkType);
				}
			});

		},
		onShow: function() {
			console.log('App Show');
		},
		onHide: function() {
			console.log('App Hide');
		},
		methods: {

		}
	};
</script>

<style lang="scss">
	/* 注意要写在第一行，同时给style标签加入lang="scss"属性 */
	@import "uview-ui/index.scss";

	/* 解决头条小程序组件内引入字体不生效的问题 */
	/* #ifdef MP-TOUTIAO */
	@font-face {
		font-family: uniicons;
		src: url('/static/uni.ttf');
	}

	/* #endif */
</style>
