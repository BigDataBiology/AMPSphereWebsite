<template>
  <div id="Downloads">
    <el-row>
      <el-col :span="24" :offset="0">
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/downloads' }">Downloads</el-breadcrumb-item>
        </el-breadcrumb>
        <br/>
        <div class="subsection-title">Core resources</div>.
        <el-table :data="downloadable_files" width="100%">
          <el-table-column prop="name" label="Name" width="200%"></el-table-column>
          <el-table-column label="URL" width="200%">
            <template #default="props">
              <el-link :href="props.row.file" type="primary">Download</el-link>
            </template>
          </el-table-column>
          <el-table-column prop="desc" label="Description" width="800%"></el-table-column>
        </el-table>
        <el-divider></el-divider>
<!--        <div class="subsection-title">Full AMPSphere data</div>-->
        <div style="text-align: left">
          Browse our
          <el-link href="https://zenodo.org/record/4606582#.YVLSBZ6A4_Y" type="primary">
            Zenodo page
          </el-link>
          to see all the resources.
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "Downloads",
  data () {
    return {
      downloadable_files: [
        {
          name: "AMP",
          file: "http://18.140.248.253:8080/AMP.tsv",
          desc: "All AMP families and sequences."},
        {
          name: "GMSC",
          file: "http://18.140.248.253:8080/GMSC.tsv",
          desc: "All AMP-associated smORF genes and sequences."},
        {
          name: "Metadata",
          file: "http://18.140.248.253:8080/Metadata.tsv",
          desc: "Host and taxonomic origins, associated habitats, metagenome samples and genomes."},
        {
          name: "Statistics",
          file: "http://18.140.248.253:8080/Statistics.tsv",
          desc: "Basic statistics of the AMPSphere database."}
      ]
    }
  }
}
</script>

<style scoped>

</style>