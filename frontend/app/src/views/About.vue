<template>
<div id="About">
  <el-row>
    <el-col :span="22" :offset="1">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/about' }">About</el-breadcrumb-item>
      </el-breadcrumb>
      <br/>
      <el-row>
        <el-table :data="dataStatsExamples">
          <el-table-column
              prop="type"
              label="Type"
              width="150">
          </el-table-column>
          <el-table-column
              label="Number of AMPs"
              width="150">
            <template #default="props">
              <el-button @click="handleBrowse(props.row.type)" type="text" size="small">
                {{ props.row.num_AMPs }}
              </el-button>
            </template>
          </el-table-column>
          <el-table-column
              prop="example"
              label="Example"
              width="300">
          </el-table-column>
        </el-table>
      </el-row>
    </el-col>
  </el-row>
</div>
</template>

<script>
export default {
  name: "About",
}
</script>

<style scoped>

</style>