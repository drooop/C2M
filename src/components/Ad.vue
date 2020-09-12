<template>
    <div @touchmove.prevent @mousewheel.prevent>
        <van-image width="100%" :height="screenHeight"
            src="http://c2m.tq.yhlcps.com/statics/image/advertisement_0911.jpg" lazy-load fit="fill"
            @click="go_to_login_page" />
    </div>
</template>

<script>
    export default {
        data() {
            return {
                user_openid: '',
                screenHeight: document.documentElement.clientHeight
            }
        },

        mounted() {
            // document.body.addEventListener('touchmove', function (e) {
            //     e.preventDefault();
            //     e.stopPropagation();
            // }, { passive: false });

            const openid = this.$route.params.openid;
            this.user_openid = openid;
            console.log(openid);

            const that = this
            window.onresize = () => {
                return (() => {
                    window.screenHeight = document.documentElement.clientHeight
                    that.screenHeight = window.screenHeight

                })()
            }
            console.log(that.screenHeight)
        },

        methods: {
            go_to_login_page() {
                this.$router.push('/login/' + this.user_openid);
            },
        },
    };
</script>

<style>

</style>