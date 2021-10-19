<template>
  <div class="Family_card">
    <el-row>
      <el-col :span="24">
        <el-container>
          <el-main>
            <div class="title">Antimicrobial peptide family: {{ accession }}
<!--              <el-button class="button" @click="downloadCurrPage()" type="primary" icon="el-icon-download" plain></el-button>-->
            </div>
            <!--          TODO test: move this description down to the overview tab-->

            <el-tabs type="border-card">
              <el-tab-pane label="Overview" id="#overview">
                <el-row style="text-align: left">
                  <el-col :span="6" class="margin-col">
                    <span class="info-item">
                      Number of AMPs:
<!--                      </span>-->
<!--                    <span>-->
                      <el-link href="#amps" type="primary">
                        <span class="info-item-value">{{ num_amps }}</span>
                      </el-link>
                    </span>
<!--                    <div class="info-item" id="sequence">-->
<!--                      Consensus sequence-->
<!--                      <el-button @click="CopyPeptideSequence()" icon="el-icon-document-copy"-->
<!--                                 size="mini" type="primary" plain>-->
<!--                      </el-button>-->
<!--                    </div>-->
<!--                    <pre><code id="aa-sequence">{{ sequence }}</code></pre>-->
<!--                    TODO update this-->
<!--                    <div>-->
<!--                      <el-button type="text" @click="SeqLogoDialogVisible = true">-->
<!--                        Sequence logo-->
<!--                      </el-button>-->
<!--                      <el-dialog-->
<!--                          v-model="SeqLogoDialogVisible"-->
<!--                          title="Tips"-->
<!--                          width="30%"-->
<!--                          :before-close="handleDialogClose">-->
<!--                        <span> {{ downloads[4].file }}</span>-->
<!--                      </el-dialog>-->
<!--                    </div>-->
                    <div style="alignment: left;">
                      <div class="info-item" id="secondary-structure">Secondary Structure</div>
<!--                      TODO change this to an error bars chart.-->
<!--                      https://codepen.io/plotly/pen/VvEVgq-->
                      <Plotly :data="secondaryStructureGraphData"
                              :layout="secondaryStructureLayout()"
                              :toImageButtonOptions="{format: 'svg', scale: 1}"/>
                    </div>

                  </el-col>
                  <el-col :span="14" :offset="2">
                    <!--                   TODO Geographical distribution -->
                    <div id="global distribution">
                      <Plotly :data="GeoPlotData()"
                              :layout="GeoPlotLayout()"
                              :toImageButtonOptions="{format: 'svg', scale: 1}"/>
                    </div>
                  </el-col>
                </el-row>

                <el-divider></el-divider>

                <el-row>
                  <el-col style="margin-left: 30px" :offset="1">
                    <h3 id="distribution" class="subsection-title">Distribution</h3>
                  </el-col>
                </el-row>
                <el-row>
                  <el-col :span="10" class="margin-col">
                    <!--                    TODO Bigger title  and figure captions-->
                    <h4 id="distribution-across-habitats">Habitats</h4>
                    <div>
                      <Plotly :data="EnvPlotData()"
                              :layout="EnvPlotLayout()"
                              :toImageButtonOptions="{format: 'svg', scale: 1}"/>
                    </div>
                  </el-col>
                  <el-col :span="3" style="line-height: 100px">
                    <el-divider direction="vertical"></el-divider>
                  </el-col>

                  <el-col :span="10">
                    <!--                    TODO Bigger title and figure captions -->
                    <h4 id="distribution-across-hosts">Hosts</h4>
                    <div>
                      <Plotly :data="HostPlotData()"
                              :layout="HostPlotLayout()"
                              :toImageButtonOptions="{format: 'svg', scale: 1}"/>
                    </div>
                  </el-col>
                  <!--                <div>-->
                  <!--                  <Plotly :data="DistributionGraphData()"-->
                  <!--                          :layout="DistributionGraphLayout()"-->
                  <!--                          :toImageButtonOptions="{format: 'svg', scale: 1}"/>-->
                  <!--                </div>-->
                </el-row>
                <br/>
                <el-divider></el-divider>
                <el-row>
                  <el-col :offset="1" class="margin-col">
                    <h3 id="amps" class="subsection-title">Associated AMPs</h3>
                    <!--                    TODO add download button here -->
                    <el-table :data="associatedAMPs.currentData" stripe style="width: 100%"
                              v-loading="loading"
                              element-loading-text="Loading..."
                              element-loading-spinner="el-icon-loading">
                      <el-table-column label="Accession" width="200">
                        <template #default="props">
                          <el-button @click="AMPDetail(props.row.accession)" type="text">{{ props.row.accession }}</el-button>
                        </template>
                      </el-table-column>
                      <el-table-column label="Peptide sequence" width="500%">
                        <template #default="props">
                          <pre><code><small>{{ props.row.sequence }}</small></code></pre>
                        </template>
                      </el-table-column>
                      <el-table-column label="# smORF genes" width="150%">
                        <template #default="props">
                          <!--                <el-tooltip class="item" effect="dark" content="Associated number of small ORF genes." placement="right">-->
                          <span>{{ props.row.metadata.info.totalItem }}</span>
                          <!--                </el-tooltip>-->
                        </template>
                      </el-table-column>
                      <el-table-column label="Tag" width="150%">
                        <template #default="props">
                          <el-tag :type="props.row.quality_tag.level"> {{ props.row.quality_tag.msg }} </el-tag>
                          <!--                <el-tag type="warning"> {{ props.row.quality_tag.msg }} </el-tag>-->
                        </template>
                      </el-table-column>
                    </el-table>
                    <el-pagination
                        @size-change="setAMPsPageSize"
                        @current-change="setAMPsPage"
                        :page-sizes="[5, 10, 20, 50, 100]"
                        :page-size="5"
                        layout="total, sizes, prev, pager, next, jumper"
                        :total="associatedAMPs.info.totalRow">
                    </el-pagination>

                  </el-col>
                </el-row>
              </el-tab-pane>
              <el-tab-pane label="Features" id="#features">
                <el-row>
                  <el-col class="margin-col">
                    <h3 id="properties" class="info-item">Biochemical property distributions</h3>
                    <div class="info-item-value">
                      These features below were calculated by using the
                      <el-link href="https://biopython.org/docs/1.79/api/Bio.SeqUtils.ProtParam.html" type="primary">
                        Bio.SeqUtils.ProtParam.ProteinAnalysis
                      </el-link>
                      module from
                      <el-link href="https://doi.org/10.1093/bioinformatics/btp163" type="primary">
                        BioPython
                      </el-link> (version 1.79).
                    </div>
                    <el-row>
                      <el-col :span="7">
                        <Plotly :data="featuresGraphData.MW"
                                :layout="featuresBoxplotLayout('Molecular weight')" />
                      </el-col>
                      <el-col :span="7">
                        <Plotly :data="featuresGraphData.Aromaticity"
                                :layout="featuresBoxplotLayout('Aromaticity')" />
                      </el-col>
                      <el-col :span="7">
                        <Plotly :data="featuresGraphData.GRAVY"
                                :layout="featuresBoxplotLayout('GRAVY (grand average of hydropathy)')" />
                      </el-col>
                    </el-row>
                    <el-row>
                      <el-col :span="7">
                        <Plotly :data="featuresGraphData.Instability_index"
                                :layout="featuresBoxplotLayout('Instability index')" />
                      </el-col>
                      <el-col :span="7">
                        <Plotly :data="featuresGraphData.Isoelectric_point"
                                :layout="featuresBoxplotLayout('Isoelectric point')" />
                      </el-col>
                      <el-col :span="7">
                        <Plotly :data="featuresGraphData.Charge_at_pH_7"
                                :layout="featuresBoxplotLayout('Charge at pH 7.0')" />
                      </el-col>
                    </el-row>


<!--                    <el-table :data="Object.values(feature_statistics).slice(1)" v-loading="loading">-->
<!--                      <el-table-column type="index" :index="indexByStatsName" width="100%"></el-table-column>-->
<!--                      <el-table-column prop="Aromaticity" label="Aromaticity" width="100%"></el-table-column>-->
<!--                      <el-table-column prop="Charge_at_pH_7" label="Charge at pH 7" width="150%"></el-table-column>-->
<!--                      <el-table-column prop="GRAVY" label="GRAVY" width="100%"></el-table-column>-->
<!--                      <el-table-column prop="Instability_index" label="Instability index" width="150%"></el-table-column>-->
<!--                      <el-table-column prop="Isoelectric_point" label="Isoelectric point" width="150%"></el-table-column>-->
<!--                      <el-table-column prop="MW" label="Molecular Weight" width="150%"></el-table-column>-->
<!--                      <el-table-column label="Molar extinction" width="150%">-->
<!--                        <template #default="props">-->
<!--                          {{ props.row.Molar_extinction.cysteines_reduced }}-->
<!--                          {{ props.row.Molar_extinction.cystines_residues }}-->
<!--                        </template>-->
<!--                      </el-table-column>-->
<!--                    </el-table>-->
<!--                    Maybe replace this with a boxplot...-->
                  </el-col>
                </el-row>
              </el-tab-pane>
              <el-tab-pane label="Downloads" id="#downloads">
                <el-row>
                  <el-col class="margin-col">
                    <h3 id="downloads" class="info-item">Downloads</h3>
                    <el-table :data="downloads" v-loading="loading">
                      <el-table-column prop="name" label="Name" width="150%"></el-table-column>
                      <el-table-column prop="file" label="File" width="150%">
                        <template #default="props">
                          <el-link @click.prevent="download(props.row.file)" type="primary"> Download </el-link>
                        </template>
                      </el-table-column>
                      <el-table-column label="Description" width="800%">
                        <template #default="props">
                          <div class="download-desc">{{ props.row.desc }}</div>
                        </template>
                      </el-table-column>
                    </el-table>
                  </el-col>
                </el-row>
              </el-tab-pane>
            </el-tabs>
          </el-main>
        </el-container>
      </el-col>
    </el-row>

  </div>
</template>

<style>
.nav-section {
  font-size: medium;
  font-weight: bold
}
.nav-subsection{
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
.download-desc {
  white-space: pre-wrap;
  word-break: keep-all;
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
import { std, mean } from 'mathjs'

export default {
  name: 'Family_card',
  components: {
    Plotly
  },
  data() {
    let features_base = {
          MW: 0,
          Length: 0,
          Molar_extinction: {cysteines_reduced: 0, cystines_residues: 0},
          Aromaticity: 0,
          GRAVY: 0,
          Instability_index: 0,
          Isoelectric_point: 0,
          Charge_at_pH_7: 0,
          Secondary_structure: {helix: 0, turn: 0, sheet: 0},
        }
    return {
      loading: false,
      SeqLogoDialogVisible: false,
      accession: this.$route.query.accession,
      consensusSequence: '',
      num_amps: 0,
      features: {'': features_base},
      secondaryStructureGraphData: [],
      featuresGraphData: {},
      associatedAMPs: {
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
      downloads: []
    }
  },
  created() {
    let self = this
    // https://stackoverflow.com/questions/50768678/axios-ajax-show-loading-when-making-ajax-request
    this.axios.interceptors.request.use((config) => {
      self.loading = true
      // trigger 'loading=true' event here
      return config;
    }, (error) => {
      self.loading = false
      // trigger 'loading=false' event here
      return Promise.reject(error);
    });
    this.axios.interceptors.response.use((response) => {
      self.loading = false
      // trigger 'loading=false' event here
      return response;
    }, (error) => {
      self.loading = false
      // trigger 'loading=false' event here
      return Promise.reject(error);
    });
    this.getFamily()
    this.setAMPsPageSize(5)
  },
  mounted() {
  },
  computed: {
    currentMetadata () {
      return this.metadata.currentData
    },
    featureStatisticsTable() {
      return this.generateTable()
    }
  },
  methods: {
    getFamily(){
      let self = this
      let fam_accession = this.accession
      this.axios.get('/families/' + fam_accession, {})
          .then(function (response) {
            console.log(response.data)
            // self.consensusSequence = response.data.sequence
            self.num_amps = response.data.num_amps
            self.features = response.data.feature_statistics
            self.distribution = response.data.distributions
            self.downloads = self.toDownloadsTable(response.data.downloads)
            self.secondaryStructureGraphData = self.SecStructureBarData()
            self.featuresGraphData = self.featuresBoxplotData()
            console.log(self.secondaryStructureGraphData)
            console.log(self.featuresGraphData)
          })
          .catch(function (error) {
            console.log(error);
          })
    },
    SecStructureBarData(){
      let probabilities = {
        helix: [],
        sheet: [],
        turn: [],
        disordered: []
      }
      Object.values(this.features).forEach(function(amp_features) {
        console.log(amp_features)
        const amp_structure = amp_features.Secondary_structure
        console.log(amp_structure)
        probabilities.helix.push(amp_structure.helix)
        probabilities.sheet.push(amp_structure.sheet)
        probabilities.turn.push(amp_structure.turn)
        probabilities.disordered.push(1 - amp_structure.helix - amp_structure.sheet - amp_structure.turn)
      })
      console.log(probabilities)
      let data = [{
        x: ['Alpha helix', 'Beta sheet', 'Beta turn', 'Disordered'],
        y: [mean(probabilities.helix), mean(probabilities.sheet),
          mean(probabilities.turn), mean(probabilities.disordered)],
        name: '',
        marker: {color: this.ColorPalette('quanlitative'), size: 4},
        error_y: {
          type: 'data',
          array: [std(probabilities.helix), std(probabilities.sheet),
            std(probabilities.turn), std(probabilities.disordered)],
          visible: true
        },
        type: 'bar'
      }]
      console.log(data)
      return data
    },
    secondaryStructureLayout(){
      return {
        title: {text: ''},
        yaxis: {title: 'Probability'},
        margin: {l: 80, r: 40, t: 20, b: 60, pad: 0},
        showlegend: false,
        height: 300,
        width: 300
      }
    },
    setAMPsPage(page) {
      // this.$message('setting to ' + page + 'th page')
      // Important: page index starting from zero.
      this.associatedAMPs.info.currentPage = page - 1
      console.log(this.associatedAMPs.info.currentPage)
      let config = {
        params: {
          family: this.accession,
          page: this.associatedAMPs.info.currentPage,
          page_size: this.associatedAMPs.info.pageSize
        }
      }
      let self = this
      this.axios.get('/amps/', config)
          .then(function (response) {
            console.log(response.data)
            self.associatedAMPs.currentData = self.initQualityTag(response.data.data)
            self.associatedAMPs.info.totalPage = response.data.info.totalPage
            self.associatedAMPs.info.totalRow = response.data.info.totalItem
          })
          .catch(function (error) {
            console.log(error);
          })
    },
    setAMPsPageSize(size) {
      this.associatedAMPs.info.pageSize = size
      this.setAMPsPage(1)
    },
    handleDialogClose(){
      console.log('dialog closed')
    },
    GeoPlotData(){
      let data = this.distribution.geo
      return [{
        type: 'scattergeo', lat: data.lat, lon: data.lon,
        marker: {
          size: data.size, sizeref: 10,
          // TODO
          // color: this.MapColors(data.colors, this.ColorPalette('quanlitative')),
          line: {color: 'black', size: 2}
        },
      }]
    },
    GeoPlotLayout(){
      return {
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
        margin: {l: 0, r: 0, t: 0, b: 0}
      }
    },
    EnvPlotData(){
      let data = this.distribution
      let env_data = {
        type: "sunburst",
        labels: data.habitat.labels, //["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parents: data.habitat.parents, //["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
        values:  data.habitat.values, //[65, 14, 12, 10, 2, 6, 6, 4, 4],
        leaf: {opacity: 0.4},
        // marker: {line: {"width": 2}},
        branchvalues: 'total'
      }
      return [env_data]
    },
    EnvPlotLayout(){
      return {
        margin: {l: 40, r: 40, b: 40, t: 40}, autosize: true,
        sunburstcolorway: this.ColorPalette('quanlitative')
      };
    },
    HostPlotData(){
      let data = this.distribution
      let host_data = {
        type: "sunburst",
        labels: data.host.labels, //["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parents: data.host.parents, //["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
        values:  data.host.values, //[65, 14, 12, 10, 2, 6, 6, 4, 4],
        leaf: {opacity: 0.4},
        // marker: {line: {"width": 2}},
        branchvalues: 'total'
      }
      return [host_data]
    },
    HostPlotLayout(){
      return {
        margin: {l: 40, r: 40, b: 40, t: 40}, autosize: true,
        sunburstcolorway: this.ColorPalette('quanlitative')
      };
    },
    DistributionGraphData(){
      let data = this.distribution
      let habitat_data = {
        type: "sunburst",
        labels: data.habitat.labels, //["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parents: data.habitat.parents, //["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
        values:  data.habitat.values, //[65, 14, 12, 10, 2, 6, 6, 4, 4],
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
    DistributionGraphLayout(){
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
            label: 'Hosts'},
          ]}
        ]}
    },
    featureGraphData(){
      let self = this
      let data = self.feature_statistics.graph_points
      let line = {color: 'blue'}
      return [
        {x: data.transfer_energy.x, y: data.transfer_energy.y, line: line, marker: {color: data.transfer_energy.c}, visible: true,},
        {x: data.flexibility.x, y: data.flexibility.y, line: line, visible: false},
        {x: data.hydrophobicity_parker.x, y: data.hydrophobicity_parker.y, line: line, visible: false},
        {x: data.surface_accessibility.x, y: data.surface_accessibility.y, line: line, visible: false}
      ]
    },
    featureGraphLayout(){
      return {
        height: 400, margin: {l: 100, r: 100, b: 80, t: 40},
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
    comparisonGraphData(){
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
    comparisonGraphLayout(){
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
    featuresBoxplotData(){
      let colors = ['rgba(93, 164, 214, 0.5)', 'rgba(255, 144, 14, 0.5)', 'rgba(44, 160, 101, 0.5)',
        'rgba(255, 65, 54, 0.5)', 'rgba(207, 114, 255, 0.5)', 'rgba(127, 96, 0, 0.5)',
        'rgba(255, 140, 184, 0.5)', 'rgba(79, 90, 117, 0.5)', 'rgba(222, 223, 0, 0.5)']
      let MW = [],
          Aromaticity = [],
          GRAVY = [],
          Instability_index = [],
          Isoelectric_point = [],
          Charge_at_pH_7 = []
      // console.log(MW)
      // let Molar_extinction = {
      //   cysteines_reduced: [],
      //   cystines_residues: []
      // }
      for (const amp_features of Object.values(this.features)){
        MW.push(amp_features.MW)
        // console.log(Molar_extinction)
        // console.log(Molar_extinction.cystines_residues)
        // Molar_extinction.cystines_residues.push(amp_features.Molar_extinction.cystines_residues)
        // Molar_extinction.cysteines_reduced.push(amp_features.Molar_extinction.cysteines_reduced)
        Aromaticity.push(amp_features.Aromaticity)
        GRAVY.push(amp_features.GRAVY)
        Instability_index.push(amp_features.Instability_index)
        Isoelectric_point.push(amp_features.Isoelectric_point)
        Charge_at_pH_7.push(amp_features.Charge_at_pH_7)
      }
      return {
        MW: [this.makefeaturesBoxplotTrace(MW, colors[0])],
        // this.makeTrace(Molar_extinction.cysteines_reduced, "Molar extinction (cysteines_reduced)", colors[2]),
        // this.makeTrace(Molar_extinction.cystines_residues, "Molar extinction (cystines residues)", colors[3]),
        Aromaticity: [this.makefeaturesBoxplotTrace(Aromaticity, colors[4])],
        GRAVY: [this.makefeaturesBoxplotTrace(GRAVY, colors[5])],
        Instability_index: [this.makefeaturesBoxplotTrace(Instability_index, colors[6])],
        Isoelectric_point: [this.makefeaturesBoxplotTrace(Isoelectric_point, colors[7])],
        Charge_at_pH_7: [this.makefeaturesBoxplotTrace(Charge_at_pH_7, colors[8])],
      }
    },
    featuresBoxplotLayout(name){
      return {
        title: name,
        autosize: true,
        margin: {l: 50, r: 20, b: 20, t: 80},
        // height: 300,
        // width: 300,
      }
    },
    makefeaturesBoxplotTrace(data, color){
      return {
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
        fillcolor: color,
        opacity: 0.6,
        meanline: {
          visible: true
        },
        name: ''
        // x0: ''
      }
      // return {
      //   name: '',
      //   type: 'violin',
      //   y: data,
      //   hoverinfo: 'y',
      //   // xaxis:{
      //   //   ticks: '',
      //   // },
      //   // boxpoints: 'none',
      //   // jitter: 0.5,
      //   // whiskerwidth: 0.2,
      //   // fillcolor: 'cls',
      //   marker: {size: 2, color: color},
      //   line: {width: 1}
      // };
    },
    MapColors(categories, colors){
      const levels = [...new Set(categories)]
      console.log(levels)
      const mapping = []
      for (let i=0; i<=categories.length; i++){
        mapping[levels[i]] = colors[i]
      }
      return categories.map(function (cate) {
        return mapping[cate]
      })
    },
    ColorPalette(kind){
      if (kind === 'sequential'){
        return ['#ffffe5', '#fff7bc', '#fee391', '#fec44f', '#fe9929', '#ec7014', '#cc4c02', '#8c2d04']
      }
      else if (kind === 'diverging'){
        return ['#8c510a', '#bf812d', '#dfc27d', '#f6e8c3', '#c7eae5', '#80cdc1', '#35978f', '#01665e']
      }
      else if (kind === 'quanlitative'){
        return ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#e6ab02', '#a6761d', '#666666']
      }
      else{
        console.log('please set the `kind` option for color palette.')
        return null
      }
    },
    exportSVG(){
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
    getFamilyPageURL(){
      return "http://119.3.63.164/family?accession=" + this.family
    },
    CopyPeptideSequence(){
      clipboard.writeText(this.sequence).then(
          () => { console.log("success!"); },
          () => { console.log("error!"); }
      )
      this.$message('Amino acid sequence copied!')
    },
    makeTraceVisible(index, totalTrace){
      var visibility = []
      for (var i=0; i<totalTrace; i++){
        visibility[i] = false
      }
      visibility[index] = true
      console.log(visibility)
      return visibility
    },
    UnpackCol(rows, key) {
      return rows.map(function(row) { return row[key]; });
    },
    initQualityTag(amps){
      for (let i=0; i < amps.length; i++) {
        Object.assign(amps[i], {quality_tag: {msg: 'Not available', level: 'warning'}})
      }
      return amps
    },
    downloadCurrPage(){
      print()
    },
    AMPDetail(accession){
      window.open('/amp?accession='+accession, '_blank')
    },
    indexByStatsName(index){
      return Object.keys(this.features)[index + 1]
    },
    toDownloadsTable(downloads){
      let tableData = []
      for(const [key, value] of Object.entries(downloads)){
        let desc = ''
        let name = ''
        if (key === "alignment"){
          name = 'Alignment'
          desc = 'Alignment - protein-aligned sequences belonging to this family in fasta format'
        } else if (key === "sequences") {
          name = 'Sequences'
          desc = 'Sequences - fasta file containing the peptide sequences belonging to this family'
        } else if (key === "hmm_logo") {
          name = 'HMM-logo'
          desc = 'HMM-logo - graphical representation of the Hidden Markov Model describing the peptides of this family'
        } else if (key === "hmm_profile") {
          name = 'HMM-profile'
          desc = 'HMM-profile - Statistical Hidden Markov Model describing the peptides of this family, used to sequence searching'
        } else if (key === "sequence_logo") {
          name = 'Sequence-logo'
          desc = 'Sequence-logo - graphical representation of the peptides alignment, the bit-wise information per position is shown'
        } else if (key === "tree_figure") {
          name = 'Tree-figure'
          desc = 'Tree-figure - ASCII graphical representation of the phylogenetic tree of peptides composing this family. Branches were drawn proportionally to the substitution distance and the node support is given as bootstrap of 1000 pseudoreplicates'
        } else if (key === "tree_nwk") {
          name = 'Tree-newick'
          desc = 'Tree-newick - phylogenetic tree of peptides composing the family in Newick format, compatible to different tree rendering programs, obtained using FastTree2.'
        } else {
          console.log('unknown type of download.')
        }
        tableData.push({name: name, file: value, desc: desc})
      }
      return tableData
    },
    download(url){
      console.log(url)
      window.open(encodeURI(url), '_blank')
    },
    descStyle(){
      return 'download-desc'
    },
  }
}
// window.addEventListener("DOMContentLoaded", function () {
//   const button = document.body.appendChild(document.createElement("button"));
//   button.textContent = "Copy";
//   button.addEventListener("click", this.CopyPeptideSequence);
// });
</script>
