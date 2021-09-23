<template>
  <div class="BrowseData">
    <el-row>
      <el-col :span="24">
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/browse_data' }">Browse data</el-breadcrumb-item>
        </el-breadcrumb>
        <br/>
<!--    multiple filter criteria:-->
<!--    TODO https://stackoverflow.com/questions/56223664/search-multiple-fields-in-a-table-in-vue-js-with-different-v-model-->
<!--    在后端添加分页信息，读取分页信息并建立pagination。filters如何实现？-->
<!--    https://www.cxyzjd.com/article/baidu_33552969/88977014-->
        <span>
          Select filters:
          <el-select v-model="options.family" filterable clearable placeholder="Family"
                     @change="onFamilyChange" size="mini"
                     v-loading="isloading" element-loading-spinner="el-icon-loading">
            <el-option v-for="item in availableOptions.family" :label="item" :value="item" :key="item"></el-option>
          </el-select>
          <el-select v-model="options.habitat" filterable clearable placeholder="Habitat"
                     @change="onHabitatChange" size="mini"
                     v-loading="isloading" element-loading-spinner="el-icon-loading">
            <el-option v-for="item in availableOptions.habitat" :label="item" :value="item" :key="item"></el-option>
          </el-select>
          <el-select v-model="options.host" filterable clearable placeholder="Host"
                     @change="onHostChange" size="mini"
                     v-loading="isloading" element-loading-spinner="el-icon-loading">
            <el-option v-for="item in availableOptions.host" :label="item" :value="item" :key="item"></el-option>
          </el-select>
<!--          TODO MEDIUM PRIORITY: change this filter into peptide length-->
          <el-select v-model="options.sample" filterable clearable placeholder="Sample"
                     @change="onSampleChange" size="mini"
                     v-loading="isloading" element-loading-spinner="el-icon-loading">
            <el-option v-for="item in availableOptions.sample" :label="item" :value="item" :key="item"></el-option>
          </el-select>
          <el-select v-model="options.origin" filterable clearable placeholder="Origin"
                     @change="onOriginChange" size="mini"
                     v-loading="isloading" element-loading-spinner="el-icon-loading">
            <el-option v-for="item in availableOptions.origin" :label="item" :value="item" :key="item"></el-option>
          </el-select>
<!--          <el-button @click="clearFilters" type="primary"><span>Clear</span></el-button>-->
          </span>
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
            @size-change="setAMPsPageSize"
            @current-change="setAMPsPage"
            :page-sizes="[20, 50, 100, 200]"
            :page-size="20"
            layout="total, sizes, prev, pager, next, jumper"
            :total="info.totalRow"
        >
        </el-pagination>
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
      axiosRefCount: 0,
      loading: false,
      info: {
        currentPage: 1,
        pageSize: 20,
        totalRow: 0,
        totalPage: 1,
      },
      options: {
        family: null,
        habitat: null,
        host: null,
        sample: null,
        origin: null,
      },
      availableOptions: {
        family: [],
        habitat: [],
        host: [],
        sample: [],
        origin: [],
      }
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
    this.setAMPsPageSize(20)
    this.getAvailableOptions()
  },
  computed: {
    isloading() {
      return this.loading
    }
  },
  methods: {
    setAMPsPage(page){
      // this.$message('setting to ' + page + 'th page')
      // Important: page index starting from zero.
      this.info.currentPage = page - 1
      console.log(this.info.currentPage)
      let config = {
        params: {
          family: this.options.family,
          habitat: this.options.habitat,
          host: this.options.host,
          sample: this.options.sample,
          origin: this.options.origin,
          page: this.info.currentPage,
          page_size: this.info.pageSize
        }
      }
      let self = this
      this.axios.get('/amps', config)
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
    setAMPsPageSize(size) {
      this.info.pageSize = size
      this.setAMPsPage(1)
    },
    getAvailableOptions(){
      let self = this
      this.axios.get('/available_filters')
        .then(function (response) {
          console.log(response.data)
          self.availableOptions = response.data
        })
        .catch(function (error) {
          console.log(error);
        })
    },
    onFamilyChange(option) { this.options.family = option; this.setAMPsPage(1) },
    onHabitatChange(option) { this.options.habitat = option; this.setAMPsPage(1) },
    onHostChange(option) { this.options.host = option; this.setAMPsPage(1) },
    onSampleChange(option) { this.options.sample = option; this.setAMPsPage(1) },
    onOriginChange(option) { this.options.origin = option; this.setAMPsPage(1) },
    clearFilters() {
      this.options = {
        family: null,
        habitat: null,
        host: null,
        sample: null,
        origin: null,
      }
    },
    initQualityTag(amps){
      for (let i=0; i < amps.length; i++) {
        Object.assign(amps[i], {quality_tag: {msg: 'Not available', level: 'warning'}})
      }
      return amps
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
    }
  }
}
</script>

