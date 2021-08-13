<template>
  <div id="Tools">
    <el-row>
      <el-col :span="22" :offset="1">
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/tools' }">Tools</el-breadcrumb-item>
        </el-breadcrumb>
        <br/>
        <el-tabs type="card" @tab-click="handleTabClick">
          <el-tab-pane label="Macrel">
            under developing...
          </el-tab-pane>
          <el-tab-pane label="HMM search">
            under developing...
          </el-tab-pane>
          <el-tab-pane label="MMseqs">
            under developing...
          </el-tab-pane>
        </el-tabs>

      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "Tools",

  methods: {
    handleTabClick(tab, event) {
      console.log(tab, event);
    },
  }
}
</script>

<style scoped>

</style>