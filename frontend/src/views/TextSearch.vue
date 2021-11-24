<template>
  <div class="TextSearch">
    <div class="row justify-center">
      <div class="col-xs-0 col-xl-2 bg-white"></div>
      <div class="col-12 col-xl-8 justify-center q-pr-md q-ma-auto">
        <el-table :data="amps" stripe style="width: 100%"
                  v-loading="isloading"
                  element-loading-text="Loading..."
                  element-loading-spinner="el-icon-loading">
          <el-table-column label="Accession" width="200">
            <template #default="props">
              <el-button @click="AMPDetail(props.row.accession)" type="text">{{ props.row.accession }}</el-button>
            </template>
          </el-table-column>
          <el-table-column label="Family" width="200">
            <template #default="props">
              <el-button @click="familyDetail(props.row.family)" type="text">{{ props.row.family }}</el-button>
            </template>
          </el-table-column>
          <el-table-column label="Peptide sequence" width="500%">
            <template #default="props">
              <pre><code><small>{{ props.row.sequence }}</small></code></pre>
            </template>
          </el-table-column>
          <el-table-column label="# smORF genes" width="150%">
            <template #default="props">
              <!--                <el-tooltip class="item" effect="dark" content="Associated number of small ORF genes." placement="right">-->
              <span>{{ props.row.metadata.info.totalItem }}</span>
              <!--                </el-tooltip>-->
            </template>
          </el-table-column>
          <el-table-column label="Tag" width="150%">
            <template #default="props">
              <el-tag :type="props.row.quality_tag.level"> {{ props.row.quality_tag.msg }} </el-tag>
              <!--                <el-tag type="warning"> {{ props.row.quality_tag.msg }} </el-tag>-->
            </template>
          </el-table-column>
        </el-table>
        <el-pagination
            @size-change="setPageSize"
            @current-change="setPage"
            :page-sizes="[20, 50, 100, 200]"
            :page-size="20"
            layout="total, sizes, prev, pager, next, jumper"
            :total="info.totalRow">
        </el-pagination>
      </div>
      <div class="col-xs-0 col-xl-2 bg-white"></div>
    </div>
<!--    <el-row>-->
<!--      <el-col :span="24">-->
<!--        <el-breadcrumb separator-class="el-icon-arrow-right">-->
<!--          <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>-->
<!--          <el-breadcrumb-item :to="{ path: '/text_search' }">Text search</el-breadcrumb-item>-->
<!--        </el-breadcrumb>-->
<!--        <br/>-->
<!--        &lt;!&ndash;    multiple filter criteria:&ndash;&gt;-->
<!--        &lt;!&ndash;    TODO https://stackoverflow.com/questions/56223664/search-multiple-fields-in-a-table-in-vue-js-with-different-v-model&ndash;&gt;-->
<!--        &lt;!&ndash;    在后端添加分页信息，读取分页信息并建立pagination。filters如何实现？&ndash;&gt;-->
<!--        &lt;!&ndash;    https://www.cxyzjd.com/article/baidu_33552969/88977014&ndash;&gt;-->
<!--      </el-col>-->
<!--    </el-row>-->
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
  name: "TextSearch",

  data() {
    return {
      query: this.$route.query.query,
      amps: [],
      axiosRefCount: 0,
      loading: false,
      info: {
        currentPage: 1,
        pageSize: 20,
        totalRow: 0,
        totalPage: 1,
      },
    }
  },
  created() {
    let self = this
    // https://stackoverflow.com/questions/50768678/axios-ajax-show-loading-when-making-ajax-request
    this.axios.interceptors.request.use((config) => {
      self.loading = true
      // trigger 'loading=true' event here
      return config;
    }, (error) => {
      self.loading = false
      // trigger 'loading=false' event here
      return Promise.reject(error);
    });
    this.axios.interceptors.response.use((response) => {
      self.loading = false
      // trigger 'loading=false' event here
      return response;
    }, (error) => {
      self.loading = false
      // trigger 'loading=false' event here
      return Promise.reject(error);
    });
  },
  mounted() {
    this.setPageSize(20)
  },
  computed: {
    isloading() {
      return this.loading
    }
  },
  methods: {
    setPage(page){
      // Important: page index starting from zero.
      this.info.currentPage = page - 1
      console.log(this.info.currentPage)
      let config = {
        params: {
          query: this.query,
          page: this.info.currentPage,
          page_size: this.info.pageSize
        }
      }
      let self = this
      this.axios.get('/search/text', config)
          .then(function (response) {
            console.log(response.data.data)
            self.amps = self.initQualityTag(response.data.data)
            self.info.totalPage = response.data.info.totalPage
            self.info.totalRow = response.data.info.totalItem
          })
          .catch(function (error) {
            console.log(error);
          })
    },
    setPageSize(size) {
      this.info.pageSize = size
      this.setPage(1)
    },
    AMPDetail(accession){
      window.open('/amp?accession='+accession, '_blank')
    },
    familyDetail(accession){
      window.open('/family?accession='+accession, '_blank')
    },
    setLoading(isLoading) {
      if (isLoading) {
        this.axiosRefCount++;
        this.loading = true;
      } else if (this.axiosRefCount > 0) {
        this.axiosRefCount--;
        this.loading = (this.axiosRefCount > 0);
      }
    },
    initQualityTag(amps){
      for (let i=0; i < amps.length; i++) {
        Object.assign(amps[i], {quality_tag: {msg: 'Not available', level: 'warning'}})
      }
      return amps
    },
  }
}
</script>

