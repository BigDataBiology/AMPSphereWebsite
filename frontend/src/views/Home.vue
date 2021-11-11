<template>
  <div class="Home">
    <div class="row justify-center">
      <div class="col-0 col-xl-2 bg-white"></div>
      <div class="col-12 col-md-7 col-xl-5 justify-center q-pr-md q-ma-auto">
        <div class="row">
          <div class="col-12 text-center subsection-title-center q-mb-md">Overall statistics and distribution</div>
          <div class="col-md-4 col-xs-12">
            <el-table :data="distributionData.amps_families" style="width: 120%" :show-header="false">
              <el-table-column prop="number" label="Number">
                <template #default="props">
                  <a href="/browse_data" style="font-size: medium"> {{ props.row.number }}</a>
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
                  <a href="/browse_data" style="font-size: medium"> {{ props.row.number }}</a>
                </template>
              </el-table-column>
              <el-table-column prop="type" label="Type"></el-table-column>
            </el-table>
          </div>
          <div class="col-md-4 col-xs-12">
            <el-table :data="distributionData.habitats_hosts" style="width: 120%" :show-header="false">
              <el-table-column prop="number" label="Number">
                <template #default="props">
                  <a href="/browse_data" style="font-size: medium"> {{ props.row.number }}</a>
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
          <div class="col-12 text-center subsection-title-center  q-mb-md">Search by sequence</div>
          <div class="col-12">
            <div class="main-text">
              Paste (&leq; 10) peptide sequences here (fasta format). <br/>
              <span class="text-bold">Note</span>: For large queries and offline use, please download<a href="http://18.140.248.253/downloads"> our prebuilt indices</a>.
            </div>
          </div>
          <div class="col-12">
            <q-input class="q-my-md" v-model="sequences" filled clearable type="textarea" color="primary"
                     label="Please enter up to 10 sequences" rows="20"/>
<!--            TODO update here.-->
<!--            <q-uploader-->
<!--                style="max-width: 300px"-->
<!--                url="http://localhost:4444/upload"-->
<!--                label="Upload a fasta file."-->
<!--                max-files="1"-->
<!--                @rejected="onRejected"-->
<!--            />-->

            <!--            <q-input-->
<!--                type="textarea" :rows="20" :autosize="{ minRows: 15, maxRows: 20}" :placeholder="exampleSequences" v-model="sequences">-->
<!--            </q-input>-->
            <div class="text-bold">
              Search for:
              <q-btn-toggle
                  v-model="searchMethod" no-caps rounded unelevated toggle-color="primary" color="white"
                  text-color="primary" size="sm"
                  :options="[{label: 'AMPs', value: 'MMseqs', slot: 'MMseqs'}, {label: 'Families', value: 'HMMER', slot: 'HMMER'}]" />
<!--              <el-radio v-model="searchMethod" label="MMseqs">AMPs</el-radio>-->
<!--              <el-radio v-model="searchMethod" label="HMMER">Families</el-radio>-->
              <q-btn @click="sequenceSearch" label="Submit" class="bg-primary text-white" />
            </div>

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
import {ref} from "vue"
import {useQuasar} from 'quasar'


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
      // exampleSequences:
      //     ">AMP10.000_002 | SPHERE-III.010_054\n" +
      //     "KRVKSFFKGYMRAIEINAALMYGYRPK\n" +
      //     ">AMP10.000_003 | SPHERE-III.001_008\n" +
      //     "GRVIGKQGRIAKAIRVVMRAAAVRVDEKVLVEID\n",
      searchMethod: 'MMseqs',
      sequences:
          ">AMP10.000_002 | SPHERE-III.010_054\n" +
          "KRVKSFFKGYMRAIEINAALMYGYRPK\n" +
          ">AMP10.000_003 | SPHERE-III.001_008\n" +
          "GRVIGKQGRIAKAIRVVMRAAAVRVDEKVLVEID\n",
      // fastaFile: [],
    }
  },
  setup(){
    const $q = useQuasar()
    $q.notify({
      message: '<strong>Note</strong>: the website is still a work-in-progress. Improvements are ongoing.',
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
  mounted() {
    this.retrieveStatistics()
  },
  methods: {
    handleFamilyDetail(accession) {
      console.log('goto', '/family?accession=' + accession)
      window.open('/family?accession=' + accession)
    },
    handleBrowse(by) {
      window.open('/browse_data?by=' + by)
    },
    retrieveStatistics() {
      var self = this
      this.axios.get('/statistics', {})
          .then(function (response) {
            console.log(response.data)
            self.statistics = response.data
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
        this.$message('Please input up to 10 sequences.')
      } else {
        window.open(encodeURI('/sequence_search?method=' + this.searchMethod + '&queries=' + this.sequences), '_self')
      }
    },
  }
}
</script>
