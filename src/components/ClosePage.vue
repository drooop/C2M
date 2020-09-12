<template>
    <div @touchmove.prevent @mousewheel.prevent>
        <van-image width="100%" :height="screenHeight"
            src="http://c2m.tq.yhlcps.com/statics/image/close_page.jpg" lazy-load fit="fill" />
    </div>
</template>

<script>
    export default {
        data() {
            return {
                screenHeight: document.documentElement.clientHeight
            }
        },

        mounted() {
            const that = this
            window.onresize = () => {
                return (() => {
                    window.screenHeight = document.documentElement.clientHeight
                    that.screenHeight = window.screenHeight
                })()
            }
            console.log(that.screenHeight)
        },

        methods: {},
    };
</script>

<style>
</style>