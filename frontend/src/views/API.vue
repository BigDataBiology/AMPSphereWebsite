<template>
  <div id="API">
    <div class="row justify-center">
      <div class="col-xs-0 col-lg-2 bg-white"></div>
      <div class="col-12 col-lg-8 justify-center q-pr-md q-ma-auto">
        <json-viewer :value="briefAPI" expand-depth="5" boxed expanded style="alignment: left; text-align: left"/>
      </div>
      <div class="col-xs-0 col-lg-2 bg-white"></div>
    </div>
<!--    <div class="row">-->
<!--      <el-col :span="22" :offset="1">-->
<!--        <el-breadcrumb separator-class="el-icon-arrow-right">-->
<!--          <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>-->
<!--          <el-breadcrumb-item :to="{ path: '/api' }">API</el-breadcrumb-item>-->
<!--        </el-breadcrumb>-->
<!--        <pre class="preview pre"></pre>-->
<!--        <div>-->
<!--        </div>-->
<!--      </el-col>-->
<!--    </div>-->
  </div>
</template>

<script>
export default {
  name: "API",
  data (){
    return {
      urlPrefix: "http://18.140.248.253:443/v1/",
    }
  },
  computed: {
    briefAPI () {
      return {
        data: {
          Browse: {
            "Statistics": {
              url: this.urlPrefix + "statistics",
              example: this.urlPrefix + "statistics"},
            "AMPs": {
              url: this.urlPrefix + "amps",
              example: this.urlPrefix + "amps" + "?page_size=5&page=0"},
            "Families": {
              url: this.urlPrefix + "families",
              example: this.urlPrefix + "families" + "?page_size=5&page=0"},
          },
          Retrieve: {
            "AMP": {
              url: this.urlPrefix + "amps/{accession}",
              example: this.urlPrefix + "amps/AMP10.000_000"},
            "Family": {
              url: this.urlPrefix + "families/{accession}",
              example: this.urlPrefix + "families/SPHERE-III.000_000"},
            "AMP features": {
              url: this.urlPrefix + "amps/{accession}/features",
              example: this.urlPrefix + "amps/AMP10.000_000/features"},
            "AMP metadata": {
              url: this.urlPrefix + "amps/{accession}/metadata",
              example: this.urlPrefix + "amps/AMP10.000_000/metadata"},
            "Family features": {
              url: this.urlPrefix + "families/{accession}/features",
              example: this.urlPrefix + "families/SPHERE-III.000_000/features"
            }
          },
          // Search: {
          //   "Text search": {
          //     url: this.urlPrefix + "search/text",
          //     example: this.urlPrefix + "search/text?query=aquatic"},
          //   "mmSeqs search": {
          //     url: this.urlPrefix + "search/mmseqs",
          //     // example: this.urlPrefix + "search/mmseqs"},
          //   "HMMER search": {
          //     url: this.urlPrefix + "search/hmmer",
          //     // example: this.urlPrefix + "search/hmmer"},
          // }
      }
      }
    }
  },
  methods: {
  }
}


</script>

<style scoped>

</style>