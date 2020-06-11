<template>
	<view class="content">
		<!-- 消息提示 -->
		<u-toast ref="uToast"></u-toast>
		<view class="header">
			<view class="top">
				<view class="avatar">
					<u-avatar src="" mode="square"></u-avatar>
				</view>
				<view class="name">
					willson.wu
				</view>

			</view>
			<view class="info">
				<view class="item">
					<view class="title">
						<view class="line"></view>
						<view class="text">
							医疗险
						</view>
						<view class="line"></view>
					</view>

					<view class="money">
						<view class="num">
							600
						</view>
						<view class="unit">
							万
						</view>
						<view class="icon">
							未保障
						</view>
					</view>

					<view class="desc">
						医保100%报销
					</view>

					<view class="btn">
						<u-button type="warning" shape="circle" size="mini">开启保障</u-button>
					</view>

				</view>

				<view class="item">
					<view class="title">
						<view class="line"></view>
						<view class="text">
							重疾险
						</view>
						<view class="line"></view>
					</view>

					<view class="money">
						<view class="num">
							500
						</view>
						<view class="unit">
							元
						</view>
						<view class="icon">
							未保障
						</view>
					</view>

					<view class="desc">
						赠送健康保障金
					</view>

					<view class="btn">
						<u-button type="warning" shape="circle" size="mini">领取保障</u-button>
					</view>

				</view>

				<view class="item">
					<view class="title">
						<view class="line"></view>
						<view class="text">
							意外险
						</view>
						<view class="line"></view>
					</view>

					<view class="money">
						<view class="num">
							40
						</view>
						<view class="unit">
							万
						</view>
						<view class="icon">
							未保障
						</view>
					</view>

					<view class="desc">
						赠送出行意外险
					</view>

					<view class="btn">
						<u-button type="warning" shape="circle" size="mini">领取保障</u-button>
					</view>

				</view>

			</view>

		</view>
		<view class="banner">
			<u-swiper :list="bannerList" img-mode="aspectFit" border-radius="30" height="160"></u-swiper>
		</view>


		<view class="about">
			<view class="title">
				<u-section title="关于我们" :show-line="false" sub-color="#126ef8" font-size="40"></u-section>
			</view>
			<view class="info">
				<image class="img" src="../../static/img/us1_new.png"></image>
				<image class="img" src="../../static/img/us2_new.png"></image>
				<image class="img" src="../../static/img/us3_new.png"></image>

			</view>

		</view>
		<view class="footer">
			<image class="img" src="../../static/img/logo_no_slogan.jpg" mode="aspectFit"></image>
			<view class="customer">
				<view class="icon">
					<u-icon name="kefu-ermai" color="#2979ff" size="36"></u-icon>
				</view>
				<view class="text">联系客服</view>
			</view>
		</view>

	</view>
</template>

<script>
	export default {
		data() {
			return {
				bannerList: [{
						image: '../../static/img/ketang.jpg',
						title: '蒹葭苍苍，白露为霜。所谓伊人，在水一方'
					},
					{
						image: '../../static/img/bxgw.jpg',
						title: '溯洄从之，道阻且长。溯游从之，宛在水中央'
					},
					{
						image: '../../static/img/banner20618.jpg',
						title: '蒹葭萋萋，白露未晞。所谓伊人，在水之湄'
					}
				]

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
	.content {

		.header {
			width: 100%;
			height: 247.47px;
			background: url(../../static/img/index-bg.jpg) no-repeat;
			background-size: contain;

			padding-top: 40rpx;
			padding-left: 40rpx;
			padding-right: 40rpx;

			font-size: 12px;

			.top {
				display: flex;

				.avatar {
					margin-right: 20rpx;
				}

				.name {
					font-size: 16px;
					color: #FFFFFF;

					line-height: 80rpx;
					font-weight: 400;


				}
			}

			.info {

				margin-top: 40rpx;
				height: 167.5px;
				display: flex;
				justify-content: space-between;

				.item {

					width: 220rpx;
					height: 300rpx;

					padding-top: 20rpx;
					padding-bottom: 20rpx;

					color: #000000;
					background: #FFFFFF;

					border-radius: 20rpx;
					box-sizing: border-box;

					font-size: 12px;

					box-shadow: 0 0.4px 3px 0 rgba(0, 0, 0, .1);
					position: relative;


					.title {

						line-height: 4.5px;
						display: flex;
						justify-content: center;
						align-items: center;
						text-align: center;
						font-size: 12px;

						.line {
							width: 2.6px;
							line-height: 4.5px;
							height: 1px;
							border-radius: 0.5px;
							background: #126ef8;
						}

						.text {
							margin: 1px;
							font-size: 4.5px;
							line-height: 5.6px;
							color: #126ef8;
							text-align: center;
							font-weight: 700;
						}

					}

					.money {
						margin-top: 20px;
						text-align: center;

						.num {
							position: absolute;
							top: 35px;
							right: 40px;
							font-size: 25px;
							font-weight: 500;
							letter-spacing: -1.5px;
							color: #333;
							font-family: DIN-Alternate-Bold;
						}

						.unit {
							position: absolute;
							top: 47px;
							right: 25px;
							font-size: 13px;
							font-weight: 500;
							color: #333;
						}

						.icon {
							position: absolute;
							width: 37px;
							height: 14px;
							line-height: 14px;
							top: 30px;
							right: 5px;
							color: #848484;
							text-align: center;
							background: #efefef;
							border-radius: 7px;
							border-bottom-left-radius: 0;
						}
					}

					.desc {
						margin-top: 55px;
						font-size: 12px;
						color: #666;
						text-align: center;
					}

					.btn {
						margin: 50rpx 40rpx;
					}

				}
			}
		}

		.banner {
			margin-top: 40rpx;
			margin-left: 40rpx;
			margin-right: 40rpx;
		}


		.about {
			margin-left: 40rpx;
			margin-right: 40rpx;

			.title {
				margin-top: 50rpx;
			}

			.info {
				display: flex;
				margin: 40rpx auto;
				justify-content: space-between;

				.img {
					width: 176rpx;
					height: 176rpx;
				}
			}
		}

		.footer {

			display: flex;
			flex-direction: column;
			justify-items: center;
			align-items: center;
			margin-top: 60rpx;
			padding-bottom: 40rpx;

			.img {
				width: 300rpx;
				height: 63rpx;
			}

			.customer {
				display: flex;
				align-items: center;
				margin: 40rpx auto;
				color: #1e91f4;

				.icon {
					margin-right: 10rpx;
				}
			}

		}
	}
</style>
