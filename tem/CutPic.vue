<template>
  <div>
    CutPicture

    <van-uploader
      v-model="uploaderCardImageList"
      :max-count="1"
      deletable
      :after-read="imageUploderCard"
    />

    <van-popup v-model="showCutWindowFlag">
      <div class="rc-cropper-one" v-if="data.src">
        <van-row>
          <van-col :span="12">
            <div class="rc-cropper__canvasCrop">
              <canvas
                :id="data.src"
                ref="canvas"
                width="350"
                height="500"
              ></canvas>
              <div class="rc-cropper__iconCropOne"></div>
            </div>
          </van-col>
          <!-- <van-col :span="11" :offset="1">
                <img :src="cropImg" alt="裁剪后图片" />
              </van-col> -->
        </van-row>
        <van-row>
          <van-col
            ><van-button
              type="success"
              size="small"
              @click="initCropper()"
              :disabled="croppShow"
              >裁剪</van-button
            ></van-col
          >
          <van-col
            ><van-button
              type="danger"
              size="small"
              @click="cancelCropper()"
              v-if="cropper"
              ><van-icon name="cross"/></van-button
          ></van-col>
        </van-row>
      </div>
    </van-popup>

    <van-butto @click="uploadImage">上传</van-butto>
  </div>
</template>

<script>
import Cropper from "cropperjs";
import "cropperjs/dist/cropper.min.css";
export default {
  name: "cropper",

  data() {
    return {
      uploaderCardImageList: [],
      cropper: null,
      croppShow: false,
      cropImg: "",
      showCutWindowFlag: false,
      user_openid: "openid",
      data: {
        src: require("../assets/testCut.png"),
      },
    };
  },

  mounted() {
    this.drawImg();
  },

  methods: {
    // 用户上传图片
    imageUploderCard(file) {
      var myDate = new Date();
      var timeStampString = String(myDate.getTime());

      this.data.src = file.content;

      this.imageFileContent = file.content;
      this.uploadImageName = timeStampString + this.user_openid;
      console.log(this.uploadImageName);

      // 上传
      let param = new FormData(); // 创建form对象
      param.append("file", this.imageFileContent); // 通过append向form对象添加数据
      param.append("filename", this.uploadImageName); // 添加form表单中其他数据

      // 添加请求头
      //   const { data: res } = await this.$http.post(this.imageUploadUrl, param);
      //   if (res.meta.status != 200) {
      //     return;
      //   }
      this.uploaderCardImageFlag = true;
      this.$toast("图片上传成功");

      this.drawImg();
      //   this.initCropper();
      this.showCutWindowFlag = true;
    },
    // 在canvas上绘制图片
    drawImg(href) {
      this.$nextTick(() => {
        let canvas = document.getElementById(this.data.src);
        if (canvas) {
          canvas.width = 300;
          canvas.height = 300;
          let ctx = canvas.getContext("2d");
          ctx.clearRect(0, 0, canvas.width, canvas.height);
          let img = new Image();
          img.crossOrigin = "Anonymous";
          img.src = href || this.data.src;
          img.onload = function() {
            ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
          };
        }
      });
    },
    // 显示裁剪框
    initCropper() {
      let _this = this;
      this.drawImg();
      this.croppShow = true;
      let cropper = new Cropper(this.$refs.canvas, {
        checkCrossOrigin: true,
        viewMode: 2,
        aspectRatio: 1 / 1,
        crop() {
          _this.sureCropper();
        },
      });
      this.cropper = cropper;
    },
    // 确认裁剪
    sureCropper() {
      let _this = this;
      this.cropper.getCroppedCanvas().toBlob(function(blob) {
        const href = window.URL.createObjectURL(blob);
        _this.cropImg = href;
      }, "image/jpeg");
    },
    // 销毁裁剪框
    cancelCropper() {
      this.cropper.destroy();
      this.croppShow = false;
      this.cropper = null;
    },

    // 上传图片
    async uploadImage() {
      const { data: res } = await this.$http.post(
        "http://localhost:8181/image",
        { fileContent: this.cropImg }
      );

      if (res.status != 200) {this.$toast('failed...'); return;}

      this.$toast('succeed...')
    },
  },
};
</script>

<style scoped>
.rc-cropper-one {
  position: relative;
}

img {
  width: 100%;
  height: 100%;
}

.rc-cropper__canvasCrop {
  width: 300px;
  height: 300px;
}

.rc-cropper__iconCropOne {
  position: absolute;
  left: 44%;
  top: 4%;
}

.van-button {
  margin: 20px 0;
  display: block;
  z-index: 10000;
}
</style>
