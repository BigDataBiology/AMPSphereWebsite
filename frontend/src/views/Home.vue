<template>
    <div class="Home">
      <el-row justify="center" align="middle">
        <el-col :span="11" type="flex" justify="middle">
          <div style="font-size: 150%; text-align: center">Browse by data type</div>
        </el-col>
        <el-col :span="11" :offset="0" type="flex" justify="middle">
          <div style="font-size: 150%; text-align: center">Search by sequence</div>
        </el-col>
      </el-row>
      <el-row>
        <br/>
      </el-row>
      <el-row>
        <el-col :span="10" :offset="1">
          <el-row>
<!--            This is AMPSphere, a database of prokaryotic AMP sequences predicted from thousands of genomes and metagenomes.-->
<!--            The almost 1 M candidate AMP sequences available here are distributed as follows:-->
<!--            <br/>-->
<!--            <br/>-->
            <el-col :span="8">
              <el-table :data="distributionData.amps_families" style="width: 100%" :show-header="false">
                <el-table-column prop="number" label="Number" width="80">
                  <template #default="props">
                    <el-link href="/browse_data" type="primary"> {{ props.row.number }} </el-link>
                  </template>
                </el-table-column>
                <el-table-column prop="type" label="Type" width="80"> </el-table-column>
              </el-table>
            </el-col>
            <el-col :span="8" :offset="0">
<!--              <h4>Derived from</h4>-->
              <el-table :data="distributionData.genomes_metagenomes" style="width: 100%" :show-header="false">
                <el-table-column prop="number" label="Number" width="60">
                  <template #default="props">
                    <el-link href="/browse_data" type="primary"> {{ props.row.number }} </el-link>
                  </template>
                </el-table-column>
                <el-table-column prop="type" label="Type" width="100"> </el-table-column>
              </el-table>
            </el-col>
            <el-col :span="8" :offset="0">
              <el-table :data="distributionData.habitats_hosts" style="width: 100%" :show-header="false">
                <el-table-column prop="number" label="Number" width="60">
                  <template #default="props">
                    <el-link href="/browse_data" type="primary"> {{ props.row.number }} </el-link>
                  </template>
                </el-table-column>
                <el-table-column prop="type" label="Type" width="100"> </el-table-column>
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
              <el-carousel :interval="5000" arrow="always" height="350px" :autoplay="true">
                <el-carousel-item v-for="graph in distributioinGraphs" :key="graph">
                  <!--                <h3>{{ graph.type }}</h3>-->
                  <el-image :src="graph.image" fit="scale-down"></el-image>
                </el-carousel-item>
              </el-carousel>
            </el-col>
          </el-row>
        </el-col>
        <el-col :span="10" :offset="2" type="flex" justify="middle">
          <el-row>
            <div style="line-height: 100px;">
              <el-input
                  type="textarea"
                  :autosize="{ minRows: 15, maxRows: 40}"
                  :placeholder="exampleSequences"
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
        statistics: {
          num_amps: 863498,
          num_families: 530194,
          num_genomes: 49757,
          num_habitats: 57,
          num_hosts: 195,
          num_metagenomes: 61393
        },
        distributionData: {
          amps_families: [
            {number: 0, type: 'AMPs'},
            {number: 0, type: 'families'},
          ],
          genomes_metagenomes: [
            {number: 0, type: 'genomes'},
            {number: 0, type: 'metagenomes'}
          ],
          habitats_hosts: [
            {number: 0, type: 'habitats'},
            {number: 0, type: 'hosts'},
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
            "GRVIGKQGRIAKAIRVVMRAAAVRVDEKVLVEID\n" +
            ">AMP10.000_004 | SPHERE-III.001_863\n" +
            "KLRKILKSMFNNYCKTFKDVPPGNMFR\n" +
            ">AMP10.000_005 | SPHERE-III.013_380\n" +
            "AIFYVIKHISRKHFVSLQRYKIKEKM\n" +
            ">AMP10.000_006 | SPHERE-III.007_692\n" +
            "LVRIISMVIAGVIIVYLVRWIDNFFSRYRK"
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
                {number: self.statistics.num_amps, type: 'AMPs'},
                {number: self.statistics.num_families, type: 'families'},
              ],
              genomes_metagenomes: [
                {number: self.statistics.num_genomes, type: 'genomes'},
                {number: self.statistics.num_metagenomes, type: 'metagenomes'}
              ],
              habitats_hosts: [
                {number: self.statistics.num_habitats, type: 'habitats'},
                {number: self.statistics.num_hosts, type: 'hosts'},
              ]
            }
          })
          .catch(function (error) {
            console.log(error);
          });
      },
    }
  }
</script>
