<template>
  <div class="BrowseData">
    <el-row>
      <el-col :span="22" :offset="1">
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/browse_data' }">Browse data</el-breadcrumb-item>
        </el-breadcrumb>
        <br/>
<!--    multiple filter criteria:-->
<!--    TODO https://stackoverflow.com/questions/56223664/search-multiple-fields-in-a-table-in-vue-js-with-different-v-model-->
<!--    在后端添加分页信息，读取分页信息并建立pagination。filters如何实现？-->
<!--    https://www.cxyzjd.com/article/baidu_33552969/88977014-->
          <el-table
              :data="amps"
              stripe
              style="width: 100%">
            <el-table-column
                label="Accession"
                width="150">
              <template #default="props">
                <el-button @click="handleFamilyDetail(props.row.accession)" type="text" size="small">
                  {{ props.row.accession }}
                </el-button>
              </template>
            </el-table-column>
            <el-table-column
                label="Family"
                width="150">
              <template #default="props">
                <el-button @click="handleFamilyDetail(props.row.family)" type="text" size="small">
                  {{ props.row.family }}
                </el-button>
              </template>
            </el-table-column>
            <el-table-column
                prop="pep_sequence"
                label="Peptide sequence"
                width="1080">
            </el-table-column>
          </el-table>
      </el-col>
      <el-col :span="11">
      </el-col>
    </el-row>

  </div>
</template>

<style>
.env-logos{
  width: 100%;
  height: 100px;
  background-color: #ffffff;
}
</style>

<script>
export default {
  name: "BrowseData",

  data() {
    return {
      amps: [],
      info: {
        currentPage: 1,
        pageSize: 20,
        totalItem: 0,
        totalPage: 1,
      },
      filters: {
        family: null,
        habitat: null,
        host: null,
        sample: null,
        origin: null,
      }
    }
  },
  created() {

  },
  mounted() {
    this.axios.get('/').then(function (response) {
      if (response.status === 200) {
        console.log('xxx')
      }
    }).catch(function (error) {
      console.log(error);
    });
  },
  computed(){

  },
  methods: {
    handleTabClick(tab, event) {
      console.log(tab, event);
    },
    handleFamilyDetail(accession){
      console.log('goto', '/family?accession='+accession)
      window.open('/family?accession='+accession, '_blank')
    }
  }
}
</script>

