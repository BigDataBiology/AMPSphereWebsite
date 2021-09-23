<template>
  <div id="SequenceSearch">
    <div v-if="method === 'MMseqs'">
      <el-table :data="result" stripe style="width: 100%" v-loading="loading">
        <el-table-column label="Query" prop="query_identifier"
                         :filters="queryFilters" :filter-method="filterTable">

        </el-table-column>
        <el-table-column label="Target" width="200">
          <template #default="props">
            <el-button type="text" @click="AMPDetail(props.row.target_identifier)">{{ props.row.target_identifier }}</el-button>
          </template>
        </el-table-column>
        <el-table-column label="Identity" sortable prop="sequence_identity"></el-table-column>
        <el-table-column label="Aligned length" sortable prop="alignment_length"></el-table-column>
        <el-table-column label="# mismatches" sortable prop="number_mismatches"></el-table-column>
        <el-table-column label="# gap" sortable prop="number_gap_openings"></el-table-column>
        <el-table-column label="E value" sortable prop="E_value"></el-table-column>
        <el-table-column label="Bit score" sortable prop="bit_score"></el-table-column>
      </el-table>
<!--        "query_identifier": "submitted_sequence",-->
<!--        "target_identifier": "AMP10.000_000",-->
<!--        "sequence_identity": 0.942,-->
<!--        "alignment_length": 27,-->
<!--        "number_mismatches": 2,-->
<!--        "number_gap_openings": 0,-->
<!--        "domain_start_position_query": 1,-->
<!--        "domain_end_position_query": 27,-->
<!--        "domain_start_position_target": 1,-->
<!--        "domain_end_position_target": 27,-->
<!--        "E_value": 2.42e-11,-->
<!--        "bit_score": 56-->
    </div>
    <div v-else-if="method === 'HMMER'">
      <el-table :data="result" stripe style="width: 100%" v-loading="loading">
        <el-table-column label="Query" prop="query_name" :filters="queryFilters" :filter-method="filterTable"></el-table-column>
        <el-table-column label="Target" width="200">
          <template #default="props">
            <el-button type="text" @click="familyDetail(props.row.target_name)">{{ props.row.target_name }}</el-button>
          </template>
        </el-table-column>
        <el-table-column label="Reliability" sortable prop="acc"></el-table-column>
        <el-table-column label="Bias" sortable prop="bias"></el-table-column>
        <el-table-column label="E-value" sortable prop="E_value"></el-table-column>
        <el-table-column label="C E-value" sortable prop="c_Evalue"></el-table-column>
        <el-table-column label="I E-value" sortable prop="i_Evalue"></el-table-column>
        <el-table-column label="Bit score" sortable prop="score"></el-table-column>
      </el-table>
    </div>
<!--        "query_accession": "-",-->
<!--        "query_length": 27,-->
<!--        "query_name": "SPHERE-III.001_396",-->
<!--        "target_accession": "-",-->
<!--        "target_length": 27,-->
<!--        "target_name": "submitted_sequence",-->
<!--        "E_value": 7.1e-25,-->
<!--        "acc": 0.99,-->
<!--        "bias": 9.2,-->
<!--        "c_Evalue": 7.399999999999999e-25,-->
<!--        "i_Evalue": 7.399999999999999e-25,-->
<!--        "num_domain": 1,-->
<!--        "domain_index": 1,-->
<!--        "score": 72.6,-->
<!--        "from_ali": 1,-->
<!--        "from_env": 1,-->
<!--        "from_hmm": 1,-->
<!--        "to_ali": 27,-->
<!--        "to_env": 27,-->
<!--        "to_hmm": 27,-->
<!--        "description_of_target": "-"-->
    </div>
</template>

<script>
export default {
  name: "SequenceSearch",
  data() {
    return {
      method: '',
      sequences: '',
      result: [],
      queryFilters: [],
      loading: false
    }
  },
  created(){
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
    this.getParams()
    this.search()
  },
  mounted(){

  },
  computed(){

  },
  methods: {
    getParams(){
      this.method = this.$route.query.method
      this.sequences = this.$route.query.queries
    },
    search(){
      let self = this
      let path = ''
      if (this.method === 'MMseqs') {path = '/search/mmseqs'}
      else if (this.method === 'HMMER'){path = '/search/hmmer'}
      else{path = ''}
      let config = {params: {query: this.sequences}}
      this.axios.get(path, config)
        .then(function (response) {
          console.log(response.data)
          self.result = response.data
          self.queryFilters = []
          let included = []
          for (let i = 0; i < self.result.length; i++) {
            let query
            if (self.method === 'MMseqs'){query = self.result[i].query_identifier; console.log('filter:', query)}
            else if (self.method === 'HMMER'){query = self.result[i].query_name; console.log('filter:', query)}
            else {console.log('no matching method.')}
            if (!included.includes(query)) {
              included.push(query)
              console.log('filter appended', query)
              self.queryFilters.push({text: query, value: query})
            }
          }
        })
        .catch(function (error) {
          console.log(error);
        })
    },
    updateMMseqsQueryFilters() {
      this.queryFilters = []
      let included = []
      for (let i = 0; i < this.result.length; i++) {
        let query = this.result[i].query_identifier
        console.log('filter:', query)
        if (!included.includes(query)) {
          included.push(query)
          console.log('filter appended', query)
          this.queryFilters.push({text: query, value: query})
        }
      }
    },
    updateHMMERQueryFilters() {
      this.queryFilters = []
      let included = []
      for (let i = 0; i < this.result.length; i++) {
        let query = this.result[i].query_name
        console.log('filter:', query)
        if (!included.includes(query)) {
          included.push(query)
          console.log('filter appended', query)
          this.queryFilters.push({text: query, value: query})
        }
      }
    },
    filterTable(value, row, column) {
      const property = column['property']
      return row[property] === value
    },
    AMPDetail(accession){
      window.open('/amp?accession='+accession, '_blank')
    },
    familyDetail(accession){
      window.open('/family?accession='+accession, '_blank')

    }
  }
}
</script>

<style scoped>

</style>