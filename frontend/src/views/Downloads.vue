<template>
  <div id="Downloads">
    <div class="row justify-center">
      <div class="col-xs-0 col-xl-2 bg-white"></div>
      <div class="col-12 col-xl-8 justify-center q-pr-md q-ma-auto">
        <div class="subsection-title">Core resources</div>.
        <el-table :data="downloadable_files" width="100%">
          <el-table-column prop="name" label="Name" width="200%"></el-table-column>
          <el-table-column prop="type" label="Type" width="150%"></el-table-column>
          <el-table-column label="URL" width="150%">
            <template #default="props">
              <el-link :href="props.row.file" type="primary">Download</el-link>
            </template>
          </el-table-column>
          <el-table-column prop="desc" label="Description" width="700%"></el-table-column>
        </el-table>
        <el-divider></el-divider>
<!--        <div class="subsection-title">Full AMPSphere data</div>-->
        <div style="text-align: left">
          Browse our
          <el-link href="https://doi.org/10.5281/zenodo.4574468" type="primary">
            Zenodo page
          </el-link>
          to see all the resources.
        </div>
      </div>
      <div class="col-xs-0 col-xl-2 bg-white"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Downloads",
  data () {
    return {
      downloadable_files: [
        {
          name: 'AMPSphere database',
          type: 'Full database',
          file: "http://18.140.248.253:443/v1/downloads/main_db",
          desc: "Full sqlite3 database containing all individual tables below.",
        },
        {
          name: "AMP",
          type: "Individual table",
          file: "http://18.140.248.253:443/v1/downloads/tables:AMP",
          desc: "All AMP families and sequences."
        },
        {
          name: "GMSC",
          type: "Individual table",
          file: "http://18.140.248.253:443/v1/downloads/tables:GMSC",
          desc: "All AMP-associated smORF genes and sequences."
        },
        {
          name: "Metadata",
          type: "Individual table",
          file: "http://18.140.248.253:443/v1/downloads/tables:Metadata",
          desc: "Host and taxonomic origins, associated habitats, metagenome samples and genomes."},
        {
          name: "Statistics",
          type: "Individual table",
          file: "http://18.140.248.253:443/v1/downloads/tables:Statistics",
          desc: "Basic statistics of the AMPSphere database."
        },
        {
          name: "MMseqs database",
          type: "Search database",
          file: "http://18.140.248.253:443/v1/downloads/search_db:mmseqs",
          desc: 'Search database for offline or large scale query, can be directly used by the MMseqs software.'
        },
        {
          name: "HMM profile database",
          type: "Search database",
          file: "http://18.140.248.253:443/v1/downloads/search_db:hmmer",
          desc: 'Search database for offline or large scale query, can be directly used by the HMMER software.'
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>