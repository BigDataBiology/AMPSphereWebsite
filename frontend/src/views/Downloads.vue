<template>
  <div id="Downloads">
    <el-row>
      <el-col :span="22" :offset="1">
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/downloads' }">Downloads</el-breadcrumb-item>
        </el-breadcrumb>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "Downloads"
}
</script>

<style scoped>

</style>