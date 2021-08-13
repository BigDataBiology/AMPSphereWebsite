<template>
  <div id="API">
    <el-row>
      <el-col :span="22" :offset="1">
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/api' }">API</el-breadcrumb-item>
        </el-breadcrumb>
        <pre class="preview pre"></pre>
        <textarea class="textarea"></textarea>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "API",
  methods: {
  }
}


</script>

<style scoped>

</style>