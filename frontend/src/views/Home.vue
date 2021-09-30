<template>
    <div class="Home">
      <el-row justify="center" align="middle">
        <el-col :span="14" :offset="1" type="flex" justify="middle">
          <div style="font-size: 150%; text-align: center">Browse by data type</div>
        </el-col>
        <el-col :span="7" :offset="1" type="flex" justify="middle">
          <div style="font-size: 150%; text-align: center">Search by sequence</div>
        </el-col>
      </el-row>
      <el-row>
        <br/>
      </el-row>
      <el-row>
        <el-col :span="14" :offset="1">
          <el-row>
<!--            This is AMPSphere, a database of prokaryotic AMP sequences predicted from thousands of genomes and metagenomes.-->
<!--            The almost 1 M candidate AMP sequences available here are distributed as follows:-->
<!--            <br/>-->
<!--            <br/>-->
            <el-col :span="7">
              <el-table :data="distributionData.amps_families" style="width: 120%" :show-header="false">
                <el-table-column prop="number" label="Number">
                  <template #default="props">
                    <el-link href="/browse_data" type="primary" style="font-size: medium"> {{ props.row.number }} </el-link>
                  </template>
                </el-table-column>
                <el-table-column prop="type" label="Type"> </el-table-column>
              </el-table>
            </el-col>
            <el-col :span="7" :offset="1">
<!--              <h4>Derived from</h4>-->
              <el-table :data="distributionData.genomes_metagenomes" style="width: 120%" :show-header="false">
                <el-table-column prop="number" label="Number">
                  <template #default="props">
                    <el-link href="/browse_data" type="primary" style="font-size: medium"> {{ props.row.number }} </el-link>
                  </template>
                </el-table-column>
                <el-table-column prop="type" label="Type"> </el-table-column>
              </el-table>
            </el-col>
            <el-col :span="7" :offset="1">
              <el-table :data="distributionData.habitats_hosts" style="width: 120%" :show-header="false">
                <el-table-column prop="number" label="Number">
                  <template #default="props">
                    <el-link href="/browse_data" type="primary" style="font-size: medium"> {{ props.row.number }} </el-link>
                  </template>
                </el-table-column>
                <el-table-column prop="type" label="Type"> </el-table-column>
              </el-table>
            </el-col>
<!--            <el-image></el-image>-->
<!--            <el-image :src="geoDistribution">-->
<!--            </el-image>-->
<!--            <el-image :src="habitatDistribution">-->
<!--            </el-image>-->
<!--            <el-image :src="hostDistribution">-->
<!--            </el-image>-->
            <el-col>
              <el-carousel :interval="5000" height="500px" :autoplay="true">
                <el-carousel-item v-for="graph in distributioinGraphs" :key="graph">
                  <!--                <h3>{{ graph.type }}</h3>-->
                  <el-image :src="graph.image" fit="scale-down"></el-image>
                </el-carousel-item>
              </el-carousel>
            </el-col>
          </el-row>
        </el-col>
        <el-col :span="7" :offset="1" type="flex" justify="middle">
          <el-row>
            <div style="text-align: left">
              Paste (&leq; 10) peptide sequences here (fasta format). <br/><br/>
              <el-input
                  type="textarea"
                  :rows="20"
                  :autosize="{ minRows: 15, maxRows: 20}"
                  :placeholder="exampleSequences"
                  v-model="sequences">
              </el-input>
            </div>
            <br/>
<!--            <div style="text-align: left">-->
<!--              Or upload a file (amino acid sequences, size &lt; 50kb)-->
<!--              <br/><br/>-->
<!--              <el-upload-->
<!--                  class="upload-demo"-->
<!--                  drag-->
<!--                  action="https://jsonplaceholder.typicode.com/posts/"-->
<!--                  :on-preview="handlePreview"-->
<!--                  :on-remove="handleRemove"-->
<!--                  :file-list="fileList"-->
<!--                  multiple-->
<!--              >-->
<!--                <i class="el-icon-upload"></i>-->
<!--                <div class="el-upload__text">Drop file here or <em>click to upload</em></div>-->
<!--              </el-upload>-->
<!--&lt;!&ndash;              <el-upload&ndash;&gt;-->
<!--&lt;!&ndash;                action="https://jsonplaceholder.typicode.com/posts/"&ndash;&gt;-->
<!--&lt;!&ndash;                :limit="1"&ndash;&gt;-->
<!--&lt;!&ndash;                :file-list="fastaFile"&ndash;&gt;-->
<!--&lt;!&ndash;                style="text-align: left"&ndash;&gt;-->
<!--&lt;!&ndash;            >&ndash;&gt;-->
<!--&lt;!&ndash;              <el-button size="small" type="primary">Upload a fasta file</el-button>&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;              <template #tip>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;                <div class="el-upload__tip"></div>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;              </template>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            </el-upload>&ndash;&gt;-->
<!--            </div>-->
          </el-row>
          <el-row>
            <!--                TODO FIXME-->
            <el-radio v-model="searchMethod" label="MMseqs">MMseqs</el-radio>
            <el-radio v-model="searchMethod" label="HMMER">HMMSearch</el-radio>
            <el-button type="primary"
                       icon="el-icon-search"
                       @click="sequenceSearch">
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
        statistics: {
          num_amps: 863498,
          num_families: 8535,
          num_genomes: 49757,
          num_habitats: 57,
          num_hosts: 195,
          num_metagenomes: 61393
        },
        distributionData: {
          amps_families: [
            {number: (863498).toLocaleString('en-US'), type: 'AMPs'},
            {number: (8535).toLocaleString('en-US'), type: 'families'},
          ],
          genomes_metagenomes: [
            {number: (49757).toLocaleString('en-US'), type: 'genomes'},
            {number: (61393).toLocaleString('en-US'), type: 'metagenomes'}
          ],
          habitats_hosts: [
            {number: (57).toLocaleString('en-US'), type: 'habitats'},
            {number: (195).toLocaleString('en-US'), type: 'hosts'},
          ]
        },
        geoDistribution: require('../assets/geoDistribution.svg'),
        hostDistribution: require('../assets/hostDistribution.svg'),
        habitatDistribution: require('../assets/habitatDistribution.svg'),
        distributioinGraphs: [
          {type: 'geography', image: require('../assets/geoDistribution.svg')},
          {type: 'host', image: require('../assets/hostDistribution.svg')},
          {type: 'habitat', image: require('../assets/habitatDistribution.svg')},
        ],
        exampleSequences:
            ">AMP10.000_002 | SPHERE-III.010_054\n" +
            "KRVKSFFKGYMRAIEINAALMYGYRPK\n" +
            ">AMP10.000_003 | SPHERE-III.001_008\n" +
            "GRVIGKQGRIAKAIRVVMRAAAVRVDEKVLVEID\n",
        searchMethod: 'MMseqs',
        sequences: '',
        // fastaFile: [],
      }
    },
    mounted () {
        this.retrieveStatistics()
    },
    methods: {
      handleFamilyDetail(accession){
        console.log('goto', '/family?accession='+accession)
        window.open('/family?accession='+accession, '_blank')
      },
      handleBrowse(by){
        window.open('/browse_data?by='+by, '_blank')
      },
      retrieveStatistics() {
        var self = this
        this.axios.get('/statistics', {})
          .then(function (response) {
            console.log(response.data)
            self.statistics = response.data;
            self.distributionData = {
              amps_families: [
                {number: self.statistics.num_amps.toLocaleString('en-US'), type: 'AMPs'},
                {number: self.statistics.num_families.toLocaleString('en-US'), type: 'families'},
              ],
              genomes_metagenomes: [
                {number: self.statistics.num_genomes.toLocaleString('en-US'), type: 'genomes'},
                {number: self.statistics.num_metagenomes.toLocaleString('en-US'), type: 'metagenomes'}
              ],
              habitats_hosts: [
                {number: self.statistics.num_habitats.toLocaleString('en-US'), type: 'habitats'},
                {number: self.statistics.num_hosts.toLocaleString('en-US'), type: 'hosts'},
              ]
            }
          })
          .catch(function (error) {
            console.log(error);
          });
      },
      sequenceSearch(){
        if ((this.sequences.match(/\n/g) || '').length + 1 > 20){
          this.$message('Please input no more than 10 sequences.')
        } else {
          if (this.sequences === ''){
            window.open(
                encodeURI('/sequence_search?method=' + this.searchMethod + '&queries=' + this.exampleSequences),
                '_blank')
          }
          else{
            window.open(
                encodeURI('/sequence_search?method=' + this.searchMethod + '&queries=' + this.sequences),
                '_blank')
          }
        }
      }
    }
  }
</script>
