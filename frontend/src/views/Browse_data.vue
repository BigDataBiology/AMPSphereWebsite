<template>
  <div class="BrowseData">
    <div class="row justify-center">
      <div class="col-xs-0 col-xl-2 bg-white"></div>
      <div class="col-12 col-xl-8 justify-center q-pa-auto">
        <q-expansion-item
            class="shadow-1 overflow-hidden"
            style="border-radius: 30px"
            label="Filters"
            header-class="bg-secondary text-white"
            expand-icon-class="text-white"
        >
          <q-card>
            <q-card-section>
              <div class="row justify-center q-py-md">
                <div class="col-12 col-md-2 text-bold justify-center">
                  Filter by metadata
                </div>
                <div class="col-12 col-md-2 justify-center q-pa-xs">
                  <q-select filled v-model="options.family" label="Family" @update:model-value="onFamilyChange"
                            :options="availableOptions.family" @filter="filterFamily"
                            input-debounce="0" use-input fill-input hide-selected
                            behavior="menu" align="center" clearable />
                </div>
                <div class="col-12 col-md-2 justify-center q-pa-xs">
                  <q-select filled v-model="options.habitat" label="Habitat" @update:model-value="onHabitatChange"
                            :options="availableOptions.habitat" @filter="filterHabitat"
                            input-debounce="0" use-input fill-input hide-selected
                            behavior="menu" align="center" clearable />
                </div>
                <div class="col-12 col-md-3 justify-center q-pa-xs">
                  <q-select filled v-model="options.sample" label="Sample/Progenomes2 genome" @update:model-value="onSampleChange"
                            :options="availableOptions.sample" @filter="filterSample"
                            input-debounce="0" use-input fill-input hide-selected
                            behavior="menu" align="center" clearable />
                </div>
                <div class="col-12 col-md-3 justify-center q-pa-xs">
                  <q-select filled v-model="options.microbial_source" label="Microbial source" @update:model-value="onMicrobialSourceChange"
                            :options="availableOptions.microbial_source" @filter="filterMicrobialSource"
                            input-debounce="0" use-input fill-input hide-selected
                            behavior="menu" align="center" clearable />
                </div>
              </div>
              <div class="row">
                <div class="col-12 col-md-2 justify-center text-bold q-pa-sm">Peptide length: </div>
                <div class="col-12 col-md-10 justify-center q-pa-sm">
                  <q-range v-model="options.pep_length" @change="onPepLengthChange"
                           :min="availableOptions.pep_length.min"
                           :max="availableOptions.pep_length.max" label color="secondary"/>
                </div>
                <div class="col-12 col-md-2 justify-center text-bold q-pa-sm">Molecular weight: </div>
                <div class="col-12 col-md-10 justify-center q-pa-sm">
                  <q-range v-model="options.molecular_weight" @change="onMWChange"
                           :min="availableOptions.molecular_weight.min"
                           :max="availableOptions.molecular_weight.max" label color="secondary"/>

                </div>
                <div class="col-12 col-md-2 justify-center text-bold q-pa-sm">Isoelectric point: </div>
                <div class="col-12 col-md-10 justify-center q-pa-sm">
                  <q-range v-model="options.isoelectric_point" @change="onpIChange"
                           :min="availableOptions.isoelectric_point.min"
                           :max="availableOptions.isoelectric_point.max" label color="secondary"/>
                </div>
                <div class="col-12 col-md-2 justify-center text-bold q-pa-sm">Charge at pH 7.0</div>
                <div class="col-12 col-md-10 justify-center q-pa-sm">
                  <q-range v-model="options.charge_at_pH_7" @change="onChargechange"
                           :min="availableOptions.charge_at_pH_7.min" label
                           :max="availableOptions.charge_at_pH_7.max" color="secondary"/>
                </div>
              </div>
            </q-card-section>
          </q-card>
        </q-expansion-item>
        <div class="row justify-center q-py-md">
          <div class="col-12">
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
              <el-table-column label="Quality badge" width="150%">
                <template #default="props">
<!--                  <q-badge :color="getBadgeColor(props.row.quality.badge)" :label="getBadgeLabel(props.row.quality.badge)" text-color="black"/>-->
                  <q-img :src="makeBadgeURL(props.row.quality.badge)" height="70%" fit="scale-down"></q-img>
                </template>
              </el-table-column>
            </el-table>
          </div>
        </div>
        <div class="row justify-center q-py-md">
          <div class="col-12">
            <el-pagination @size-change="setAMPsPageSize" @current-change="setAMPsPage" :page-sizes="[20, 50, 100, 200]"
                           :page-size="20" layout="sizes, pager, jumper" :total="info.totalRow">
            </el-pagination>
          </div>
        </div>
      </div>
      <div class="col-xs-0 col-xl-2 bg-white"></div>
    </div>
  </div>
</template>

<style>
.env-logos {
  width: 100%;
  height: 100px;
  background-color: #ffffff;
}
</style>

<script>
import {useQuasar} from 'quasar'


export default {
  name: "BrowseData",

  data() {
    const options_full = {
      family: [],
      habitat: [],
      sample: [],
      microbial_source: [],
      pep_length: {
        min: 8,
        max: 98
      },
      molecular_weight: {
        min: 813.0397,
        max: 12285.954999999973
      },
      isoelectric_point: {
        min: 4.0500284194946286,
        max: 11.999967765808105
      },
      charge_at_pH_7: {
        min: -56.17037696904594,
        max: 43.781710336808885
      }
    }
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
        sample: null,
        microbial_source: null,
        pep_length: {
          min: 8,
          max: 98
        },
        molecular_weight: {
          min: 813.0397,
          max: 12285.954999999973
        },
        isoelectric_point: {
          min: 4.0500284194946286,
          max: 11.999967765808105
        },
        charge_at_pH_7: {
          min: -56.17037696904594,
          max: 43.781710336808885
        }
      },
      avalOptionsFull: options_full,
      availableOptions: options_full,
    }
  },
  setup(){
    const $q = useQuasar()
    $q.notify({
      message: '<strong>Note</strong>: The filters may need tens of seconds to load. Please be patient.',
      html: true,
      color: 'primary',
      position: 'top',
      timeout: 10000,
      icon: 'announcement',
      actions: [
        { label: 'Got it', color: 'yellow', handler: () => { /* ... */ } }
      ]
    })
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
    setAMPsPage(page) {
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
          microbial_source: this.options.microbial_source,
          pep_length_interval: this.options.pep_length.min.toString() + ',' + this.options.pep_length.max.toString(),
          mw_interval: this.options.molecular_weight.min.toString() + ',' + this.options.molecular_weight.max.toString(),
          pI_interval: this.options.isoelectric_point.min.toString() + ',' + this.options.isoelectric_point.max.toString(),
          charge_interval: this.options.charge_at_pH_7.min.toString() + ',' + this.options.charge_at_pH_7.max.toString(),
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
    getAvailableOptions() {
      let self = this
      this.axios.get('/available_filters')
          .then(function (response) {
            console.log(response.data)
            self.avalOptionsFull = Object.assign({}, response.data)
            self.availableOptions = response.data
          })
          .catch(function (error) {
            console.log(error);
          })
    },
    filterFamily(val, update, abort){
      update(() => {
        val = val.toLowerCase()
        this.availableOptions.family = this.avalOptionsFull.family.filter(v => v.toLowerCase().indexOf(val) > -1)
      })
    },
    filterSample(val, update, abort){
      update(() => {
        val = val.toLowerCase()
        this.availableOptions.sample = this.avalOptionsFull.sample.filter(v => v.toLowerCase().indexOf(val) > -1)
      })
    },
    filterHabitat(val, update, abort){
      update(() => {
        val = val.toLowerCase()
        this.availableOptions.habitat = this.avalOptionsFull.habitat.filter(v => v.toLowerCase().indexOf(val) > -1)
      })
    },
    filterMicrobialSource(val, update, abort){
      update(() => {
        val = val.toLowerCase()
        this.availableOptions.microbial_source = this.avalOptionsFull.microbial_source.filter(v => v.toLowerCase().indexOf(val) > -1)
      })
    },
    onFamilyChange(option) {
      this.options.family = option;
      this.setAMPsPage(1)
    },
    onHabitatChange(option) {
      this.options.habitat = option;
      this.setAMPsPage(1)
    },
    onSampleChange(option) {
      this.options.sample = option;
      this.setAMPsPage(1)
    },
    onMicrobialSourceChange(option) {
      this.options.microbial_source = option;
      this.setAMPsPage(1)
    },
    onPepLengthChange(value) {
      // this.options.pep_length = {min: 0, max: 100}
      console.log('peplength changed.')
      this.setAMPsPage(1)
    },
    onMWChange(value) {
      // this.options.pep_length = {min: 0, max: 100}
      console.log('MW changed.')
      this.setAMPsPage(1)
    },
    onpIChange(value) {
      // this.options.pep_length = {min: 0, max: 100}
      console.log('pI changed.')
      this.setAMPsPage(1)
    },
    onChargechange(value) {
      // this.options.pep_length = {min: 0, max: 100}
      console.log('Charge changed.')
      this.setAMPsPage(1)
    },
    clearFilters() {
      this.options = {
        family: null,
        habitat: null,
        sample: null,
        microbial_source: null,
        pep_length: {
          min: 0,
          max: 100
        }
      }
    },
    initQualityTag(amps) {
      for (let i = 0; i < amps.length; i++) {
        Object.assign(amps[i], {quality_tag: {msg: 'Not available', level: 'warning'}})
      }
      return amps
    },
    getBadgeColor(quality_level){
      const color_mapping = {
        gold: 'green',
        silver: 'yellow',
        bronze: 'red'
      }
      return color_mapping[quality_level]
    },
    getBadgeLabel(quality_level){
      const quality_level_mapping = {
        gold: 'High',
        silver: 'Medium',
        bronze: 'Low'
      }
      return quality_level_mapping[quality_level]
    },
    makeBadgeURL(quality) {
      const quality_level_mapping = {
        gold: 'high',
        silver: 'medium',
        bronze: 'low'
      }
      const color_mapping = {
        gold: 'FFD700',
        silver: 'C0C0C0',
        bronze: 'CD7F32'
      }
      // const URL = 'https://badgen.net/badge/quality/' + quality_level_mapping[quality]  + '/' +
      const URL = 'https://img.shields.io/static/v1?style=flat&label=quality&color=' + color_mapping[quality] + '&message=' + quality_level_mapping[quality] + '&style=flat'
      console.log(URL)
      return URL
    },
    AMPDetail(accession) {
      window.open('/amp?accession=' + accession, '_blank')
    },
    familyDetail(accession) {
      window.open('/family?accession=' + accession, '_blank')
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

