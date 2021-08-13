<template>
    <div class="Home">
      <el-row>
        <br/>
      </el-row>
<!--      <el-row>-->
<!--        <h3 style="text-align: center">Please cite</h3>-->
<!--        <el-col offset="1" :span="10">-->
<!--          <div>-->
<!--          For AMPSphere current version (<a href="https://doi.org/10.5281/zenodo.4606582">v.2021-08</a>), please cite:-->
<!--          </div>-->
<!--          <pre><code>-->
<!--          Santos-Júnior, Célio D.; Schmidt, Thomas S.B.;-->
<!--          Fullam, Anthony; Duan, Yiqian; Hui, Chong; Bork, Peer;-->
<!--          Zhao, Xing-Ming &amp; Coelho, Luis Pedro. (2021).-->
<!--          AMPSphere : the worldwide survey of prokaryotic-->
<!--          antimicrobial peptides (Version v.2021-08) [Data set].-->
<!--          Zenodo. DOI: 10.5281/zenodo.4606582-->
<!--        </code></pre>-->
<!--        </el-col>-->
<!--        <el-col offset="1" span="10">-->
<!--          <p>In case you also used <a href="http://big-data-biology.org/software/macrel/">Macrel</a> tool, please cite:</p>-->
<!--          <pre><code>-->
<!--          Santos-Júnior CD, Pan S, Zhao X, Coelho LP. 2020.-->
<!--          Macrel: antimicrobial peptide screening in genomes-->
<!--          and metagenomes. PeerJ 8:e10555.-->
<!--          DOI: 10.7717/peerj.10555-->
<!--          </code></pre>-->
<!--        </el-col>-->
<!--      </el-row>-->
      <el-row justify="center" align="middle">
        <el-col :span="10" type="flex" justify="middle">
          <div style="font-size: 150%; text-align: center">Browse by</div>
        </el-col>
        <el-col :span="10" :offset="2" type="flex" justify="middle">
          <div style="font-size: 150%; text-align: center">Search by sequence</div>
        </el-col>
      </el-row>
      <el-row>
        <br/>
      </el-row>
      <el-row>
        <el-col :span="10" :offset="1">
          <el-row>
<!--            <el-col :span="2">-->
<!--              <img src="./../assets/logo/B-DNA.svg" style="width: 15px; height: 50px"/>-->
<!--            </el-col>-->
            This is AMPSphere, a database of prokaryotic AMP sequences predicted from thousands of genomes and metagenomes.
            The almost 1 M candidate AMP sequences available here are distributed as follows:
            <br/>
            <br/>
            <el-col :span="10">
<!--              <h4>Derived from</h4>-->
<!--              genomes and metagenomes aligned to the left, numbers aligned to the right.-->
              <el-descriptions column="1" border="border">
                <el-descriptions-item label="Genomes: ">
                  {{ dataStats.Genomes }}
                </el-descriptions-item>
                <el-descriptions-item label="Metagenomes: ">
                  {{ dataStats.Metagenomes }}
                </el-descriptions-item>
              </el-descriptions>
            </el-col>
            <el-col :span="10" :offset="4">
              <el-descriptions column="1" border="border">
                <el-descriptions-item label="AMPs">
                  {{ dataStats.AMPs }}
                </el-descriptions-item>
                <el-descriptions-item label="Families">
                  {{ dataStats.Families }}
                </el-descriptions-item>
                <el-descriptions-item label="Environments">
                  {{ dataStats.Environments }}
                </el-descriptions-item>
                <el-descriptions-item label="Hosts">
                  {{ dataStats.Hosts }}
                </el-descriptions-item>
              </el-descriptions>
            </el-col>
<!--            <el-table :data="dataStatsExamples">-->
<!--              <el-table-column-->
<!--                  prop="type"-->
<!--                  label="Type"-->
<!--                  width="150">-->
<!--              </el-table-column>-->
<!--              <el-table-column-->
<!--                  label="Number of AMPs"-->
<!--                  width="150">-->
<!--                <template #default="props">-->
<!--                  <el-button @click="handleBrowse(props.row.type)" type="text" size="small">-->
<!--                    {{ props.row.num_AMPs }}-->
<!--                  </el-button>-->
<!--                </template>-->
<!--              </el-table-column>-->
<!--              <el-table-column-->
<!--                  prop="example"-->
<!--                  label="Example"-->
<!--                  width="300">-->
<!--              </el-table-column>-->
<!--            </el-table>-->
          </el-row>
        </el-col>
        <el-col :span="10" :offset="2" type="flex" justify="middle">
          <el-row>
            <div style="line-height: 100px;">
              <el-input
                  type="textarea"
                  :autosize="{ minRows: 8, maxRows: 20}"
                  placeholder="e.g. FFGIGQQEMTLEEIGDKFGLTRERVRQIKEKAIRRLRQS"
                  v-model="text">
              </el-input>
            </div>
          </el-row>
          <el-row>
            <el-radio v-model="searchMethod" label="MMseqs">MMseqs</el-radio>
            <el-radio v-model="searchMethod" label="HMMSearch">HMMSearch</el-radio>
            <el-button type="primary"
                       icon="el-icon-search">
              Search
            </el-button>
          </el-row>
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
        name: 'Home',
      data() {
        return {
          searchMethod: 'MMseqs',
          dataStats: {
            Genomes: '5149 (example data)',
            Metagenomes: '1M (example data)',
            AMPs: '1M (example data)',
            Families: '3555 (example data)',
            Hosts: '30 (example data)',
            Environments: '128 (example data)',
          },
        }
      },
      methods: {
        handleFamilyDetail(accession){
          console.log('goto', '/family?accession='+accession)
          window.open('/family?accession='+accession, '_blank')
        },
        handleBrowse(by){
          window.open('/browse_data?by='+by, '_blank')
        }
      }
    }
</script>
