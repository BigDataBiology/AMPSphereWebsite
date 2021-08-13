<template>
  <div class="BrowseData">
    <el-row>
      <el-col :span="22" :offset="1">
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/browse_data' }">Browse data</el-breadcrumb-item>
        </el-breadcrumb>
        <br/>
        <el-tabs type="card" @tab-click="handleTabClick">
          <el-tab-pane label="AMPs">
            <el-table
                :data="AMPs_data"
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
          </el-tab-pane>
          <el-tab-pane label="Families" lazy=true>
            <el-table
                :data="families_data"
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
                  prop="num_AMPs"
                  label="Number of AMPs"
                  width="150">
              </el-table-column>
              <el-table-column
                  prop="consensus_seq"
                  label="Consensus sequence"
                  width="1080">
              </el-table-column>
            </el-table>
          </el-tab-pane>
          <el-tab-pane label="Environments">
            under developing...
          </el-tab-pane>
          <el-tab-pane label="Hosts">
            under developing...
          </el-tab-pane>
        </el-tabs>
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
      url: require('../assets/logo.png'),
      AMPs_data: [{
        accession: 'AMP10.000-000',
        family: 'SPHERE-III.000-000',
        pep_sequence: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMT',
      },{
        accession: 'AMP10.000-000',
        family: 'SPHERE-III.000-000',
        pep_sequence: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMT',
      },{
        accession: 'AMP10.000-000',
        family: 'SPHERE-III.000-000',
        pep_sequence: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMT',
      },{
        accession: 'AMP10.000-000',
        family: 'SPHERE-III.000-000',
        pep_sequence: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMT',
      },{
        accession: 'AMP10.000-000',
        family: 'SPHERE-III.000-000',
        pep_sequence: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMT',
      },{
        accession: 'AMP10.000-000',
        family: 'SPHERE-III.000-000',
        pep_sequence: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMT',
      },{
        accession: 'AMP10.000-000',
        family: 'SPHERE-III.000-000',
        pep_sequence: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMT',
      },{
        accession: 'AMP10.000-000',
        family: 'SPHERE-III.000-000',
        pep_sequence: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMT',
      },{
        accession: 'AMP10.000-000',
        family: 'SPHERE-III.000-000',
        pep_sequence: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMT',
      },{
        accession: 'AMP10.000-000',
        family: 'SPHERE-III.000-000',
        pep_sequence: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMT',
      },{
        accession: 'AMP10.000-000',
        family: 'SPHERE-III.000-000',
        pep_sequence: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMT',
      }
      ],
      families_data: [{
        accession: 'SPHERE-III.000-000',
        num_AMPs: 'nnnn',
        consensus_seq: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMTLEEIGDKFGL'
      }, {
        accession: 'SPHERE-III.000-000',
        num_AMPs: 'nnnn',
        consensus_seq: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMTLEEIGDKFGL'
      }, {
        accession: 'SPHERE-III.000-000',
        num_AMPs: 'nnnn',
        consensus_seq: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMTLEEIGDKFGL'
      }, {
        accession: 'SPHERE-III.000-000',
        num_AMPs: 'nnnn',
        consensus_seq: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMTLEEIGDKFGL'
      }, {
        accession: 'SPHERE-III.000-000',
        num_AMPs: 'nnnn',
        consensus_seq: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMTLEEIGDKFGL'
      }, {
        accession: 'SPHERE-III.000-000',
        num_AMPs: 'nnnn',
        consensus_seq: 'FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQSSFFGIGQQEMTLEEIGDKFGL'
      }],
      envs_data: [],
      hosts_data: []
    }
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

