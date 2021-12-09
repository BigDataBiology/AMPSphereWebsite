<template>
  <div class="AMP_card">
    <div class="row justify-center">
      <div class="col-xs-0 col-xl-2 bg-white"></div>
      <div class="col-12 col-xl-8 justify-center q-pr-md q-ma-auto">
        <div class="row">
          <div class="col-12 q-px-md">
            <div class="text-h4 q-my-md">Antimicrobial peptide: {{ amp.accession }}</div>
            <!--                    TODO test: move this description down to the overview tab-->
            <div class="row">
              <div class="col-6">
                <div class="row">
                  <span class="text-bold">Quality
                    <a href="/about">?</a>
                    <q-tooltip :offset="[10, 10]">
                      Understand how we controlled the quality.
                    </q-tooltip>
                    :
                  </span>
                  <q-img v-if="amp.quality.Antifam !== 'yellow'" class="col" :src="makeQualityBadge('Antifam', amp.quality.Antifam)" height="2rem" fit="scale-down"></q-img>
                  <q-img v-if="amp.quality.coordinates !== 'yellow'" class="col" :src="makeQualityBadge('coordinates', amp.quality.coordinates)" height="2rem" fit="scale-down"></q-img>
                  <q-img v-if="amp.quality.metaproteomes !== 'yellow'" class="col" :src="makeQualityBadge('metaproteomes', amp.quality.metaproteomes)" height="2rem" fit="scale-down"></q-img>
                  <q-img v-if="amp.quality.RNAcode !== 'yellow'" class="col" :src="makeQualityBadge('RNAcode', amp.quality.RNAcode)" height="2rem" fit="scale-down"></q-img>
                </div>
              </div>
            </div>
            <div class="text-body1">
              The AMP belongs to
              <a :href="getFamilyPageURL()">
                <span class="text-body1">{{ amp.family }}</span>
              </a>
              family and has {{ amp.length }} amino acid residues.
            </div>
          </div>
        </div>
        <div class="row bg-white">
          <div class="col-12 q-pa-md">
            <q-tabs v-model="tabName" dense align="left" class="text-teal text-white">
              <q-tab name="overview" label="Overview" tabindex="overview" index="overview"/>
              <q-tab name="features" label="Features" tabindex="features" index="features"/>
            </q-tabs>
            <q-tab-panels v-model="tabName" animated class="row text-left">
              <q-tab-panel name="overview">
                <div class="row text-left">
                  <div class="col-12 col-md-3 q-pt-md q-px-md justify-center">
                    <div class="subsubsection-title">
                      Peptide sequence <q-btn @click="CopyPeptideSequence()" icon="content_copy" size="sm"></q-btn>
                    </div>
                    <pre><code id="aa-sequence">{{ amp.sequence }}</code></pre>
                    <div class="subsubsection-title">Secondary Structure</div>
                    <Plotly :data="SecStructureBarData()" :layout="secondaryStructureLayout()"
                            :toImageButtonOptions="{format: 'svg', scale: 1}"/>
                  </div>
                  <div class="col-12 col-md-8 offset-md-1 q-pt-md q-px-md justify-center" id="global distribution">
                    <div class="subsubsection-title text-center">Geographical Distribution</div>
                    <div v-if="distribution.geo.lat.length > 0">
                      <Plotly :data="GeoPlotData()" :layout="GeoPlotLayout()" :toImageButtonOptions="{format: 'svg', scale: 1}"/>
                    </div>
                    <div v-else>
                      <div style="height:400px; line-height: 400px" class="text-center q-px-md">
                        Empty, all associated smORF genes were from Progenomes2 genomes (no geographical information).
                      </div>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-12 q-px-md q-pt-md">
                    <div class="subsection-title">Distribution</div>
                  </div>
                  <div class="col-12 col-md-6 q-px-md">
<!--                    TODO Bigger title  and figure captions-->
                    <div class="subsubsection-title text-center">Habitats</div>
                    <div v-if="distribution.habitat.labels.length !== 0">
                      <Plotly :data="EnvPlotData()" :layout="EnvPlotLayout()" :toImageButtonOptions="{format: 'svg', scale: 1}"/>
                    </div>
                    <div v-else style="height:500px; display: -webkit-flex; display: flex; align-items: center; " class="text-center q-px-md">
                      <p>Empty, all associated smORF genes were from Progenomes2 genomes (no habitat information).</p>
                    </div>
                  </div>
                  <div class="col-12 col-md-6 q-px-md">
                    <div class="subsubsection-title text-center">Microbial sources</div>
                    <div>
                      <Plotly :data="MicrobialSourcePlotData()" :layout="MicrobialSourcePlotLayout()" :toImageButtonOptions="{format: 'svg', scale: 1}"/>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-12 q-px-md q-pt-md">
                    <div class="subsection-title">Relationships</div>
<!--                    TODO add download button here -->
                    <el-table :data="currentMetadata" stripe :default-sort="{prop: 'GMSC', order: 'ascending'}" width="100%">
                      <el-table-column prop="GMSC" label="Gene" sortable width="260%"/>
                      <el-table-column label="Gene sequense" sortable width="400%">
                        <template #default="props">
                          <pre><code><small>{{ props.row.gene_sequence }}</small></code></pre>
                        </template>
                      </el-table-column>
                      <el-table-column prop="sample" label="Sample/Genome" sortable width="150%"/>
                      <el-table-column prop="habitat" label="Habitat" sortable width="150%"/>
                      <el-table-column prop="microbial_source" label="microbial source" sortable width="150%"/>
                    </el-table>
                    <div class="block">
                      <el-pagination
                          @size-change="setMetadataPageSize"
                          @current-change="setMetadataPage"
                          :page-sizes="[5, 10, 20, 50, 100]"
                          :page-size="5"
                          layout="total, sizes, prev, pager, next, jumper"
                          :total="amp.metadata.info.totalRow"
                      >
                      </el-pagination>
                    </div>
                  </div>
                </div>
              </q-tab-panel>
              <q-tab-panel name="features">
                <div class="row">
                  <div class="col-12 q-pa-md">
                    <div class="row">
                      <div class="col-12 col-md-4 justify-center">
                        <div class="subsection-title q-py-md">Biochemical properties</div>
                        <ul>
                          <li>
                            <div class="info-item-value">
                              The feature value of {{ amp.accession }} was pointed out in the distribution among its entire AMP family.
                            </div>
                          </li>
                          <li>
                            <div class="info-item-value">
                              The features below were calculated by using the
                              <el-link href="https://biopython.org/docs/1.79/api/Bio.SeqUtils.ProtParam.html" type="primary">
                                Bio.SeqUtils.ProtParam.ProteinAnalysis
                              </el-link>
                              module from
                              <el-link href="https://doi.org/10.1093/bioinformatics/btp163" type="primary">
                                BioPython
                              </el-link> (version 1.79).
                            </div>
                          </li>
                          <li>
                            <div class="info-item-value">
                              Amino acids helical wheel with the H-moment indicated, calculated by using <el-link href="https://modlamp.org/modlamp.html?highlight=helical%20wheel#modlamp.plot.helical_wheel">helical_wheel</el-link> from <el-link href="https://modlamp.org/">modlAMP</el-link>
                            </div>
                          </li>
                        </ul>
                      </div>
                      <div class="col-12 col-md-4 offset-md-2 justify-center">
                        <div style="text-align: center" id="helical-wheel">
                          <el-link :href="amp.helicalwheel" type="primary">
                            <span class="medium">Helical wheel</span>
                          </el-link>
                        </div>
                        <div style="align-content: center; text-align: center;">
                          <el-image :src="amp.helicalwheel"></el-image>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-12 col-md-4">
                        <div class="subsection-title-center">Molecular weight<q-tooltip max-width="30rem">{{ featuresHelpMessages.MW }}</q-tooltip></div>
                        <Plotly :data="makeFamilyFeatureTraces(famFeaturesGraphData.molecular_weight)"
                                :layout="familyFeatureGraphLayout(amp.molecular_weight)"/>
                      </div>
                      <div class="col-12 col-md-4">
                        <div class="subsection-title-center">Aromaticity<q-tooltip max-width="30rem">{{ featuresHelpMessages.Aromaticity }}</q-tooltip></div>
                        <Plotly :data="makeFamilyFeatureTraces(famFeaturesGraphData.aromaticity)"
                                :layout="familyFeatureGraphLayout(amp.aromaticity)" />
                      </div>
                      <div  class="col-12 col-md-4">
                        <div class="subsection-title-center">GRAVY<q-tooltip max-width="30rem">{{ featuresHelpMessages.GRAVY }}</q-tooltip></div>
                        <Plotly :data="makeFamilyFeatureTraces(famFeaturesGraphData.gravy)"
                                :layout="familyFeatureGraphLayout(amp.gravy)" />
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-12 col-md-4">
                        <div class="subsection-title-center">Instability index<q-tooltip max-width="30rem">{{ featuresHelpMessages.Instability_index }}</q-tooltip></div>
                        <Plotly :data="makeFamilyFeatureTraces(famFeaturesGraphData.instability_index)"
                                :layout="familyFeatureGraphLayout(amp.instability_index)" />
                      </div>
                      <div class="col-12 col-md-4">
                        <div class="subsection-title-center">Isoelectric point<q-tooltip max-width="30rem">{{ featuresHelpMessages.pI }}</q-tooltip></div>
                        <Plotly :data="makeFamilyFeatureTraces(famFeaturesGraphData.isoelectric_point)"
                                :layout="familyFeatureGraphLayout(amp.isoelectric_point)" />
                      </div>
                      <div class="col-12 col-md-4">
                        <div class="subsection-title-center">Charge at pH 7.0<q-tooltip max-width="30rem">{{ featuresHelpMessages.Charge_at_pH_7 }}</q-tooltip></div>
                        <Plotly :data="makeFamilyFeatureTraces(famFeaturesGraphData.charge_at_pH_7)"
                                :layout="familyFeatureGraphLayout(amp.charge_at_pH_7)" />
                      </div>
                    </div>
  <!--                  TODO update this later, remove this for a while-->
  <!--                  <el-divider></el-divider>-->
  <!--                  <el-row>-->
  <!--                    <br>-->
  <!--                      <div styles="alignment: center; text-align: center">-->
  <!--                          <Plotly :data="featureGraphData()"-->
  <!--                                  :layout="featureGraphLayout()"-->
  <!--                                  :toImageButtonOptions="{format: 'svg', scale: 1}"/>-->
  <!--                      </div>-->
  <!--                        <div>-->
  <!--                          <span class="caption-bold">EZenergy.</span> Profile of {{ accession }} residues free energy of transfer from water to membrane lipid.-->
  <!--                        </div>-->
  <!--                        <div>-->
  <!--                          <span class="caption-bold">Flexibility.</span> Profile of flexibility of {{ accession }}. The normalized flexibility parameters (B-values) from <el-link href="https://onlinelibrary.wiley.com/doi/10.1002/prot.340190207" type="primary">Vihinen (1994)</el-link> was the scale adopted in the profile calculation.-->
  <!--                        </div>-->
  <!--                        <div>-->
  <!--                          <span class="caption-bold">Hydrophobicity Parker.</span> Profile of hydrophobicity of residues of {{ accession }} using the relative scale of Parker.-->
  <!--                        </div>-->
  <!--                        <div>-->
  <!--                          <span class="caption-bold">Surface accessibility.</span> Profile of solvent accessibility of residues of {{ accession }}.-->
  <!--                        </div>-->
  <!--                    <br/>-->
  <!--                  </el-row>-->
  <!--                  <el-divider></el-divider>-->
  <!--                  <el-row>-->
  <!--                    <br>-->
  <!--                    <div styles="alignment: center; text-align: center">-->
  <!--                      <v-chart :option="echartOption"></v-chart>-->
  <!--                    </div>-->
  <!--                    <div>-->
  <!--                      <span class="caption-bold">EZenergy.</span> Profile of {{ accession }} residues free energy of transfer from water to membrane lipid.-->
  <!--                    </div>-->
  <!--                    <div>-->
  <!--                      <span class="caption-bold">Flexibility.</span> Profile of flexibility of {{ accession }}. The normalized flexibility parameters (B-values) from <el-link href="https://onlinelibrary.wiley.com/doi/10.1002/prot.340190207" type="primary">Vihinen (1994)</el-link> was the scale adopted in the profile calculation.-->
  <!--                    </div>-->
  <!--                    <div>-->
  <!--                      <span class="caption-bold">Hydrophobicity Parker.</span> Profile of hydrophobicity of residues of {{ accession }} using the relative scale of Parker.-->
  <!--                    </div>-->
  <!--                    <div>-->
  <!--                      <span class="caption-bold">Surface accessibility.</span> Profile of solvent accessibility of residues of {{ accession }}.-->
  <!--                    </div>-->
  <!--                    <br/>-->
  <!--                  </el-row>-->
                  </div>
                </div>
              </q-tab-panel>
            </q-tab-panels>
          </div>
        </div>
      </div>
      <div class="col-xs-0 col-xl-2 bg-white"></div>
    </div>
  </div>
</template>

<style>
.nav-section {
  font-size: medium;
  font-weight: bold
}

.nav-subsection {
  line-height: 1.5;
  font-size: medium;
  font-weight: normal;
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}
</style>

<script>
import Plotly from "../components/Plotly"
import * as clipboard from "clipboard-polyfill/text"
import { Notify } from "quasar"


export default {
  name: 'AMP_card',
  components: {
    Plotly,
  },
  data() {
    const default_distribution = {
      geo: {type: "bubble map", lat: [], lon: [], size: [], colors: []},
      habitat: {type: "bar plot", labels: [], values: []},
      microbial_source: {type: "bar plot", labels: [], values: []}
    }
    return {
      // echartOption: {
      //   xAxis: {
      //     type: 'category',
      //     data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
      //   },
      //   yAxis: {
      //     type: 'value'
      //   },
      //   series: [
      //     {
      //       data: [150, 230, 224, 218, 135, 147, 260],
      //       type: 'line'
      //     }
      //   ]
      // },
      tabName: 'overview',
      amp: {
        accession: this.$route.query.accession,
        sequence: '',
        length: 0,
        family: '',
        molecular_weight: 0,
        aromaticity: 0,
        gravy: 0,
        instability_index: 0,
        isoelectric_point: 0,
        charge_at_pH_7: 0,
        secondary_structure: {helix: 0, turn: 0, sheet: 0},
        feature_graph_points: {
          transfer_energy: {type: "line plot", x: [], y: [], c: []},
          hydrophobicity_parker: {type: "line plot", x: [], y: [], c: []},
          surface_accessibility: {type: "line plot", x: [], y: [], c: []},
          flexibility: {type: "line plot", x: [], y: [], c: []}
        },
        metadata: {
          info: {
            pageSize: 5,
            totalPage: 1,
            totalRow: 1,
            currentPage: 1,
          },
          data: [],
        },
        helicalwheel: '',
        quality: {
          Antifam: "yellow",
          RNAcode: "yellow",
          metaproteomes: "yellow",
          coordinates: "yellow",
          score: 0,
        },
      },
      distribution: default_distribution,
      default_distribution: default_distribution,
      famFeaturesGraphData: {
        molecular_weight: [],
        length: [],
        aromaticity: [],
        gravy: [],
        instability_index: [],
        isoelectric_point: [],
        charge_at_pH_7: [],
      },
      featuresHelpMessages: {
        MW: 'Molecular weight of a protein in Daltons.',
        Aromaticity: 'Aromaticity according to Lobry (1994), simply the relative frequency of Phe+Trp+Tyr.',
        Instability_index: 'Instability index according to Guruprasad et al (1990) is a test of a protein for stability. Values above 40 correspont to unstable proteins (short half lives).',
        GRAVY: 'Grand average of hydropathicity index (GRAVY) represents the hydrophobicity value of a peptide, and consists of the sum of the hydropathy values of all the amino acids divided by the sequence length. If GRAVY is positive, it indicates a hydrophobic protein as well as its opposite, when GRAVY is negative.',
        Charge_at_pH_7: 'Charge corresponds to the net electrical charge of a protein at pH 7.0',
        pI: 'Isoelectric point (pI) is the pH at which a particular molecule carries no net electrical charge.'
      },
    }
  },
  // setup (){
  //   const $q = useQuasar()
  // },
  created() {
    this.getAMP()
  },
  mounted() {
    this.setMetadataPageSize(5)
  },
  computed: {
    currentMetadata() {
      return this.amp.metadata.data
    }
  },
  methods: {
    getAMP() {
      let self = this
      let amp_accession = self.$route.query.accession
      this.axios.get('/amps/' + amp_accession, {})
          .then(function (response) {
            console.log(response.data)
            self.amp = response.data
            self.amp.helicalwheel = 'http://18.140.248.253:443/v1/amps/' + self.amp.accession +  '/helicalwheel'
            self.amp.metadata.info.totalRow = response.data.metadata.info.totalItem
            self.getFamilyFeatures()
          })
          .catch(function (error) {
            console.log(error);
          })
      this.axios.get('/amps/' + amp_accession + '/distributions', {})
          .then(function (response) {
            console.log(response.data)
            self.distribution = response.data
          })
          .catch(function (error) {
            console.log(error)
          })
    },
    makeQualityBadge(name, value){
      const URL = 'https://img.shields.io/static/v1?style=flat&label=' + name + '&color=' + value + '&message=' + this.getBadgeLabel(value) + '&style=flat'
      // console.log(URL)
      return URL
    },
    getBadgeLabel(quality_level){
      const quality_level_mapping = {
        green: 'Pass',
        yellow: 'Medium',
        red: 'Fail'
      }
      return quality_level_mapping[quality_level]
    },
    getFamilyFeatures() {
      let self = this
      this.axios.get('/families/' + self.amp.family + '/features', {})
          .then(function (response) {
            console.log(response.data)
            self.updateFamilyFeatures(response.data)
          })
          .catch(function (error) {
            console.log(error)
          })
    },
    SecStructureBarData() {
      let strucData = this.amp.secondary_structure
      // strucData.disordered = 1 - strucData.turn - strucData.helix - strucData.sheet
      return [{
        type: 'bar',
        name: '',
        x: Object.keys(strucData),
        y: Object.values(strucData),
        marker: {color: this.ColorPalette('quanlitative')},
        textinfo: "label+percent", insidetextorientation: "radial"
      }]
    },
    secondaryStructureLayout() {
      return {
        title: {text: ''},
        yaxis: {title: 'Fraction of amino acids'},
        margin: {l: 80, r: 40, t: 20, b: 60, pad: 0},
        showlegend: false,
        height: 300,
        width: 300
      }
    },
    setMetadataPage(page) {
      // this.$message('setting to ' + page + 'th page')
      // Important: page index starting from zero.
      this.amp.metadata.info.currentPage = page - 1
      console.log(this.amp.metadata.info.currentPage)
      let config = {
        params: {page: this.amp.metadata.info.currentPage, page_size: this.amp.metadata.info.pageSize}
      }
      let self = this
      this.axios.get('/amps/' + this.amp.accession + '/metadata', config)
          .then(function (response) {
            console.log(response.data)
            self.amp.metadata.data = response.data.data
            self.amp.metadata.info.totalPage = response.data.info.totalPage
            self.amp.metadata.info.totalRow = response.data.info.totalItem
            console.log(self.amp.metadata.data)
          })
          .catch(function (error) {
            console.log(error);
          })
    },
    setMetadataPageSize(size) {
      this.amp.metadata.info.pageSize = size
      this.setMetadataPage(1)
    },
    GeoPlotData() {
      let data = this.distribution.geo
      return [{
        type: 'scattergeo',
        //locationmode: 'USA-states',
        lat: data.lat,
        lon: data.lon,
        marker: {
          size: data.size,
          sizeref: 10,
          // FIXME
          // color: this.MapColors(data.colors, this.ColorPalette('quanlitative')),
          line: {
            color: 'black',
            size: 2
          }
        },
      }]
    },
    GeoPlotLayout() {
      return {
        // title: {
        //   text: 'Geographical distribution'
        // },
        height: 400,
        showlegend: false,
        geo: {
          scope: 'global',
          resolution: 50,
          showland: true,
          landcolor: 'rgb(217, 217, 217)',
          subunitwidth: 1,
          countrywidth: 1,
          subunitcolor: 'rgb(255,255,255)',
          countrycolor: 'rgb(255,255,255)'
        },
        margin: {
          l: 40,
          r: 40,
          t: 40,
          b: 40
        }
      }
    },
    EnvPlotData() {
      let data = this.distribution
      let env_data = {
        type: "bar",
        x: data.habitat.values,
        y: data.habitat.labels,
        orientation: 'h',
        marker: {
          color: this.ColorPalette('quanlitative')[0],
          width: 1
        },
      }
      return [env_data]
    },
    EnvPlotLayout() {
      return {
        margin: {l: 200, r: 50, b: 80, t: 20}, autosize: false, height: 500,
        xaxis: {
          type: 'log', autorange: true,
          title: {
            text: '# smORF genes (in exponential)',
            font: {
              size: 18,
            }
          },
        },
      }
    },
    MicrobialSourcePlotData(){
      let data = this.distribution
      let env_data = {
        type: "bar",
        x: data.microbial_source.values,
        y: data.microbial_source.labels,
        orientation: 'h',
        marker: {
          color: this.ColorPalette('quanlitative')[1],
          width: 1
        },
      }
      return [env_data]
    },
    MicrobialSourcePlotLayout(){
      return {
        margin: {l: 200, r: 50, b: 80, t: 20}, autosize: false, height: 500,
        xaxis: {
          type: 'log', autorange: true,
          title: {
            text: '# smORF genes (in exponential)',
            font: {
              size: 18,
            }
          },
        },
      }
    },
    DistributionGraphData() {
      let data = this.distribution
      let habitat_data = {
        type: "sunburst",
        labels: data.habitat.labels, //["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parents: data.habitat.parents, //["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
        values: data.habitat.values, //[65, 14, 12, 10, 2, 6, 6, 4, 4],
        leaf: {opacity: 0.4},
        // marker: {line: {"width": 2}},
        branchvalues: 'total'
      }
      // let host_data = {
      //   type: "sunburst",
      //   labels: data.host.labels, //['Viruses', "Anelloviridae", "unclassified Anelloviridae", "Small anellovirus", "cellular organisms", "Bacteria", "Terrabacteria group", "Actinobacteria"],
      //   parents: data.host.parents, // ["", 'Viruses', "Anelloviridae", "unclassified Anelloviridae", "", "cellular organisms", "Bacteria", "Terrabacteria group"],
      //   values: data.host.values, //[14, 14, 14, 14, 6, 6, 6, 6],
      //   outsidetextfont: {size: 20, color: "#377eb8"},
      //   leaf: {opacity: 0.4},
      //   // marker: {line: {width: 2}},
      //   branchvalues: 'total',
      //   visible: false,
      // }
      return [habitat_data]
    },
    // DistributionGraphLayout() {
    //   return {
    //     height: 400, margin: {l: 40, r: 40, b: 40, t: 40}, autosize: true,
    //     sunburstcolorway: this.ColorPalette('quanlitative'),
    //     updatemenus: [{
    //       direction: 'left', type: 'buttons', pad: {r: 10, t: 10},
    //       showactive: true, x: 0.5, y: 1.2, yanchor: 'top', xanchor: 'center',
    //       buttons: [{
    //         method: 'update',
    //         args: [{'visible': this.makeTraceVisible(0, 2)}],
    //         label: 'Habitats'
    //       }, {
    //         method: 'update',
    //         args: [{'visible': this.makeTraceVisible(1, 2)}],
    //         label: 'Hosts'
    //       },
    //       ]
    //     }
    //     ]
    //   }
    // },
    initFamilyFeatures() {
      this.famFeaturesGraphData = {
        molecular_weight: [],
        length: [],
        aromaticity: [],
        gravy: [],
        instability_index: [],
        isoelectric_point: [],
        charge_at_pH_7: [],
        // Secondary_structure: {helix: [], turn: [], sheet: []},
      }
    },
    updateFamilyFeatures(data) {
      this.initFamilyFeatures()
      let self = this
      Object.values(data).forEach(function (amp_features) {
            self.famFeaturesGraphData.instability_index.push(amp_features.Instability_index)
            self.famFeaturesGraphData.gravy.push(amp_features.GRAVY)
            self.famFeaturesGraphData.molecular_weight.push(amp_features.MW)
            self.famFeaturesGraphData.aromaticity.push(amp_features.Aromaticity)
            self.famFeaturesGraphData.charge_at_pH_7.push(amp_features.Charge_at_pH_7)
            self.famFeaturesGraphData.isoelectric_point.push(amp_features.Isoelectric_point)
            // self.famFeaturesGraphData.Secondary_structure.helix.push(amp_features.Secondary_structure.helix)
            // self.famFeaturesGraphData.Secondary_structure.turn.push(amp_features.SecStructureBarData.turn)
            // self.famFeaturesGraphData.Secondary_structure.sheet.push(amp_features.Secondary_structure.sheet)
          }
      )
    },
    makeFamilyFeatureTraces(data) {
      console.log(data)
      return [
        {
          type: 'violin',
          y: data,
          points: 'all',
          box: {
            visible: true
          },
          hoverinfo: 'y',
          boxpoints: 'none',
          line: {
            color: 'black'
          },
          fillcolor: '#8dd3c7',
          opacity: 0.6,
          meanline: {
            visible: true
          },
          name: ''
          // x0: ''
        }
      ]
    },
    familyFeatureGraphLayout(value) {
      return {
        // title: name,
        autosize: true,
        margin: {l: 50, r: 20, b: 20, t: 20},
        annotations: [{
          x: 0,
          xanchor: 'left',
          y: value,
          yanchor: 'bottom',
          text: this.accession,
          showarrow: true,
          font: {
            size: 16,
            color: 'red'
          },
          align: 'center',
          arrowhead: 1,
          arrowcolor: 'red',
          ax: 20,
          ay: -20,
        }],
        // shapes: [
        //   {
        //     type: 'scatter',
        //     x0: [0],
        //     y0: [value],
        //     marker: {
        //       color: 'red',
        //     }
        //   }
        // ]
      }
    },
    featureGraphData() {
      let self = this
      let data = self.features.graph_points
      let line = {color: 'blue'}
      return [

        {
          x: data.transfer_energy.x,
          y: data.transfer_energy.y,
          line: line,
          marker: {color: data.transfer_energy.c},
          visible: true,
        },
        {x: data.flexibility.x, y: data.flexibility.y, line: line, visible: false},
        {x: data.hydrophobicity_parker.x, y: data.hydrophobicity_parker.y, line: line, visible: false},
        {x: data.surface_accessibility.x, y: data.surface_accessibility.y, line: line, visible: false}
      ]
    },
    featureGraphLayout() {
      return {
        height: 600, width: 1000, margin: {l: 100, r: 100, b: 80, t: 40},
        // xaxis: {
        //   title: {
        //     text: 'Window start position'
        //   },
        //   showticklabels: true,
        //   tickfont: {
        //     // family: 'Old Standard TT, serif',
        //     size: 10,
        //     tickangle: 90,
        //     color: ['green', 'red', 'blue']//this.features.graph_points.surface_accessibility.c
        //   },
        //   // label: {
        //   //   font: {
        //   //     size: 10,
        //   //     color: this.features.graph_points.surface_accessibility.c
        //   //   }
        //   // }
        // },
        // yaxis: {
        //   title: {
        //     text: 'Selected feature'
        //   }
        // },
        updatemenus: [
          {
            direction: 'left', type: 'buttons', pad: {r: 10, t: 10},
            showactive: true, x: 0.5, y: 1.2, yanchor: 'top', xanchor: 'center',
            buttons: [
              {method: 'restyle', args: ['visible', this.makeTraceVisible(0, 4)], label: 'EZ energy'},
              {method: 'restyle', args: ['visible', this.makeTraceVisible(1, 4)], label: 'Flexibility'},
              {method: 'restyle', args: ['visible', this.makeTraceVisible(2, 4)], label: 'Hydrophobicity - Parker'},
              {method: 'restyle', args: ['visible', this.makeTraceVisible(3, 4)], label: 'Surface Accessibility'}
            ]
          }],
      }
    },
    comparisonGraphData() {
      function makeTrace(i) {
        return {
          y: Array.apply(null, Array(100)).map(() => Math.random()),
          line: {
            color: 'black'
          },
          visible: i === 0,
          //name: ['EZenergy', 'Flexibility', 'Hydrophobicity Parker', 'SA AMPs'].slice(i),
        };
      }

      return [0, 1, 2, 3, 4, 5, 6, 7].map(makeTrace)
    },
    comparisonGraphLayout() {
      return {
        direction: 'left', type: 'buttons', pad: {r: 10, t: 10},
        updatemenus: [
          {
            direction: 'left', type: 'buttons', pad: {'r': 10, 't': 10},
            showactive: true, x: 0.5, y: 1.4, yanchor: 'top', xanchor: 'center',
            buttons: [
              {method: 'restyle', args: ['visible', this.makeTraceVisible(4, 12)], label: 'aa composition diviation'},
              {method: 'restyle', args: ['visible', this.makeTraceVisible(5, 12)], label: 'aindex_z'},
              {method: 'restyle', args: ['visible', this.makeTraceVisible(6, 12)], label: 'boman_z'},
              {method: 'restyle', args: ['visible', this.makeTraceVisible(7, 12)], label: 'charge_z'}],
          },
          {
            direction: 'left', type: 'buttons', pad: {'r': 10, 't': 10},
            showactive: true, x: 0.5, y: 1.2, yanchor: 'top', xanchor: 'center',
            buttons: [
              {method: 'restyle', args: ['visible', this.makeTraceVisible(8, 12)], label: 'hmoment_z'},
              {method: 'restyle', args: ['visible', this.makeTraceVisible(9, 12)], label: 'hydrophobicity z'},
              {method: 'restyle', args: ['visible', this.makeTraceVisible(10, 12)], label: 'instaindex_z'},
              {method: 'restyle', args: ['visible', this.makeTraceVisible(11, 12)], label: 'pI_z'}]
          }
        ]
      }
    },
    MapColors(categories, colors) {
      const levels = [...new Set(categories)]
      console.log(levels)
      const mapping = []
      for (let i = 0; i <= categories.length; i++) {
        mapping[levels[i]] = colors[i]
      }
      return categories.map(function (cate) {
        return mapping[cate]
      })
    },
    ColorPalette(kind) {
      if (kind === 'sequential') {
        return ['#ffffe5', '#fff7bc', '#fee391', '#fec44f', '#fe9929', '#ec7014', '#cc4c02', '#8c2d04']
      } else if (kind === 'diverging') {
        return ['#8c510a', '#bf812d', '#dfc27d', '#f6e8c3', '#c7eae5', '#80cdc1', '#35978f', '#01665e']
      } else if (kind === 'quanlitative') {
        return ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#e6ab02', '#a6761d', '#666666']
      } else {
        console.log('please set the `kind` option for color palette.')
        return null
      }
    },
    exportSVG() {
      return {
        toImageButtonOptions: {
          format: 'svg', // one of png, svg, jpeg, webp
          filename: 'custom_image',
          height: 500,
          width: 700,
          scale: 1 // Multiply title/legend/axis/canvas sizes by this factor
        }
      }
    },
    getFamilyPageURL() {
      // TODO Change URL here
      return "/family?accession=" + this.amp.family
    },
    CopyPeptideSequence() {
      clipboard.writeText(this.amp.sequence).then(
          () => {
            console.log("success!");
            this.showNotif('Peptide sequences copied.')
          },
          () => {
            console.log("error!");
          }
      )
    },
    showNotif(message){
      Notify.create({
        message: message,
        // html: true,
        color: 'primary',
        position: 'bottom',
        timeout: 3000,
        icon: 'announcement',
        // actions: [
        //   { label: 'Got it', color: 'yellow', handler: () => { /* ... */ } }
        // ]
      })
    },
    makeTraceVisible(index, totalTrace) {
      var visibility = []
      for (var i = 0; i < totalTrace; i++) {
        visibility[i] = false
      }
      visibility[index] = true
      console.log(visibility)
      return visibility
    },
    UnpackCol(rows, key) {
      return rows.map(function (row) {
        return row[key];
      });
    },
    downloadCurrPage() {
      print()
    }
  }
}
// window.addEventListener("DOMContentLoaded", function () {
//   const button = document.body.appendChild(document.createElement("button"));
//   button.textContent = "Copy";
//   button.addEventListener("click", this.CopyPeptideSequence);
// });
</script>
