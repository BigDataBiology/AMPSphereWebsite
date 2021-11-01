<template>
  <div class="Home">
    <div class="row justify-center">
      <div class="col-0 col-xl-2 bg-white"></div>
      <div class="col-12 col-md-7 col-xl-5 justify-center q-pr-md q-ma-auto">
        <div class="row">
          <div class="col-12 text-center" style="font-size: 150%">Browse by data type</div>
          <div class="col-md-4 col-xs-12">
            <el-table :data="distributionData.amps_families" style="width: 120%" :show-header="false">
              <el-table-column prop="number" label="Number">
                <template #default="props">
                  <el-link href="/browse_data" type="primary" style="font-size: medium"> {{
                      props.row.number
                    }}
                  </el-link>
                </template>
              </el-table-column>
              <el-table-column prop="type" label="Type"></el-table-column>
            </el-table>
          </div>
          <div class="col-md-4 col-xs-12">
            <!--              <h4>Derived from</h4>-->
            <el-table :data="distributionData.genomes_metagenomes" style="width: 120%" :show-header="false">
              <el-table-column prop="number" label="Number">
                <template #default="props">
                  <el-link href="/browse_data" type="primary" style="font-size: medium"> {{
                      props.row.number
                    }}
                  </el-link>
                </template>
              </el-table-column>
              <el-table-column prop="type" label="Type"></el-table-column>
            </el-table>
          </div>
          <div class="col-md-4 col-xs-12">
            <el-table :data="distributionData.habitats_hosts" style="width: 120%" :show-header="false">
              <el-table-column prop="number" label="Number">
                <template #default="props">
                  <el-link href="/browse_data" type="primary" style="font-size: medium"> {{
                      props.row.number
                    }}
                  </el-link>
                </template>
              </el-table-column>
              <el-table-column prop="type" label="Type"></el-table-column>
            </el-table>
          </div>
        </div>
        <div class="row">
          <div class="col-12">
            <q-carousel animated v-model="slideIndex" control-color="primary" control-text-color="black" arrows
                        navigation autoplay height="31rem">
              <q-carousel-slide :name="1" :img-src="distributioinGraphs[0].image" fit="scale-down"/>
              <q-carousel-slide :name="2" :img-src="distributioinGraphs[1].image" fit="scale-down"/>
              <q-carousel-slide :name="3" :img-src="distributioinGraphs[2].image" fit="scale-down"/>
            </q-carousel>
          </div>

          <!--              <el-carousel :interval="5000" height="500px" :autoplay="true">-->
          <!--                <el-carousel-item v-for="graph in distributioinGraphs" :key="graph">-->
          <!--                  &lt;!&ndash;                <h3>{{ graph.type }}</h3>&ndash;&gt;-->
          <!--                  <el-image :src="graph.image" fit="scale-down"></el-image>-->
          <!--                </el-carousel-item>-->
          <!--              </el-carousel>-->
        </div>
      </div>
      <div class="col-12 col-md-5 col-xl-3 justify-center q-pl-md q-ma-auto">
        <div class="row">
          <div class="col-12" style="font-size: 150%; text-align: center">Search by sequence</div>
          <div class="col-12">
            <div style="text-align: left">
              Paste (&leq; 10) peptide sequences here (fasta format). <br/><br/>
              Or try
              <el-link type="primary" href="http://18.140.248.253/downloads"> our search databases</el-link>
              .<br/><br/>
              <el-input
                  type="textarea"
                  :rows="20"
                  :autosize="{ minRows: 15, maxRows: 20}"
                  :placeholder="exampleSequences"
                  v-model="sequences">
              </el-input>
            </div>
            <br/>
          </div>
          <div class="col-12">
            <el-tooltip content="Search for AMP" placement="bottom">
              <el-radio v-model="searchMethod" label="MMseqs">
                MMseqs
              </el-radio>
            </el-tooltip>
            <el-tooltip content="Search for family" placement="bottom">
              <el-radio v-model="searchMethod" label="HMMER">
                HMMSearch
              </el-radio>
            </el-tooltip>
            <el-button type="primary" @click="sequenceSearch">
              <BootstrapIcon icon="search" variant="light" size="1x"/>
              Search
            </el-button>
          </div>

        </div>
      </div>
      <div class="col-0 col-xl-2 bg-white"></div>
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
import {ref} from "vue";

export default {
  name: 'Home',
  data() {
    return {
      slideIndex: ref(1),
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
  mounted() {
    this.retrieveStatistics()
  },
  methods: {
    handleFamilyDetail(accession) {
      console.log('goto', '/family?accession=' + accession)
      window.open('/family?accession=' + accession, '_blank')
    },
    handleBrowse(by) {
      window.open('/browse_data?by=' + by, '_blank')
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
    sequenceSearch() {
      if ((this.sequences.match(/\n/g) || '').length + 1 > 20) {
        this.$message('Please input no more than 10 sequences.')
      } else {
        if (this.sequences === '') {
          window.open(
              encodeURI('/sequence_search?method=' + this.searchMethod + '&queries=' + this.exampleSequences),
              '_blank')
        } else {
          window.open(
              encodeURI('/sequence_search?method=' + this.searchMethod + '&queries=' + this.sequences),
              '_blank')
        }
      }
    }
  }
}
</script>
