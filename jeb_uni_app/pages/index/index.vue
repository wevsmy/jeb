<template>
	<view class="content">
		<!-- 消息提示 -->
		<u-toast ref="uToast"></u-toast>
		<view>嘉E保商城</view>

	</view>
</template>

<script>
	export default {
		data() {
			return {

			}
		},
		watch: {
			show(n) {
				console.log(n);
			}
		},
		methods: {

		}
	}
</script>

<style lang="scss" scoped>

</style>
