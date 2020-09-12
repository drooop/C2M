import Vue from "vue";
import App from "./App.vue";
import router from "./router";

// import apiConfig from "../config/api.config";

import "./plugins/vant.js";
// 导入全局样式表
import "vant/lib/index.css";

// 导入cropperJS用于裁剪图片
// import "./plugins/cropperjs/dist/cropper.min.js";
// import "./plugins/cropperjs/dist/cropper.min.css";
// babel-polyfill 低版本兼容 axios请求
// import 'babel-polyfill'

// axios劫持http配置
import axios from "axios";
// axios.defaults.baseURL = "http://127.0.0.1:8888/api/private/v1/";
axios.interceptors.request.use((config) => {
  console.log(config);
  config.headers.Authorization = window.sessionStorage.getItem("token");
  // 最后必须return config
  return config;
});

Vue.prototype.$http = axios;

Vue.config.productionTip = false;

// axios.defaults.baseURL = apiConfig.baseUrl;

axios.defaults.withCredentials = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
