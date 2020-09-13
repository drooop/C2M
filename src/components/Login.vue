<template>
    <div class="hello">
        <!-- 显示当前进行到第几个步骤，stepNum来控制-->
        <van-row>
            <van-col :span="2"></van-col>
            <van-col :span="20">
                <van-steps :active="stepNumber">
                    <van-step>正面预览</van-step>
                    <van-step>背面信息</van-step>
                    <van-step>生成工单</van-step>
                </van-steps>
            </van-col>
            <van-col :span="2"></van-col>
        </van-row>

        <!-- 所有步骤的外框，框在一个row里 -->
        <van-row type="flex" justify="center">
            <van-col :span="2"></van-col>
            <van-col :span="20">
                <!-- 1. 第一个步骤，选择正面打印图片(固定) -->
                <div v-if="stepNumber == 0">
                    <!-- 图片选择区域 -->
                    <div>
                        <van-radio-group v-model="imageSelectedBox1">
                            <van-cell-group>
                                <van-cell clickable @click="radio = '1'">
                                    <van-radio name="china_telecom">
                                        <van-image height="100" fit="scale-down"
                                            src="http://c2m.tq.yhlcps.com/statics/image/china_telecom.jpeg">
                                            <template v-slot:error>加载失败</template>
                                        </van-image>
                                    </van-radio>
                                </van-cell>
                            </van-cell-group>
                        </van-radio-group>
                        <div class="previewImgFirst">
                            <!-- 产品预览区域 -->
                            <van-image class="normalFrontImg" width="100%" fit="scale-down" :src="normalFrontImgURL">
                                <template v-slot:error>加载失败</template>
                            </van-image>
                        </div>

                    </div>
                    <!-- 底部导航区域 -->
                    <van-tabbar>
                        <van-tabbar-item> </van-tabbar-item>
                        <van-tabbar-item> </van-tabbar-item>
                        <van-tabbar-item> </van-tabbar-item>
                        <van-tabbar-item>
                            <van-button type="info" @click="onClickConfirmProductType">
                                下一步
                            </van-button>
                        </van-tabbar-item>
                    </van-tabbar>
                </div>
                <!-- 2. 第二个步骤 -->
                <div v-if="stepNumber == 1">
                    <div>
                        <p>请选择其中一种，作为产品的背面信息。目前可打印文字信息与图片</p>
                        <van-radio-group v-model="imageSelectedBox2">
                            <van-cell-group>
                                <!-- 2.1 图片选择(目前别无选择就一张) -->
                                <van-cell clickable @click="radio = '1'">
                                    <van-radio name="image">
                                        图片
                                    </van-radio>
                                </van-cell>
                                <!-- 2.2 文字输入 -->
                                <van-cell clickable @click="radio = '1'">
                                    <van-radio name="text">
                                        文字
                                    </van-radio>
                                </van-cell>

                            </van-cell-group>
                        </van-radio-group>
                        <div style="margin-top:5%;" v-show="textDisplayBoolean()">
                            背面文字：<van-form ref="boxFormRef" validate-first>
                                <van-field v-model="front_box" name="front_box" label="" placeholder="输入您想展示的文字"
                                    maxlength="14" show-word-limit
                                    :rules="[{ required: true, message: '请务必输入文字信息哦' }]" />
                            </van-form>
                        </div>

                        <div v-show="imageDisplayBoolean()">
                            背面图片：
                            <van-image height="100" fit="scale-down"
                                src="http://c2m.tq.yhlcps.com/statics/image/meet_future.jpeg" />
                        </div>
                        <div class="previewImgSecond">
                            <!-- 产品预览区域 -->
                            <van-image class="normalBackImgURL" width="100%" fit="scale-down" :src="normalBackImgURL">
                                <template v-slot:error>加载失败</template>
                            </van-image>
                        </div>


                    </div>

                    <!-- 底部导航 -->
                    <van-tabbar>
                        <van-tabbar-item>
                            <van-button type="info" @click="onClickPreviousStep">
                                上一步
                            </van-button>
                        </van-tabbar-item>
                        <van-tabbar-item> </van-tabbar-item>
                        <van-tabbar-item> </van-tabbar-item>
                        <van-tabbar-item>
                            <van-button type="info" @click="onClickConfirmProductInfo">
                                下一步
                            </van-button>
                        </van-tabbar-item>
                    </van-tabbar>
                </div>
                <!-- 3. 第三个步骤 -->
                <div v-if="stepNumber == 2">
                    <p>请点击右下角的“生成工单”按钮以产生工单～</p>
                    <!-- 底部导航 -->
                    <van-tabbar>
                        <van-tabbar-item>
                            <van-button type="info" @click="onClickPreviousStep">
                                上一步
                            </van-button>
                        </van-tabbar-item>
                        <van-tabbar-item> </van-tabbar-item>
                        <van-tabbar-item> </van-tabbar-item>
                        <van-tabbar-item>
                            <van-button type="info" @click="onClickGenerateOrder">
                                生成工单
                            </van-button>
                        </van-tabbar-item>
                    </van-tabbar>
                </div>
            </van-col>
            <van-col :span="2"></van-col>
        </van-row>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                pickup_code: "",
                normalFrontImgURL: "http://c2m.tq.yhlcps.com/statics/c2m/general_cardcase_front_preview.jpg",
                normalBackImgURL: "http://c2m.tq.yhlcps.com/statics/c2m/general_cardcase_back_preview.jpg",

                // 步骤导航条控制
                stepNumber: 0,

                // url配置
                imageUploadUrl: "http://c2m.tq.yhlcps.com/image",
                orderCreateUrl: "http://c2m.tq.yhlcps.com/api/create",

                // 控制Product Type选择器
                productType: "名片夹",

                // 控制背面是文字还是图片
                backContentType: "text",

                // Form Data
                user_openid: "",

                // Form Data Box
                front_box: "5G智能制造",
                // reverse_box: "tq_film_1",
                testBoolean: true,

                imageSelectedBox1: "china_telecom",
                imageSelectedBox2: "",
                imageSelectedKeyChain: "1",
            };
        },

        mounted() {
            const openid = this.$route.params.openid;
            this.user_openid = openid;
            console.log(openid);
        },
        methods: {
            textDisplayBoolean() {
                if (this.imageSelectedBox2 == "text") {
                    return true
                } else {
                    return false
                }
            },
            imageDisplayBoolean() {
                if (this.imageSelectedBox2 == "image") {
                    return true
                } else {
                    return false
                }
            },
            normalPreviewImgDisplay() {
                if (this.productType == "名片夹") {
                    return true
                } else {
                    return false
                }
            },
            onClickConfirmProductType() {
                this.stepNumber += 1;
            },

            onClickPreviousStep() {
                this.stepNumber -= 1;
            },

            onClickConfirmProductInfo() {
                if (this.imageSelectedBox2) {
                    this.stepNumber += 1;
                } else {
                    this.$dialog.alert({ message: "请告诉我您想要文字还是图片呢～" })
                    return
                }
            },

            onClickGenerateOrder_dialog(code) {
                this.$dialog.alert({
                    title: '您本次的取件码为:' + code,
                    message: '<p>您可以继续进行的操作：</p><p>1. 公众号回复“取件码”获取订单详情</p><p>2. 公众号中回复“订单”获取您的订单</p>',
                    theme: 'round-button',
                }).then(() => {
                    this.$router.push("/close_page");
                    this.clearAllFormData();
                })
            },

            onClickGenerateOrder() {
                var temOpenId = this.user_openid;

                this.$dialog
                    .confirm({
                        title: "生成工单",
                        message: "是否确认下单",
                    })
                    .then(async () => {
                        // on confirm
                        var data = ""
                        if (this.imageSelectedBox2 === "text") {
                            data = this.front_box
                        } else if (this.imageSelectedBox2 === "image") {
                            data = "logo2"
                        } else {
                            this.$toast("解析上传信息时遇到了未知错误");
                            return
                        }
                        const draw_info = {
                            data: data
                        };

                        console.log("draw_info:\n", draw_info);

                        const orderForm = {
                            user_openid: this.user_openid,
                            goods_type: this.productType,
                            draw_info: draw_info,
                        };

                        console.log(orderForm);

                        // if (this.constantCondition) {
                        const { data: res } = await this.$http.post(
                            this.orderCreateUrl,
                            orderForm
                        );

                        // 如果取到的status是200以外的数，或取到的status是undefined
                        if (res.meta.status != 200) {
                            this.$toast("订单生成失败请稍后再试");
                            this.$route.push("/login/" + temOpenId);
                            return;
                        }

                        var pickup_code = res.data.pickup_code;
                        console.log("pickup_code: ", pickup_code);
                        // 数据初始化

                        this.onClickGenerateOrder_dialog(pickup_code)
                    })
                    .catch(() => {
                        // on cancel
                    });

            },

            // clearAllFormData
            clearAllFormData() {
                // 数据初始化
                this.stepNumber = 0;
                // Product Type
                this.productType = "名片夹";
                this.imageSelectedBox1 = "1";
                this.imageSelectedBox2 = "1";
            },
        },
    };
</script>

<style scoped>
    .previewImgFirst {
        position: absolute;
        left: 0%;
        bottom: 15%;
    }

    .previewImgSecond {
        position: absolute;
        left: 0%;
        bottom: 15%;
    }
</style>