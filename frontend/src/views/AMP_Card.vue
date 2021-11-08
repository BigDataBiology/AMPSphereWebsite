<template>
  <div class="AMP_card">
    <div class="row justify-center">
      <div class="col-xs-0 col-xl-2 bg-white"></div>
      <div class="col-12 col-xl-8 justify-center q-pr-md q-ma-auto">
        <div class="row">
          <div class="col-12 q-px-md">
            <div class="text-h4">Antimicrobial peptide: {{ accession }}</div>
            <!--                    TODO test: move this description down to the overview tab-->
            <div class="text-body1">
              The AMP belongs to
              <el-link :href="getFamilyPageURL()" type="primary">
                <span class="text-body1">{{ family }}</span>
              </el-link>
              family and has {{ length }} amino acid residues.
            </div>
          </div>
        </div>
        <div class="row bg-white">
          <div class="col-12 q-pa-md">
            <q-tabs v-model="tabName" dense align="left" class="text-teal text-white">
              <q-tab name="overview" label="Overview" />
              <q-tab name="features" label="Features" />
            </q-tabs>
            <q-tab-panels v-model="tabName" animated class="row text-left">
              <q-tab-panel name="overview">
                <div class="row text-left">
                  <div class="col-12 col-md-3 q-pt-md q-px-md justify-center">
                    <div class="subsubsection-title">
                      Peptide sequence <q-btn @click="CopyPeptideSequence()" icon="content_copy" size="sm"></q-btn>
                    </div>
                    <pre><code id="aa-sequence">{{ sequence }}</code></pre>
                    <div class="subsubsection-title">Secondary Structure</div>
                    <Plotly :data="SecStructureBarData()" :layout="secondaryStructureLayout()"
                            :toImageButtonOptions="{format: 'svg', scale: 1}"/>
                  </div>
                  <div class="col-12 col-md-8 offset-md-1 q-pt-md q-px-md justify-center" id="global distribution">
                    <div class="subsubsection-title text-center">Geographical Distribution</div>
                    <Plotly :data="GeoPlotData()" :layout="GeoPlotLayout()" :toImageButtonOptions="{format: 'svg', scale: 1}"/>
                  </div>
                </div>
                <div class="row">
                  <div class="col-12 q-px-md q-pt-md">
                    <div class="subsection-title">Distribution</div>
                  </div>
                  <div class="col-12 col-md-6">
<!--                    TODO Bigger title  and figure captions-->
                    <div class="subsubsection-title text-center">Habitats</div>
                    <Plotly :data="EnvPlotData()" :layout="EnvPlotLayout()" :toImageButtonOptions="{format: 'svg', scale: 1}"/>
                  </div>
                  <div class="col-12 col-md-6">
                    <!--                    TODO Bigger title and figure captions -->
                    <div class="subsubsection-title text-center">Hosts</div>
                    <Plotly :data="HostPlotData()" :layout="HostPlotLayout()" :toImageButtonOptions="{format: 'svg', scale: 1}"/>
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
                      <el-table-column prop="host_scientific_name" label="Host" sortable width="150%"/>
                      <el-table-column prop="origin_scientific_name" label="AMP source" sortable width="150%"/>
                    </el-table>
                    <div class="block">
                      <el-pagination
                          @size-change="setMetadataPageSize"
                          @current-change="setMetadataPage"
                          :page-sizes="[5, 10, 20, 50, 100]"
                          :page-size="5"
                          layout="total, sizes, prev, pager, next, jumper"
                          :total="metadata.info.totalRow"
                      >
                      </el-pagination>
                    </div>
                  </div>
                </div>
              </q-tab-panel>
              <q-tab-panel name="features">
                <div class="row">
                  <div class="col-12 q-pa-md">
                    <div class="subsection-title">Biochemical properties</div>
                    <div class="info-item-value">
                      The feature value of {{ accession }} was pointed out in the distribution among its entire AMP family.
                    </div>
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
                    <div class="row">
                      <div class="col-12 col-md-4">
                        <div style="text-align: center" id="helical-wheel">
                          <br/><br/>
                          <el-link :href="helicalwheel" type="primary">
                            <span class="medium">Helical wheel</span>
                          </el-link>
                          <br/>
                          Amino acids helical wheel with the H-moment indicated, calculated by using <el-link href="https://modlamp.org/modlamp.html?highlight=helical%20wheel#modlamp.plot.helical_wheel">helical_wheel</el-link> from <el-link href="https://modlamp.org/">modlAMP</el-link>
                        </div>
                        <div style="align-content: center; text-align: center;">
                          <el-image :src="helicalwheel"></el-image>
                        </div>
                      </div>
                      <div class="col-12 col-md-4">
                        <Plotly :data="makeFamilyFeatureTraces(famFeaturesGraphData.MW)"
                                :layout="familyFeatureGraphLayout(features.MW, 'Molecular weight')"/>
                      </div>
                      <div class="col-12 col-md-4">
                        <Plotly :data="makeFamilyFeatureTraces(famFeaturesGraphData.Aromaticity)"
                                :layout="familyFeatureGraphLayout(features.Aromaticity, 'Aromaticity')" />
                      </div>
                    </div>
                    <div class="row">
                      <div  class="col-12 col-md-4">
                        <Plotly :data="makeFamilyFeatureTraces(famFeaturesGraphData.GRAVY)"
                                :layout="familyFeatureGraphLayout(features.GRAVY, 'GRAVY')" />
                      </div>
                      <div class="col-12 col-md-4">
                        <Plotly :data="makeFamilyFeatureTraces(famFeaturesGraphData.Instability_index)"
                                :layout="familyFeatureGraphLayout(features.Instability_index, 'Instability index')" />
                      </div>
                      <div class="col-12 col-md-4">
                        <Plotly :data="makeFamilyFeatureTraces(famFeaturesGraphData.Isoelectric_point)"
                                :layout="familyFeatureGraphLayout(features.Isoelectric_point, 'Isoelectric point')" />
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-12 col-md-4">
                        <Plotly :data="makeFamilyFeatureTraces(famFeaturesGraphData.Charge_at_pH_7)"
                                :layout="familyFeatureGraphLayout(features.Charge_at_pH_7, 'Charge at pH 7.0')" />
                      </div>
                      <div class="col-12 col-md-4">
                        <Plotly :data="makeFamilyFeatureTraces(famFeaturesGraphData.Molar_extinction.cystines_residues)"
                                :layout="familyFeatureGraphLayout(features.Molar_extinction.cystines_residues, 'Molar extinction (cystines residues)')" />
                      </div>
                      <div class="col-12 col-md-4">
                        <Plotly :data="makeFamilyFeatureTraces(famFeaturesGraphData.Molar_extinction.cysteines_reduced)"
                                :layout="familyFeatureGraphLayout(features.Molar_extinction.cysteines_reduced, 'Molar extinction (ccysteines reduced)')" />
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



<!--                    <el-divider></el-divider>-->

<!--                    <br/>-->
<!--                    <el-divider></el-divider>-->
<!--    &lt;!&ndash;                      <el-pagination&ndash;&gt;-->
<!--    &lt;!&ndash;                          @current-change="setMetadataPage"&ndash;&gt;-->
<!--    &lt;!&ndash;                          :page-size="metadata.info.pageSize"&ndash;&gt;-->
<!--    &lt;!&ndash;                          layout="total, prev, pager, next, jumper"&ndash;&gt;-->
<!--    &lt;!&ndash;                          :total="metadata.info.totalRow"&ndash;&gt;-->
<!--    &lt;!&ndash;                      >&ndash;&gt;-->
<!--    &lt;!&ndash;                      </el-pagination>&ndash;&gt;-->
<!--      &lt;!&ndash;                    FIXME integrate pagination buttons with the table&ndash;&gt;-->
<!--                        </div>-->

<!--                      </el-col>-->
<!--                    </el-row>-->
<!--                  </el-tab-pane>-->
<!--                  <el-tab-pane label="Features">-->
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

.el-tabs__item {
  font-size: 17px;
}

.el-aside {
  /*background-color: #D3DCE6;*/
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  color: #333;
  text-align: center;
}
</style>

<script>
import Plotly from "../components/Plotly"
import * as clipboard from "clipboard-polyfill/text";


export default {
  name: 'AMP_card',
  components: {
    Plotly,
  },
  data() {
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
      accession: this.$route.query.accession,
      sequence: '',
      length: 0,
      family: '',
      features: {
        MW: 0,
        Length: 0,
        Molar_extinction: {cysteines_reduced: 0, cystines_residues: 0},
        Aromaticity: 0,
        GRAVY: 0,
        Instability_index: 0,
        Isoelectric_point: 0,
        Charge_at_pH_7: 0,
        Secondary_structure: {helix: 0, turn: 0, sheet: 0},
        graph_points: {
          transfer_energy: {type: "line plot", x: [], y: [], c: []},
          hydrophobicity_parker: {type: "line plot", x: [], y: [], c: []},
          surface_accessibility: {type: "line plot", x: [], y: [], c: []},
          flexibility: {type: "line plot", x: [], y: [], c: []}
        }
      },
      famFeaturesGraphData: {
        MW: [],
        Length: [],
        Molar_extinction: {cysteines_reduced: [], cystines_residues: []},
        Aromaticity: [],
        GRAVY: [],
        Instability_index: [],
        Isoelectric_point: [],
        Charge_at_pH_7: [],
        Secondary_structure: {helix: [], turn: [], sheet: []},
      },
      metadata: {
        info: {
          pageSize: 5,
          totalPage: 1,
          totalRow: 1,
          currentPage: 1,
        },
        currentData: [],
      },
      distribution: {
        geo: {
          type: "bubble map",
          lat: [], lon: [], size: [], colors: []
        },
        habitat: {
          type: "sunburst plot",
          labels: [], parents: [], values: [], colorway: []
        },
        host: {
          type: "sunburst plot",
          labels: [], parents: [], values: [], colorway: []
        },
        origin: {
          type: "sunburst plot",
          labels: [], parents: [], values: [], colorway: []
        }
      },
      helicalwheel: ''
    }
  },
  created() {
    this.getAMP()
  },
  mounted() {
    this.setMetadataPageSize(5)
  },
  computed: {
    currentMetadata() {
      return this.metadata.currentData
    }
  },
  methods: {
    getAMP() {
      let self = this
      let amp_accession = self.$route.query.accession
      this.axios.get('/amps/' + amp_accession, {})
          .then(function (response) {
            console.log(response.data)
            self.sequence = response.data.sequence
            console.log(response.data.sequence)
            console.log(response.data.sequence.length)
            self.length = response.data.sequence.length
            self.family = response.data.family
            self.helicalwheel = 'http://18.140.248.253:443/v1/amps/' + self.accession + '/helicalwheel'
            self.features = response.data.features
            self.metadata.currentData = response.data.metadata.data
            self.metadata.info.currentPage = 1
            self.metadata.info.totalPage = response.data.metadata.info.totalPage
            self.metadata.info.totalRow = response.data.metadata.info.totalItem
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
    getFamilyFeatures() {
      let self = this
      this.axios.get('/families/' + self.family + '/features', {})
          .then(function (response) {
            console.log(response.data)
            self.updateFamilyFeatures(response.data)
          })
          .catch(function (error) {
            console.log(error)
          })
    },
    SecStructureBarData() {
      let strucData = this.features.Secondary_structure
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
      this.metadata.info.currentPage = page - 1
      console.log(this.metadata.info.currentPage)
      let config = {
        params: {page: this.metadata.info.currentPage, page_size: this.metadata.info.pageSize}
      }
      let self = this
      this.axios.get('/amps/' + self.accession + '/metadata', config)
          .then(function (response) {
            console.log(response.data)
            self.metadata.currentData = response.data.data
            self.metadata.info.totalPage = response.data.info.totalPage
            self.metadata.info.totalRow = response.data.info.totalItem
          })
          .catch(function (error) {
            console.log(error);
          })
    },
    setMetadataPageSize(size) {
      this.metadata.info.pageSize = size
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
        type: "sunburst",
        labels: data.habitat.labels, //["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parents: data.habitat.parents, //["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
        values: data.habitat.values, //[65, 14, 12, 10, 2, 6, 6, 4, 4],
        leaf: {opacity: 0.4},
        // marker: {line: {"width": 2}},
        branchvalues: 'total'
      }
      return [env_data]
    },
    EnvPlotLayout() {
      return {
        margin: {l: 0, r: 0, b: 0, t: 0}, autosize: true,
        sunburstcolorway: this.ColorPalette('quanlitative')
      };
    },
    HostPlotData() {
      let data = this.distribution
      let host_data = {
        type: "sunburst",
        labels: data.host.labels, //["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parents: data.host.parents, //["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
        values: data.host.values, //[65, 14, 12, 10, 2, 6, 6, 4, 4],
        leaf: {opacity: 0.4},
        // marker: {line: {"width": 2}},
        branchvalues: 'total'
      }
      return [host_data]
    },
    HostPlotLayout() {
      return {
        margin: {l: 0, r: 0, b: 0, t: 0}, autosize: true,
        sunburstcolorway: this.ColorPalette('quanlitative')
      };
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
      let host_data = {
        type: "sunburst",
        labels: data.host.labels, //['Viruses', "Anelloviridae", "unclassified Anelloviridae", "Small anellovirus", "cellular organisms", "Bacteria", "Terrabacteria group", "Actinobacteria"],
        parents: data.host.parents, // ["", 'Viruses', "Anelloviridae", "unclassified Anelloviridae", "", "cellular organisms", "Bacteria", "Terrabacteria group"],
        values: data.host.values, //[14, 14, 14, 14, 6, 6, 6, 6],
        outsidetextfont: {size: 20, color: "#377eb8"},
        leaf: {opacity: 0.4},
        // marker: {line: {width: 2}},
        branchvalues: 'total',
        visible: false,
      }
      return [habitat_data, host_data]
    },
    DistributionGraphLayout() {
      return {
        height: 400, margin: {l: 40, r: 40, b: 40, t: 40}, autosize: true,
        sunburstcolorway: this.ColorPalette('quanlitative'),
        updatemenus: [{
          direction: 'left', type: 'buttons', pad: {r: 10, t: 10},
          showactive: true, x: 0.5, y: 1.2, yanchor: 'top', xanchor: 'center',
          buttons: [{
            method: 'update',
            args: [{'visible': this.makeTraceVisible(0, 2)}],
            label: 'Habitats'
          }, {
            method: 'update',
            args: [{'visible': this.makeTraceVisible(1, 2)}],
            label: 'Hosts'
          },
          ]
        }
        ]
      }
    },
    initFamilyFeatures() {
      this.famFeaturesGraphData = {
        MW: [],
        Length: [],
        Molar_extinction: {cysteines_reduced: [], cystines_residues: []},
        Aromaticity: [],
        GRAVY: [],
        Instability_index: [],
        Isoelectric_point: [],
        Charge_at_pH_7: [],
        Secondary_structure: {helix: [], turn: [], sheet: []},
      }
    },
    updateFamilyFeatures(data) {
      this.initFamilyFeatures()
      console.log(data)
      let self = this
      Object.values(data).forEach(function (amp_features) {
            self.famFeaturesGraphData.Instability_index.push(amp_features.Instability_index)
            self.famFeaturesGraphData.GRAVY.push(amp_features.GRAVY)
            self.famFeaturesGraphData.MW.push(amp_features.MW)
            self.famFeaturesGraphData.Aromaticity.push(amp_features.Aromaticity)
            self.famFeaturesGraphData.Charge_at_pH_7.push(amp_features.Charge_at_pH_7)
            self.famFeaturesGraphData.Isoelectric_point.push(amp_features.Isoelectric_point)
            self.famFeaturesGraphData.Molar_extinction.cysteines_reduced.push(amp_features.Molar_extinction.cysteines_reduced)
            self.famFeaturesGraphData.Molar_extinction.cystines_residues.push(amp_features.Molar_extinction.cystines_residues)
            // self.famFeaturesGraphData.Secondary_structure.helix.push(amp_features.Secondary_structure.helix)
            // self.famFeaturesGraphData.Secondary_structure.turn.push(amp_features.SecStructureBarData.turn)
            // self.famFeaturesGraphData.Secondary_structure.sheet.push(amp_features.Secondary_structure.sheet)
          }
      )
    },
    makeFamilyFeatureTraces(data) {
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
    familyFeatureGraphLayout(value, name) {
      return {
        title: name,
        autosize: true,
        margin: {l: 50, r: 20, b: 20, t: 80},
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
      return "http://18.140.248.253/family?accession=" + this.family
    },
    CopyPeptideSequence() {
      clipboard.writeText(this.sequence).then(
          () => {
            console.log("success!");
          },
          () => {
            console.log("error!");
          }
      )
      this.$message('Amino acid sequence copied!')
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
