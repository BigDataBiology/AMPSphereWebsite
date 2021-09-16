<template>
 <div class="AMP_card">
    <el-row>
      <el-col :span="22" :offset="1">
        <el-container>
          <sidebar-menu :menu="menu" />
          <el-aside>
            <el-menu :unique-opened="true" style="position: fixed; top:240px; text-align: left; width:250px">
              <el-submenu index="1">
                <template #title>
                  <i class="el-icon-info"></i>
                <el-link class="nav-section" href="#general_info">General information</el-link>
              </template>
                <el-menu-item><el-link class="nav-subsection" href="#family">Family</el-link></el-menu-item>
                <el-menu-item><el-link class="nav-subsection" href="#length">Peptide length</el-link></el-menu-item>
                <el-menu-item><el-link class="nav-subsection" href="#molecular-weight">Molecular weight</el-link></el-menu-item>
                <el-menu-item><el-link class="nav-subsection" href="#sequence">Sequence</el-link></el-menu-item>
<!--                <el-menu-item><el-link class="nav-subsection" href="#gene-sequence">Gene sequence</el-link></el-menu-item>-->
                <el-menu-item><el-link class="nav-subsection" href="#relationships">Relationships</el-link></el-menu-item>
                <el-menu-item><el-link class="nav-subsection" href="#secondary-structure">Secondary structure</el-link></el-menu-item>
              </el-submenu>
              <el-submenu index="2">
                <template #title>
                  <i class="el-icon-info"></i>
                  <el-link class="nav-section" href="#distribution">Distribution</el-link>
                </template>
                <el-menu-item><el-link class="nav-subsection" href="#global-distribution">Global</el-link></el-menu-item>
                <el-menu-item><el-link class="nav-subsection" href="#distribution-across-habitats">Habitats</el-link></el-menu-item>
                <el-menu-item><el-link class="nav-subsection" href="#distribution-across-hosts">Hosts</el-link></el-menu-item>
              </el-submenu>
              <el-submenu index="3">
                <template #title>
                  <i class="el-icon-info"></i>
                  <el-link class="nav-section" href="#properties">Properties</el-link>
                </template>
                <el-menu-item><el-link type="info" class="nav-subsection" href="#charge-neutral-pH">Charge at neutral pH</el-link></el-menu-item>
                <el-menu-item><el-link class="nav-subsection" href="#isoeletric-point">Isoeletric point</el-link></el-menu-item>
                <el-menu-item><el-link class="nav-subsection" href="#molar-extinction">Molar extinction</el-link></el-menu-item>
                <el-menu-item><el-link class="nav-subsection" href="#aromaticity">Aromaticity</el-link></el-menu-item>
                <el-menu-item><el-link class="nav-subsection" href="#gravy">GRAVY</el-link></el-menu-item>
                <el-menu-item><el-link class="nav-subsection" href="#instability-index">Instability index</el-link></el-menu-item>
                <el-menu-item><el-link class="nav-subsection" href="#helical-wheel">Helical wheel</el-link></el-menu-item>
              </el-submenu>
              <el-submenu index="4">
                <template #title>
                  <i class="el-icon-info"></i>
                  <el-link class="nav-section" href="#graphs">Graphs</el-link>
                </template>
                <el-menu-item><el-link class="nav-subsection" href="#features">Features</el-link></el-menu-item>
                <el-menu-item><el-link class="nav-subsection" href="#comparisons">Comparisons</el-link></el-menu-item>
              </el-submenu>
            </el-menu>
          </el-aside>
          <el-main>
<!--            <el-table-column prop="Accession" label="Accession" width="200%"></el-table-column>-->
            <span>
              <h1>Antimicrobial peptide: {{ accession }}
                <el-button class="button" @click="downloadCurrPage()" type="primary" icon="el-icon-download" circle></el-button>
              </h1>
            </span>

<!--            <h3 id="general_info">General information</h3>-->
              <el-row style="text-align: left">
                <el-col :span="16">
                  <ul>
                    <li><span class="info-item" id="family">Family</span>: {{ family }}</li>
                    <br/>
                    <li><span class="info-item" id="length">Length</span>: {{ length }}</li>
                    <br/>
                    <li><span class="info-item" id="molecular-weight">Molecular weight</span>: {{ features.MW }} </li>
                    <br/>
                    <li><span class="info-item" id="sequence">Sequence</span>: {{ sequence }}</li>
<!--                    <br/>-->
<!--                    <li><span class="info-item" id="gene-sequence">Gene sequence</span>: {{ AMP.Info.GeneSequence }}</li>-->
                  </ul>
                </el-col>
                <el-col :span="6">
                  <div id="secondary-structure" style="height: 180px;">
<!--                    <Plotly :data="SecStructureData()" :layout="SecStructureLayout()"/>-->
                    <Plotly :data="SecStructurePieData()"
                            :layout="{title: {text: 'Secondary Structure'},
                            margin: {l: 0, r: 0, t: 0, b: 0, pad: 0},
                            showlegend: false, height: 180}"
                            :toImageButtonOptions="{format: 'svg', scale: 1}"/>
                  </div>
                </el-col>
              </el-row>
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

            <br/>

            <hr>
            <h3 id="distribution">Distribution</h3>
              <el-row>
<!--                <h4 id="global-distribution">Global distribution</h4>-->
                <Plotly :data="GeoPlotData()"
                        :layout="GeoPlotLayout()"
                        :toImageButtonOptions="{format: 'svg', scale: 1}"/>
              </el-row>
              <el-row>
                <el-col :span="12">
                  <h4 id="distribution-across-habitats">Across habitats</h4>
                  <div>
                    <Plotly :data="EnvPlotData()"
                            :layout="EnvPlotLayout()"
                            :toImageButtonOptions="{format: 'svg', scale: 1}"/>
                  </div>
                </el-col>
                <el-col :span="12">
                  <h4 id="distribution-across-hosts">Across hosts</h4>
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
            <hr>
            <h3 id="properties">Biochemical properties</h3>
              <el-col :span="12">
              <div style="text-align: left">
<!--                More spaces-->
                <ul>
                  <li><span class="info-item" id="charge-neutral-pH">Charge at pH 7.0</span>: {{ features.Charge_at_pH_7 }}</li>
                  <br/>
                  <li><span class="info-item" id="isoeletric-point">Isoeletric point</span>: {{ features.Isoelectric_point }}</li>
                  <br/>
                  <li><span class="info-item" id="molar-extinction">Molar extinction</span>:
                    {{ features.Molar_extinction.cysteines_reduced }}
                    {{ features.Molar_extinction.cystines_residues }}
                  </li>
                  <br/>
                  <li><span class="info-item" id="aromaticity">Aromaticity</span>: {{ features.Aromaticity }}</li>
                  <br/>
                  <li><span class="info-item" id="gravy">GRAVY</span>: {{ features.GRAVY }}</li>
                  <br/>
                  <li><span class="info-item" id="instability-index">Instability index</span>: {{ features.Instability_index }}</li>
                </ul>
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
  .info-item {
    font-weight: bold;
    color: #063d7c;
    font-size: large;
  }
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
        Molar_extinction: {
          cysteines_reduced: 0,
          cystines_residues: 0
        },
        Aromaticity: 0,
        GRAVY: 0,
        Instability_index: 0,
        Isoelectric_point: 0,
        Charge_at_pH_7: 0,
        Secondary_structure: {
          helix: 0,
          turn: 0,
          sheet: 0
        },
        graph_points: {
          transfer_energy: {
            type: "line plot",
            x: [],
            y: [],
            c: []
            },
          hydrophobicity_parker: {
            type: "line plot",
            x: [],
            y: [],
            c: []
          },
          surface_accessibility: {
            type: "line plot",
            x: [],
            y: [],
            c: []
          },
          flexibility: {
            type: "line plot",
            x: [],
            y: [],
            c: []
          }
        }
      },
      metadata: [],
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
      relationships: {
        page: 1,
        pageSize: 6,
        currentTableData: [
          {GMSC: 'GMSC10.SMORF.000_036_844_556', Source: 'SAMEA104142073', taxid: 237, sciname: 'Phocaeicola'},
        ],
        tableData: [
        {GMSC: 'GMSC10.SMORF.000_036_844_556', Source: 'SAMEA104142073', taxid: 237, sciname: 'Phocaeicola'},
        {GMSC: 'GMSC10.SMORF.001_828_692_528', Source: 'SAMN03955567', taxid: 237, sciname: 'Phocaeicola'},
        {GMSC: 'GMSC10.SMORF.001_828_750_506', Source: 'SAMN03955549', taxid: 237, sciname: 'Phocaeicola'},
        {GMSC: 'GMSC10.SMORF.001_828_786_262', Source: 'SAMN03955576', taxid: 237, sciname: 'Phocaeicola'},
        {GMSC: 'GMSC10.SMORF.001_828_803_495', Source: 'SAMN03955558', taxid: 237, sciname: 'Phocaeicola'},
        {GMSC: 'GMSC10.SMORF.001_828_863_094', Source: 'SAMN03955541', taxid: 237, sciname: 'Phocaeicola'},
        {GMSC: 'GMSC10.SMORF.001_828_884_876', Source: 'SAMN03955550', taxid: 488, sciname: 'Phocaeicola dorei'},
        {GMSC: 'GMSC10.SMORF.001_828_927_346', Source: 'SAMN05930844', taxid: 237, sciname: 'Phocaeicola'},
        {GMSC: 'GMSC10.SMORF.001_829_153_490', Source: 'SAMN05930833', taxid: 237, sciname: 'Phocaeicola'},
        {GMSC: 'GMSC10.SMORF.001_829_180_169', Source: 'SAMN05930842', taxid: 238, sciname: 'Phocaeicola vulgatus'},
      ]},
      helicalwheel: require('./../assets/images/helicalwheel_AMP10.000_000.png'),
    }
    },
  mounted() {
    // this.setRelationshipTablePage(1)
    console.log('setting first page')
    this.getAMP()
  },
  computed: {
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
          self.metadata = response.data.metadata
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
    SecStructureData(){
      let strucData = this.features.Secondary_structure
      return [{
        x: [strucData.helix],
        y: [''],
        name: 'Alpha helix',
        orientation: 'h',
        type: 'bar',
        marker: {width: 0.5},
      },{
        x: [strucData.turn],
        y: [''],
        name: 'Beta turn',
        orientation: 'h',
        type: 'bar',
        marker: {width: 0.5},
      },{
        x: [strucData.sheet],
        y: [''],
        name: 'Beta sheet',
        orientation: 'h',
        type: 'bar',
        marker: {width: 0.5},
      },{
        x: [100 - strucData.turn - strucData.helix - strucData.sheet],
        y: [''],
        name: 'Disordered',
        orientation: 'h',
        type: 'bar',
        marker: {width: 0.5},
      }]
    },
    SecStructureLayout(){
      return {
        margin: {l: 0, r: 0, t: 0, b: 0},
        barmode: 'stack',
        legend: {orientation: "h", xanchor: "center", x: 0.5, y: 0.95},
      }
    },
    SecStructurePieData(){
      let strucData = this.features.Secondary_structure
      strucData.disordered = 1 - strucData.turn - strucData.helix - strucData.sheet
      return [{
        type: 'pie',
        values: Object.values(strucData),
        labels: Object.keys(strucData),
        marker:{
          colors: this.ColorPalette('quanlitative'),
        },
        textinfo: "label+percent",
        insidetextorientation: "radial"}]
    },
    // setRelationshipTablePage (val) {
    //   let self = this
    //   self.AMP.relationships.page = val
    //   self.AMP.relationships.currentTableData = this.AMP.relationships.tableData.slice(
    //       this.AMP.relationships.pageSize * this.AMP.relationships.page -
    //       this.AMP.relationships.pageSize, this.AMP.relationships.pageSize * this.AMP.relationships.page)
    // },
    GeoPlotData(){
      // let GeoString = "n\tenvironmental_features\tlatitude\tlongitude\tMO-level-I\n" +
      //   "10\thuman-associated habitat [ENVO:00009003]\t39.9\t116.25\tTerrestrial\n" +
      //   "70\thuman-associated habitat [ENVO:00009003]\t37.27567620000001\t-104.65581230000001\tTerrestrial\n" +
      //   "10\tanimal-associated habitat [ENVO:00006776]\t52.13\t5.29\tTerrestrial\n" +
      //   "10\thuman-associated habitat [ENVO:00009003]\t34.5\t109.5\tTerrestrial\n" +
      //   "10\thuman-associated habitat [ENVO:00009003]\t39.9\t116.25\tTerrestrial\n" +
      //   "10\thuman-associated habitat [ENVO:00009003]\t47.3\t106.15\tTerrestrial\n" +
      //   "30\thuman-associated habitat [ENVO:00009003]\t56.21285989999999\t9.3005073\tTerrestrial\n" +
      //   "10\thuman-associated habitat [ENVO:00009003]\t38.626999999999995\t-90.1994\tTerrestrial\n" +
      //   "10\thuman-associated habitat [ENVO:00009003]\t30.3\t120.2\tTerrestrial\n" +
      //   "30\thuman-associated habitat [ENVO:00009003]\t56.21285989999999\t9.3005073\tTerrestrial"
      // let geoData = d3.tsvParse(GeoString, d3.autoType)
      // console.log(geoData)
      // return [{
      //   type: 'scattergeo',
      //   //locationmode: 'USA-states',
      //   lat: this.UnpackCol(geoData, 'latitude'),
      //   lon: this.UnpackCol(geoData, 'longitude'),
      //   marker: {
      //     size: this.UnpackCol(geoData, 'n'),
      //     color: this.MapColors(this.UnpackCol(geoData, 'MO-level-I'), this.ColorPalette('quanlitative')),
      //     line: {
      //       color: 'black',
      //       size: 2
      //     }
      //   },
      // }]
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
          l: 30,
          r: 30,
          t: 30,
          b: 30
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
    //   function makeTrace(i) {
    //     return {
    //       y: Array.apply(null, Array(100)).map(() => Math.random()),
    //       line: {
    //         color: 'black'
    //       },
    //       visible: i === 0,
    //       //name: ['EZenergy', 'Flexibility', 'Hydrophobicity Parker', 'SA AMPs'].slice(i),
    //     };
    //   }
    //   return [0, 1, 2, 3].map(makeTrace)
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
</script>
