<template>
 <div class="AMP_card">
    <el-row>
      <el-col :span="22" :offset="1">
        <el-container>
          <el-main>
            <div class="title">Antimicrobial peptide: {{ accession }}
              <el-button class="button" @click="downloadCurrPage()" type="primary" icon="el-icon-download" plain></el-button>
            </div>
<!--          TODO test: move this description down to the overview tab-->
            <div class="description">
              The AMP belongs to
              <el-link :href="getFamilyPageURL()" type="primary">
                <span class="description">{{ family }}</span>
              </el-link>
              family and has {{length}} amino acid residues.
            </div>

            <el-tabs type="border-card">
              <el-tab-pane label="Overview">
                <el-row style="text-align: left">
                  <el-col :span="6" style="margin-left: 30px">
                    <div class="info-item" id="sequence">
                      Peptide sequence
                      <el-button @click="CopyPeptideSequence()" icon="el-icon-document-copy"
                                 size="mini" type="primary" plain>
<!--                        Copy-->
                      </el-button>
                    </div>
                    <pre><code id="aa-sequence">{{ sequence }}</code></pre>
                    <div style="alignment: left;">
                      <div class="info-item" id="secondary-structure">Secondary Structure</div>
                      <Plotly :data="SecStructurePieData()"
                              :layout="{title: {text: 'Secondary Structure'},
                            margin: {l: 0, r: 0, t: 0, b: 0, pad: 0},
                            showlegend: false, height: 240, width: 240}"
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
                  <el-col :span="10" style="magrin-left: 30px">
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
                  <el-col style="margin-left: 30px" :offset="1">
                    <h3 id="relationships" class="subsection-title">Relationships</h3>
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
                      <el-table-column prop="origin_scientific_name" label="Origin" sortable width="150%"/>
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
<!--                      <el-pagination-->
<!--                          @current-change="setMetadataPage"-->
<!--                          :page-size="metadata.info.pageSize"-->
<!--                          layout="total, prev, pager, next, jumper"-->
<!--                          :total="metadata.info.totalRow"-->
<!--                      >-->
<!--                      </el-pagination>-->
  <!--                    FIXME integrate pagination buttons with the table-->
                    </div>

                  </el-col>
                </el-row>
              </el-tab-pane>
              <el-tab-pane label="Features">
                <h3 id="properties">Biochemical properties</h3>
                <el-col :span="12">
                  <div style="text-align: left">
                    <div>
                    <span class="info-item" id="charge-neutral-pH">Charge at pH 7.0: </span>
                    <span class="info-item-value">{{ features.Charge_at_pH_7 }} </span>
                    </div>
                    <div>
                    <span class="info-item" id="isoeletric-point">Isoeletric point: </span>
                    <span class="info-item-value"> {{ features.Isoelectric_point }} </span>
                    </div>
                    <div>
                    <span class="info-item" id="molar-extinction">Molar extinction: </span>
                    <span class="info-item-value">
                      {{ features.Molar_extinction.cysteines_reduced }}
                      {{ features.Molar_extinction.cystines_residues }}
                    </span>
                    </div>
                    <div>
                    <span class="info-item" id="aromaticity">Aromaticity: </span>
                    <span class="info-item-value">{{ features.Aromaticity }}</span>
                    </div>
                    <div>
                    <span class="info-item" id="gravy">GRAVY: </span>
                    <span class="info-item-value"> {{ features.GRAVY }}</span>
                    </div>
                    <div>
                    <span class="info-item" id="instability-index">Instability index: </span>
                    <span class="info-item-value">{{ features.Instability_index }}</span>
                    </div>
                  </div>
                </el-col>
                <el-col :span="6" :offset="2">
                  <div style="text-align: center" id="helical-wheel">
                    <el-link :href="helicalwheel"
                             target="_blank"
                             type="primary">
                      <span class="medium">Helical wheel</span>
                    </el-link>
                    <br/>
                    Amino acids helical wheel with the H-moment indicated.
                  </div>
                  <div style="align-content: center; text-align: center;">
                    <el-image :src="helicalwheel"></el-image>
                    <!--                  TODO directly include svg file here, not inplace generation-->
                    <!--                  TODO https://observablehq.com/@smsaladi/helical-wheel-visualization-wip-2019_05_10-->
                    <!--                  TODO inplacely generate helicalwheel using echarts-->
                    <!--                  https://github.com/ecomfe/vue-echarts/blob/5.x/README.zh_CN.md-->
                    <!--                  https://echarts.apache.org/examples/zh/editor.html?c=graph-circular-layout-->
                  </div>
                </el-col>

                <br>
                <!--            <h3 id="graphs">Graphs</h3>-->
                <el-row>
                  <el-col>
                    <!--                  <h4 id="features">Features</h4>-->
                    <div>
                      <Plotly :data="featureGraphData()"
                              :layout="featureGraphLayout()"
                              :toImageButtonOptions="{format: 'svg', scale: 1}"/>
                    </div>
                    EZenergy.  xxxxx. Flexibility.  xxxxx.  Hydrophobicity Parker. xxxxx.
                  </el-col>
                </el-row>
                <br/>
              </el-tab-pane>
            </el-tabs>
<!--            <h3 id="general_info">General information</h3>-->

<!--              <el-row style="text-align: left">-->
<!--                <ul>-->
<!--                  <li><span class="info-item" id="relationships">Relationships</span>-->
<!--                    <el-tooltip class="item" content="Download relationships table" placement="right">-->
<!--                      <el-button @click="downloadRelationshipsTable()" type="text"-->
<!--                                 icon="el-icon-download" circle></el-button>-->
<!--                    </el-tooltip>-->
<!--                  </li>-->
<!--                  <el-table :data="relationships.currentTableData" height="250" style="width: 100%" size="mini">-->
<!--                    <el-table-column prop="GMSC" label="Genes" width="250%"/>-->
<!--&lt;!&ndash;                    TODO display gene sequence here.&ndash;&gt;-->
<!--                    <el-table-column prop="Source" label="Sample/Genome" width="250%"/>-->
<!--&lt;!&ndash;                    <el-table-column prop="taxid" label="Taxon id" width="100%"/>&ndash;&gt;-->
<!--                    <el-table-column prop="sciname" label="Name" width="250%"/>-->
<!--                  </el-table>-->
<!--                  <div class="block">-->
<!--                    <el-pagination-->
<!--                        @current-change="setRelationshipTablePage"-->
<!--                        :page-size="relationships.pageSize"-->
<!--                        layout="total, prev, pager, next"-->
<!--                        :total="relationships.tableData.length"-->
<!--                    >-->
<!--                    </el-pagination>-->
<!--&lt;!&ndash;                    FIXME integrate pagination buttons with the table&ndash;&gt;-->
<!--                  </div>-->
<!--                </ul>-->
<!--                </el-row>-->
<!--            <el-card>-->
<!--              <el-row>-->
<!--                <el-col>-->
<!--                  <h4 id="comparisons">Comparison with entire database</h4>-->
<!--                  <div><Plotly :data="comparisonGraphData()" :layout="comparisonGraphLayout()"></Plotly></div>-->
<!--                  Z-score comparison of (a) aliphatic index, (b) Boman index, (c) hydrophobic moment, (d) instability index - instaindex, (e) isoelectric point, and (f) charge using the average of complete training set separated by non-antimicrobial peptides (gray), antimicrobial peptides (black) and dots representing the peptide as a red star.-->
<!--                </el-col>-->
<!--              </el-row>-->
<!--            </el-card>-->
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
//import { tsvParse } from 'd3-dsv'
// import * as d3 from "d3-dsv";



export default {
  name: 'AMP_card',
  components: {
    Plotly
  },
  data() {
    return {
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
      helicalwheel: require('./../assets/images/helicalwheel_AMP10.000_000.png'),
    }
    },
  created() {
    this.getAMP()
  },
  mounted() {
    this.setMetadataPageSize(5)
  },
  computed: {
    currentMetadata () {
      return this.metadata.currentData
    }
  },
  methods: {
    getAMP(){
      let self = this
      let amp_accession = self.$route.query.accession
      this.axios.get('/amps/' + amp_accession, {})
        .then(function (response) {
          console.log(response.data)
          self.sequence = response.data.sequence
          self.length = response.data.sequence.length;
          self.family = response.data.family
          self.features = response.data.features
          self.metadata.currentData = response.data.metadata.data
          self.metadata.info.currentPage = 1
          self.metadata.info.totalPage = response.data.metadata.info.totalPage
          self.metadata.info.totalRow = response.data.metadata.info.totalItem
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
    SecStructurePieData(){
      let strucData = this.features.Secondary_structure
      strucData.disordered = 1 - strucData.turn - strucData.helix - strucData.sheet
      return [{
        type: 'pie', values: Object.values(strucData), labels: Object.keys(strucData),
        marker: {colors: this.ColorPalette('quanlitative')},
        textinfo: "label+percent", insidetextorientation: "radial"}]
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
    GeoPlotData(){
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
        margin: {
          l: 0,
          r: 0,
          t: 0,
          b: 0
        }
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
      let data = self.features.graph_points
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
    downloadCurrPage(){
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
