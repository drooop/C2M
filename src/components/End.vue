<template>
  <div>
    <p>您的取件码为：{{ pickup_code }}</p>
    <p>请关闭本页面后:</p>
    <p>1. 在本公众号中回复取件码获取本订单详情</p>
    <p>2. 公众号中回复“订单”获取您的所有订单</p>
    <!-- <van-button @click="closePage">
      返回微信公众号
    </van-button> -->
  </div>
</template>

<script>
export default {
  data() {
    return {
      pickup_code: 0,
    };
  },

  mounted() {
    const pickup_code = this.$route.params.pickup_code;
    this.pickup_code = pickup_code;
    console.log("in End component", this.pickup_code);

    //     const oScript = document.createElement("script");
    //     oScript.type = "text/javascript";
    //     oScript.src = "http://res.wx.qq.com/open/js/jweixin-1.6.0.js";
    //     document.body.appendChild(oScript);

    //     // 初始化配置
    //     wx.config({
    //       debug: true, // 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。
    //       appId: "wx63a775ce1f72fbcd", // 必填，公众号的唯一标识
    //       timestamp: "", // 必填，生成签名的时间戳
    //       nonceStr: "", // 必填，生成签名的随机串
    //       signature: "", // 必填，签名
    //       jsApiList: [], // 必填，需要使用的JS接口列表
    //     });
  },

  methods: {
    //     closePage() {
    //       //   WeixinJSBridge.call("closeWindow");
    //       //这个可以关闭安卓系统的手机
    //       document.addEventListener(
    //         "WeixinJSBridgeReady",
    //         function() {
    //           WeixinJSBridge.call("closeWindow");
    //         },
    //         false
    //       );
    //       //这个可以关闭ios系统的手机
    //       WeixinJSBridge.call("closeWindow");
    //     },
  },
};
</script>

<style></style>
