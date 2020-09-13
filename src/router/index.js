import Vue from "vue";
import VueRouter from "vue-router";
import Login from "@/components/Login.vue";
import Error from "@/components/Error.vue";
import End from "@/components/End.vue";
// import CutPic from "@/components/CutPic.vue";
import FlutterApp from "@/components/FlutterApp.vue";
import Ad from "@/components/Ad.vue";
import Ad_VIP from "@/components/Ad_VIP.vue";
import SuperUserEntry from "@/components/SuperUserEntry.vue";
import ClosePage from "@/components/ClosePage.vue";
import RedirectForVIP from "@/components/RedirectForVIP.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/login/:openid/",
    component: Login,
  },
  {
    path: "/super/eaac28c5-15e5-4486-b37e-e2281a7e31a6",
    // component: SuperUserEntry,
    component: RedirectForVIP,
  },
  {
    path: "/vip/:openid",
    component: SuperUserEntry,
  },
  {
    path: "/vip_ad/:openid",
    component: Ad_VIP,
  },
  {
    path: "/close_page",
    component: ClosePage,
  },
  {
    path: "/error",
    component: Error,
  },
  {
    path: "/end/:pickup_code/",
    component: End,
  },
  {
    path: "/flutterweb",
    component: FlutterApp,
  },
  {
    path: "/ad/:openid/",
    component: Ad,
  },
];

const router = new VueRouter({
  routes,
});

// 挂在路由导航守卫
// router.beforeEach((to, from, next) => {
//   // to 将要访问的路径
//   // from 代表从哪个路径跳转进来
//   // next 是一个表示放行的函数

//   // netx() 放行    next('/login') 强制跳转
//   if (to.path === "/login") {
//     return next();
//   }
//   // 获取token
//   const tokenStr = window.sessionStorage.getItem("token");
//   // 如果无token, 强制跳转到'/login'
//   if (!tokenStr) {
//     return next("/login");
//   }
//   // 有 token, 放行
//   next();
// });

export default router;
