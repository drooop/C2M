<template>
  <div class="hello">
    <!-- 顶端Nav -->
    <!-- <van-row>
      <van-nav-bar
        title="云海流智能系统"
        :left-text="leftText"
        right-text=". . ."
        left-arrow
        @click-left="onClickLeft"
        @click-right="onClickRight"
      />
    </van-row> -->

    <!-- 显示当前进行到第几个步骤，stepNum来控制-->
    <van-row>
      <van-col :span="2"></van-col>
      <van-col :span="20">
        <van-steps :active="stepNumber">
          <!-- <van-step>类型选择</van-step> -->
          <van-step>信息输入</van-step>
          <van-step>工单生成</van-step>
        </van-steps>
      </van-col>
      <van-col :span="2"></van-col>
    </van-row>

    <!-- 所有步骤的外框，框在一个row里 -->
    <van-row type="flex" justify="center">
      <van-col :span="2"></van-col>
      <van-col :span="20">
        <!-- 1. 第一个步骤，选择产品类别 -->
        <!-- <div v-if="stepNumber == 0">
          <van-radio-group v-model="productType">
            <van-cell-group>
              <van-cell title="名片" clickable @click="radio = '名片'">
                <template #right-icon>
                  <van-radio name="名片" />
                </template>
              </van-cell>
              <van-cell title="名片夹" clickable @click="radio = '名片夹'">
                <template #right-icon>
                  <van-radio name="名片夹" />
                </template>
              </van-cell>
              <van-cell title="钥匙扣" clickable @click="radio = '钥匙扣'">
                <template #right-icon>
                  <van-radio name="钥匙扣" />
                </template>
              </van-cell>
            </van-cell-group>
          </van-radio-group>

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
        </div> -->


        <!-- 2. 第二个步骤 -->
        <div v-if="stepNumber == 1">
          <!-- 2.1名片 -->
          <div v-if="productType == '名片'">
            <van-form ref="cardFormRef" validate-first>
              <van-field
                v-model="body_name_card"
                name="body_name"
                label="姓名"
                placeholder="输入姓名"
                maxlength="8"
                show-word-limit
                :rules="[{ required: true, message: '请务必输入姓名' }]"
              />
              <van-field
                v-model="cor_name_card"
                name="cor_name"
                label="公司名称"
                placeholder="输入公司名称"
                :rules="[{ required: true, message: '请务必输入公司名称' }]"
              />
              <van-field
                v-model="cor_addr_card"
                name="cor_addr_card"
                label="公司地址"
                placeholder="输入公司地址"
                :rules="[{ required: true, message: '请务必输入公司地址' }]"
              />
              <van-field
                v-model="cor_phone_card"
                name="cor_phone"
                label="联系电话"
                placeholder="输入联系电话"
                :rules="[{ required: true, message: '请务必输入联系电话' }]"
              />
              <van-field
                v-model="cor_email_card"
                name="cor_email"
                label="电子邮箱"
                placeholder="输入电子邮箱"
                :rules="[{ required: true, message: '请务必输入电子邮箱' }]"
              />
            </van-form>

            <van-uploader
              v-model="uploaderCardImageList"
              :deletable="false"
              :max-count="1"
              :after-read="imageUploderCard"
            />
          </div>
          <!-- 2.2 名片夹 -->
          <div v-if="productType == '名片夹'">
            <van-form ref="boxFormRef" validate-first>
              <van-field
                v-model="front_box"
                name="front_box"
                label="正面文字"
                placeholder="输入您想展示的文字"
                maxlength="32"
                show-word-limit
                :rules="[{ required: true, message: '请务必输入文字信息哦' }]"
              />
            </van-form>
            <van-radio-group v-model="imageSelectedBox">
              <van-cell-group>
                <van-cell clickable @click="radio = '1'">
                  <van-radio name="tq_film_1">
                    <van-image
                      height="100"
                      fit="scale-down"
                      src="http://c2m.tq.yhlcps.com/statics/film/film1.png"
                    >
                      <template v-slot:error>加载失败</template>
                    </van-image>
                  </van-radio>
                </van-cell>

                <van-cell clickable @click="radio = '2'">
                  <van-radio name="tq_film_2">
                    <van-image
                      height="100"
                      fit="scale-down"
                      src="http://c2m.tq.yhlcps.com/statics/film/film2.png"
                    >
                      <template v-slot:error>加载失败</template>
                    </van-image>
                  </van-radio>
                </van-cell>

                <van-cell clickable @click="radio = '3'">
                  <van-radio name="tq_film_3">
                    <van-image
                      height="100"
                      fit="scale-down"
                      src="http://c2m.tq.yhlcps.com/statics/film/film3.png"
                    >
                      <template v-slot:error>加载失败</template>
                    </van-image>
                  </van-radio>
                </van-cell>

                <van-cell clickable @click="radio = '4'">
                  <van-radio name="tq_film_4">
                    <van-image
                      height="100"
                      fit="scale-down"
                      src="http://c2m.tq.yhlcps.com/statics/film/film4.png"
                    >
                      <template v-slot:error>加载失败</template>
                    </van-image>
                  </van-radio>
                </van-cell>
              </van-cell-group>
            </van-radio-group>
          </div>

          <!-- 2.3 钥匙扣 -->
          <div v-if="productType == '钥匙扣'">
            <van-radio-group v-model="imageSelectedKeyChain">
              <van-cell-group>
                <van-cell clickable @click="radio = '1'">
                  <van-radio name="tq_film_5">
                    <van-image
                      height="100"
                      fit="scale-down"
                      src="http://c2m.tq.yhlcps.com/statics/film/film5.png"
                    >
                      <template v-slot:error>加载失败</template>
                    </van-image>
                  </van-radio>
                </van-cell>

                <van-cell clickable @click="radio = '2'">
                  <van-radio name="tq_film_6">
                    <van-image
                      height="100"
                      fit="scale-down"
                      src="http://c2m.tq.yhlcps.com/statics/film/film6.png"
                    >
                      <template v-slot:error>加载失败</template>
                    </van-image>
                  </van-radio>
                </van-cell>
              </van-cell-group>
            </van-radio-group>
          </div>

          <!-- 公用的确认按钮 -->
          <!-- <van-row type="flex" justify="center">
            <van-button type="info" @click="onClickPreviousStep">
              上一步
            </van-button>
            <van-button type="info" @click="onClickConfirmProductInfo">
              下一步
            </van-button>
          </van-row> -->
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
          <!-- 假装是一个预览图 -->
          <!-- <van-image
            height="100"
            fit="scale-down"
            :src="require('../assets/test.png')"
            @click="showFlutterWeb"
          >
            <template v-slot:loading>
              <van-loading type="spinner" size="20" />
            </template>
            <template v-slot:error>预览图加载失败</template>
          </van-image> -->
          <p>请点击右下角的“生成工单”按钮以产生工单～</p>
          <!-- <van-button type="info" @click="onClickPreviousStep">
            上一步
          </van-button>
          <van-row type="flex" justify="center">
            <van-button type="info" @click="onClickGenerateOrder">
              生成工单
            </van-button>
          </van-row> -->
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

        <!-- </van-tab> -->
        <!-- </van-tabs> -->
      </van-col>
      <van-col :span="2"></van-col>
    </van-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      constantCondition: false,
      leftText: "",
      flag: false,

      // 步骤导航条控制
      stepNumber: 1,

      // url配置
      imageUploadUrl: "http://c2m.tq.yhlcps.com/image",
      orderCreateUrl: "http://c2m.tq.yhlcps.com/api/create",

      // 控制Product Type选择器
      productType: "名片夹",

      // Form Data
      user_openid: "",

      // FormData Card
      body_name_card: "",
      cor_name_card: "",
      cor_addr_card: "",
      cor_phone_card: "",
      cor_email_card: "",

      uploadImageName: "",

      imageFileContent: "",

      // Form Data Box
      front_box: "drop",
      // reverse_box: "tq_film_1",

      // Form Data Keychain
      reverse_keychain: "tq_film_5",

      imageSelectedCard: "1",
      imageSelectedBox: "tq_film_1",
      imageSelectedKeyChain: "1",

      uploaderCardImageFlag: false,
      uploaderCardImageList: [],
    };
  },

  mounted() {
    const openid = this.$route.params.openid;
    this.user_openid = openid;
    console.log(openid);
  },
  methods: {
    // onClickLeft() {
    //   this.$toast("返回");
    // },
    // onClickRight() {
    //   this.$toast("按钮");
    // },
    showFlutterWeb(){
      this.$router.push('/flutterweb');
    },
    onClickConfirmProductType() {
      this.stepNumber += 1;
    },

    onClickPreviousStep() {
      this.stepNumber -= 1;
    },

    async onClickConfirmProductInfo() {
      this.flag = false;

      const _this = this;

      if (this.productType == "名片") {
        console.log("it's Card!");
        this.$refs.cardFormRef
          .validate()
          .then(function() {
            if (_this.uploaderCardImageFlag == true) {
              _this.flag = true;
              _this.stepNumber += 1;
            } else {
              _this.$toast("未上传图片");
            }
          })
          .catch(function() {
            _this.$toast("表单未填写完整");
          });
      } else if (this.productType == "名片夹") {
        console.log("it's Box!");
        this.stepNumber += 1;
      } else if (this.productType == "钥匙扣") {
        console.log("it's KeyChain");
        this.stepNumber += 1;
      } else {
        console.log("Invalid ProductType!");
      }
    },

    onClickGenerateOrder() {
      var temOpenId = this.user_openid;

      if (this.productType == "名片") {
        this.$dialog
          .confirm({
            title: "生成工单",
            message: "是否确认下单",
          })
          .then(async () => {
            // on confirm
            const draw_info = {
              body_name: this.body_name_card,
              cor_name: this.cor_name_card,
              cor_addr: this.cor_addr_card,
              cor_phone: this.cor_phone_card,
              cor_email: this.cor_email_card,
              filename: this.uploadImageName,
            };

            console.log("draw_info:\n", draw_info);

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
              this.$route.push("/login/" + temOpenId);
              return;
            }

            const pickup_code = res.data.pickup_code;
            console.log("pickup_code: ", pickup_code);
            // 数据初始化
            this.clearAllFormData();
            this.$toast("上传成功");

            // this.$route.push("/login/" + temOpenId);
            this.$router.push("/end/" + pickup_code);
            this.$toast("订单生成完毕！");
            console.log(res);
          })
          .catch(() => {
            // on cancel
          });
      } else if (this.productType == "名片夹") {
        this.$dialog
          .confirm({
            title: "生成工单",
            message: "是否确认下单",
          })
          .then(async () => {
            // on confirm
            const draw_info = {
              front: this.front_box,
              reverse: this.imageSelectedBox,
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

            const pickup_code = res.data.pickup_code;
            console.log("pickup_code: ", pickup_code);
            // 数据初始化
            this.clearAllFormData();

            this.$toast("上传成功");

            // this.$route.push("/login/" + temOpenId);
            this.$router.push("/end/" + pickup_code);
            this.$toast("订单生成完毕！");
            console.log(res);
            // }
          })
          .catch(() => {
            // on cancel
          });
      } else if (this.productType == "钥匙扣") {
        this.$dialog
          .confirm({
            title: "生成工单",
            message: "是否确认下单",
          })
          .then(async () => {
            // on confirm
            const draw_info = {
              reverse: this.imageSelectedKeyChain,
            };

            console.log("draw_info:\n", draw_info);

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
              this.$route.push("/login/" + temOpenId);
              return;
            }

            const pickup_code = res.data.pickup_code;
            console.log("pickup_code: ", pickup_code);
            // 数据初始化
            this.clearAllFormData();

            this.$toast("上传成功");

            // this.$route.push("/login/" + temOpenId);
            this.$router.push("/end/" + pickup_code);
            this.$toast("订单生成完毕！");
            console.log(res);
          })
          .catch(() => {
            // on cancel
          });
      }
    },

    // 选择Card图片
    onChangeImageCard() {
      console.log("onChangeImageCard");
    },

    // 用户上传图片
    async imageUploderCard(file) {
      var myDate = new Date();
      var timeStampString = String(myDate.getTime());

      this.imageFileContent = file.content;
      this.uploadImageName = timeStampString + this.user_openid;
      console.log(this.uploadImageName);

      // 上传
      let param = new FormData(); // 创建form对象
      param.append("file", this.imageFileContent); // 通过append向form对象添加数据
      param.append("filename", this.uploadImageName); // 添加form表单中其他数据

      // console.log('file:', param.get('file'))

      // let config = {
      //   headers: {'Content-Type': 'multipart/form-data'}
      // }
      // 添加请求头
      const { data: res } = await this.$http.post(this.imageUploadUrl, param);
      if (res.meta.status != 200) {
        return;
      }
      this.uploaderCardImageFlag = true;
      this.$toast("图片上传成功");
    },

    // clearAllFormData
    clearAllFormData() {
      // 数据初始化
      this.stepNumber = 0;

      // Product Type
      this.productType = "名片";
      // Form Data
      this.body_name_card = "";
      this.cor_name_card = "";
      this.cor_addr_card = "";
      this.cor_phone_card = "";
      this.cor_email_card = "";
      this.uploadImageName = "";
      this.imageFileContent = "";

      this.imageSelectedCard = "1";
      this.imageSelectedBox = "1";
      this.imageSelectedKeyChain = "1";
      this.uploaderCardImageList = [];
      this.uploaderCardImageFlag = false;
      this.flag = false;
    },

    // caculate length
    caculateLength(content) {
      var counter = 0;
      for (var i = 0; i < content.length; i++) {
        var c = content.charAt(i);
        if (/^[\u4e00-\u9fa5]$/.test(c)) {
          counter += 2;
        } else {
          counter += 1;
        }
      }
      return counter;
    },
  },
};
</script>

<style scoped></style>
