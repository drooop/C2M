<template>
    <div id="apply" class="hello">
        <!-- 显示当前进行到第几个步骤，stepNum来控制-->
        <van-row>
            <van-col :span="2"></van-col>
            <van-col :span="20">
                <van-steps :active="stepNumber">
                    <van-step>产品类型选择</van-step>
                    <van-step>信息录入</van-step>
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
                    <van-radio-group v-model="productType">
                        <van-cell-group>
                            <van-cell clickable @click="radio = '1'">
                                <van-radio name="名片夹vip">
                                    <p>皮质名片夹</p>
                                </van-radio>
                            </van-cell>
                            <van-cell clickable @click="radio = '2'">
                                <van-radio name="名片夹">
                                    <p>普通名片夹</p>
                                </van-radio>
                            </van-cell>
                        </van-cell-group>
                    </van-radio-group>
                    <!-- 产品预览区域 -->
                    <van-image v-show="normalPreviewImgDisplay()" class="productPreviewImg" width="100%"
                        fit="scale-down" :src="normalPreviewImgURL">
                        <template v-slot:error>加载失败</template>
                    </van-image>
                    <van-image v-show="vipPreviewImgDisplay()" class="productPreviewImg" width="100%" fit="scale-down"
                        :src="vipPreviewImgURL">
                        <template v-slot:error>加载失败</template>
                    </van-image>
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
                    <!-- 指定图片图片区域 -->
                    <p>固定的图片</p>
                    <van-image height="100" fit="scale-down" :src="china_telecom_URL">
                        <template v-slot:error>加载失败</template>
                    </van-image>
                    <!-- 可选图片图片区域 -->
                    <p v-show="vipInfoDisplay()">请选择其中一种，作为产品账面右侧的内容。目前可打印文字信息与图片</p>
                    <p v-show="normalInfoDisplay()">请选择其中一种，作为产品背面的内容。目前可打印文字信息与图片</p>
                    <van-radio-group v-model="imageSelectedBox2">
                        <van-cell-group>
                            <!-- 2.1 图片选择(目前别无选择就一张) -->
                            <van-cell clickable @click="radio = '1'">
                                <van-radio name="image">
                                    图片
                                </van-radio>
                            </van-cell>
                            <van-cell clickable @click="radio = '2'">
                                <!-- 2.2 文字输入 -->
                                <van-radio name="text1">
                                    文字: "边缘协同生产"
                                </van-radio>
                            </van-cell>
                            <van-cell clickable @click="radio = '3'">
                                <!-- 2.2 文字输入 -->
                                <van-radio name="text2">
                                    文字: "5G智能制造"
                                </van-radio>
                            </van-cell>
                            <van-cell clickable @click="radio = '4'">
                                <!-- 2.2 文字输入 -->
                                <van-radio name="text3">
                                    文字: "5G智慧工厂"
                                </van-radio>
                            </van-cell>
                            <van-cell clickable @click="radio = '5'">
                                <!-- 2.2 文字输入 -->
                                <van-radio name="text_cust">
                                    自定义文字
                                </van-radio>
                            </van-cell>
                        </van-cell-group>
                    </van-radio-group>
                    <div style="margin-top:5%;" v-show="textDisplayBoolean()">
                        背面文字：<van-form ref="boxFormRef" validate-first>
                            <van-field v-model="front_box" name="front_box" label="" placeholder="输入您想展示的文字"
                                maxlength="7" show-word-limit :rules="[{ required: true, message: '请务必输入文字信息哦' }]" />
                        </van-form>
                    </div>

                    <div v-show="imageDisplayBoolean()">
                        背面图片：
                        <van-image height="100" fit="scale-down" :src="meet_future_URL" />
                    </div>

                    <!-- 底部导航 -->
                    <van-tabbar v-show="inputPageNavigatorDisplayBoolean">
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
                inputPageNavigatorDisplayBoolean: true,
                defaultHeight: '0',  //默认屏幕高度
                nowHeight: '0',  //实时屏幕高度

                normalPreviewImgURL: "http://c2m.tq.yhlcps.com/statics/c2m/general_cardcase_preview.jpg",
                vipPreviewImgURL: "http://c2m.tq.yhlcps.com/statics/c2m/vip_cardcase_preview.jpg",

                // 步骤导航条控制
                stepNumber: 0,

                // url配置
                imageUploadUrl: "http://c2m.tq.yhlcps.com/statics/image/",
                orderCreateUrl: "http://c2m.tq.yhlcps.com/api/create",
                meet_future_URL: "http://c2m.tq.yhlcps.com/statics/image/meet_future.jpeg",
                china_telecom_URL: "http://c2m.tq.yhlcps.com/statics/image/china_telecom.jpeg",

                // 控制Product Type选择器, 名片夹/名片夹vip
                productType: "名片夹vip",
                user_openid: "user_open_id",

                // Form Data Box
                front_box: "5G智能制造",

                imageSelectedBox1: "china_telecom",
                imageSelectedBox2: "",
                imageSelectedKeyChain: "1",

                uploaderCardImageFlag: false,
                uploaderCardImageList: [],
            };
        },

        mounted() {
            // eaac28c5-15e5-4486-b37e-e2281a7e31a6
            const openid = this.$route.params.openid;
            this.user_openid = openid;
            console.log('vip:' + this.user_openid)

            // this.defaultHeight = $(window).height();
            this.defaultHeight = window.innerHeight
            window.onresize = () => {
                return (() => {
                    // this.nowHeight = $(window).height();
                    this.nowHeight = window.innerHeight
                })();
            };


        },
        methods: {
            testOnFocus() {
                this.inputPageNavigatorDisplayBoolean = false
            },
            testOnBlur() {
                this.inputPageNavigatorDisplayBoolean = true
            },
            textDisplayBoolean() {
                if (this.imageSelectedBox2 == "text_cust") {
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

            vipInfoDisplay() {
                if (this.productType == "名片夹vip") {
                    return true
                } else {
                    return false
                }
            },
            normalInfoDisplay() {
                if (this.productType == "名片夹") {
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
            vipPreviewImgDisplay() {
                if (this.productType == "名片夹vip") {
                    return true
                } else {
                    return false
                }
            },
            onClickConfirmProductType() {
                if (this.imageSelectedBox1) {
                    this.stepNumber += 1;
                } else {
                    this.$dialog.alert({ message: "Please input info" })
                    return
                }
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
                this.$dialog
                    .confirm({
                        title: "生成工单",
                        message: "是否确认下单",
                    }).then(async () => {
                        // on confirm
                        var data = ""
                        if (this.imageSelectedBox2 === "text_cust") {
                            data = this.front_box
                        } else if (this.imageSelectedBox2 === "text1") {
                            data = "边缘协同生产"
                        } else if (this.imageSelectedBox2 === "text2") {
                            data = "5G智能制造"
                        } else if (this.imageSelectedBox2 === "text3") {
                            data = "5G智慧工厂"
                        } else if (this.imageSelectedBox2 === "image") {
                            data = "logo2"
                        } else {
                            this.$toast("解析上传信息时遇到了未知错误");
                            return
                        }
                        const draw_info = {
                            data: data
                        };

                        const orderForm = {
                            user_openid: this.user_openid,
                            goods_type: this.productType,
                            draw_info: draw_info,
                        };

                        console.log(orderForm);

                        const { data: res } = await this.$http.post(
                            this.orderCreateUrl,
                            orderForm
                        );

                        // 如果取到的status是200以外的数，或取到的status是undefined
                        if (res.meta.status != 200) {
                            this.$toast("订单生成失败请稍后再试");
                            this.$route.push("/login/" + this.openid);
                            return;
                        }

                        var pickup_code = res.data.pickup_code;
                        console.log(pickup_code)

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
                this.productType = "名片";

                // Option1 meet_futrue.jpg
                this.imageSelectedBox1 = "1";

                // Option2 text or image
                this.imageSelectedBox2 = "1";
            },
        },

        watch: {
            nowHeight: function () {
                if (this.defaultHeight != this.nowHeight) {
                    //键盘弹出操作
                    this.inputPageNavigatorDisplayBoolean = false
                } else {
                    //键盘不弹出操作
                    this.inputPageNavigatorDisplayBoolean = true
                }
            }
        }
    };
</script>

<style scoped>
    .focusState {
        position: absolute;
    }

    /* .productPreviewImg {
        position: absolute;
        left: 0%;
        bottom: 10%;
    } */
</style>