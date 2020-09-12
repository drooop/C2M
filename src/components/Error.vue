<template>
  <div>
    <p>you are not allowed to be here...</p>
    <van-uploader
      v-model="uploaderCardImageList"
      :max-count="1"
      :after-read="imageUploderCard"
      width="10rem"
      height="10rem"
      image-fit="none"
    />
  </div>
</template>

<script>
export default {
  data() {
    return {
      pickup_code: 0,
      uploaderCardImageList: [],
    };
  },

  methods: {
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
      this.$toast("图片上传成功");
    },
  },
};
</script>

<style></style>
