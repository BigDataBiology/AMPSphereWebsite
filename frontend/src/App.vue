<!--<template>-->
<!--  <meta name="viewport" content="width=device-width, initial-scale=1.0">-->

<!--  <div id="AMPSphere">-->
<!--    <el-container>-->
<!--      <el-header height="150px">-->
<!--        <div class="header-wrapper">-->
<!--          <div class="logo">-->
<!--            <el-image styles="height: 150px; width: 150px" :src="url" lazy></el-image>-->
<!--          </div>-->
<!--          <div class="search-box">-->
<!--            <span>-->
<!--              <el-input placeholder="Text search" v-model="searchTerm" @keyup.enter="textSearch" clearable-->
<!--                                    maxlength="40" show-word-limit=true>-->
<!--              <template #append>-->
<!--                <el-button type="primary" icon="el-icon-search" @click="textSearch">Search</el-button>-->
<!--              </template>-->
<!--              </el-input>-->
<!--&lt;!&ndash;              <el-button type="primary" icon="el-icon-search" @click="textSearch">Search</el-button>&ndash;&gt;-->
<!--            </span>-->
<!--            <span>-->
<!--              <br/><br/>-->
<!--              Examples:-->
<!--              <el-link href="/AMP?accession=AMP10.000_001" target="_blank" type="primary">AMP10.000_001</el-link>,-->
<!--              <el-link href="/family?accession=SPHERE-III.001_396" target="_blank" type="primary">SPHERE-III.001_396</el-link>,-->
<!--              <el-link href="/text_search?query=Aquatic" target="_blank" type="primary">Aquatic</el-link>,-->
<!--              <el-link href="/text_search?query=Homo sapiens" target="_blank" type="primary">Homo sapiens</el-link>-->
<!--            </span>-->
<!--          </div>-->
<!--          <div class="menu">-->
<!--            <el-menu mode="horizontal" :default-active="activeMenuItem" :router="true">-->
<!--              <el-menu-item index="home">Home</el-menu-item>-->
<!--              <el-menu-item index="browse_data">Browse data</el-menu-item>-->
<!--              <el-menu-item index="api">API</el-menu-item>-->
<!--              <el-menu-item index="about">About</el-menu-item>-->
<!--              <el-menu-item index="downloads">Downloads</el-menu-item>-->
<!--              <el-menu-item index="contact">Contact</el-menu-item>-->
<!--            </el-menu>-->
<!--          </div>-->
<!--        </div>-->
<!--      </el-header>-->

<!--      <el-main>-->
<!--&lt;!&ndash;        Use CDN to speed up the production build: https://segmentfault.com/a/1190000015709430&ndash;&gt;-->
<!--        <el-row>-->
<!--          <el-col :offset="1" :span="22">-->
<!--            <div>-->
<!--              <router-view/>-->
<!--            </div>-->
<!--          </el-col>-->
<!--        </el-row>-->
<!--      </el-main>-->

<!--      <el-footer height="120px">-->
<!--        <el-row type="flex" justify="center">-->
<!--          <el-col :span="22" :offset="1" type="flex" justify="bottom">-->
<!--            <el-divider></el-divider>-->
<!--            Powered by-->
<!--            <el-link href="https://vuejs.org/index.html" type="success">Vue.js</el-link>-->
<!--            <el-divider direction="vertical"></el-divider>-->
<!--            <el-link href="https://element-plus.org/#/en-US" type="primary">Element</el-link>-->
<!--            <el-divider direction="vertical"></el-divider>-->
<!--            <el-link href="https://fastapi.tiangolo.com/" type="success">FastAPI</el-link>-->
<!--          </el-col>-->
<!--        </el-row>-->
<!--        <el-row type="flex" justify="center">-->
<!--          <el-col :span="22" :offset="1" type="flex" justify="bottom">-->
<!--            &copy;2021-{{year}}-->
<!--            <el-link href="https://www.fudan.edu.cn/" type="warning">Fudan University</el-link>-->
<!--            All Rights Reserved.-->
<!--          </el-col>-->
<!--        </el-row>-->
<!--      </el-footer>-->
<!--    </el-container>-->
<!--  </div>-->
<!--</template>-->
<template>
  <div id="AMPSphere" class="q-pa-md">
  <q-layout view="hHh lpR fFf" class="shadow-2 rounded-borders">
    <q-header reveal bordered class="bg-white text-black" reveal-offset="100px" height-hint="160" style="height: 160px">
      <div class="row q-pl-auto q-pr-auto" style="height: 150px">
        <div class="col-xs-0 col-sm-1 col-md-2 bg-white"></div>
        <div class="col-xs-12 col-sm-10 col-md-8">
          <div class="row justify-center q-my-none q-pb-none" style="height: 100px">
            <div class="col-xs-4 col-sm-2 col-md-1">
              <q-img :src="require('./assets/logo.png')" sizes="(max-width: 100px) 100px, 100px" style="height: 100px" alt="Cannot load" fit="scale-down"></q-img>
            </div>
            <div class="col-xs-8 col-sm-8 col-md-6 offset-sm-1 offset-md-5">
              <q-input  clearable clear-icon="close" filled color="black" label="Search" v-model="searchTerm"
                        type="search" hint="AMP10.000_001, SPHERE-III.001_396, Aquatic, Homo sapiens"
                        style="max-width: 600px">
                <template v-slot:append>
                  <q-btn @click="textSearch()" label="Search" icon-right="search"></q-btn>
                </template>
              </q-input>
            </div>
          </div>
          <div class="row justify-center q-my-none q-pt-none" style="height: 50px">
            <div class="col-12">
              <q-tabs align="center" class="bg-white text-black" v-model="activeMenuItem" inline-label>
                <q-route-tab to="/home" label="Home" />
                <q-route-tab to="/browse_data" label="Browse" />
                <q-route-tab to="/api" label="API" />
                <q-route-tab to="/about" label="About" />
                <q-route-tab to="/downloads" label="Downloads" />
                <q-route-tab to="/contact" label="Contact" />
              </q-tabs>
            </div>
          </div>
        </div>
        <div class="col-xs-0 col-sm-1 col-md-2 bg-white"></div>
      </div>
    </q-header>

    <q-page-container>
      <!--     TODO  Define space on different screen size inside each view component.-->
      <!--     template-->
      <!--      <div class="row justify-center">-->
      <!--        <div class="col-xs-0 col-lg-2 bg-white"></div>-->
      <!--        <div class="col-12 col-lg-8 justify-center q-pr-md q-ma-auto">-->
      <!--          content...-->
      <!--        </div>-->
      <!--        <div class="col-xs-0 col-lg-2 bg-white"></div>-->
      <!--      </div>-->
      <router-view class="q-ma-auto q-pt-md" />
    </q-page-container>

    <q-footer reveal bordered class="bg-white text-white" >
      <div class="row text-center">
        <div class="col-xs-0 col-sm-1 col-md-2 bg-white"></div>
        <div class="col-xs-12 col-sm-10 col-md-8 justify-end text-black">
          <q-separator light />
          Powered by
          <el-link href="https://vuejs.org/index.html" type="success">Vue.js</el-link>
          <el-divider direction="vertical"></el-divider>
          <el-link href="https://element-plus.org/#/en-US" type="primary">Element</el-link>
          <el-divider direction="vertical"></el-divider>
          <el-link href="https://fastapi.tiangolo.com/" type="success">FastAPI</el-link>
        </div>
        <div class="col-xs-0 col-sm-1 col-md-2 bg-white"></div>
        <div class="col-xs-0 col-sm-1 col-md-2 bg-white"></div>
        <div class="col-xs-12 col-sm-10 col-md-8 justify-end text-black">
          &copy;2021-{{year}}
          <el-link href="https://www.fudan.edu.cn/" type="warning">Fudan University</el-link>
          All Rights Reserved.
        </div>
        <div class="col-xs-0 col-sm-1 col-md-2 bg-white"></div>
      </div>
    </q-footer>
  </q-layout>
  </div>
</template>

<style>
.header-wrapper {
  display: grid;
  grid-template-columns: repeat(24, 1fr);
  grid-template-rows: repeat(3, 1fr);
}
.logo{
  grid-column-start: 2;
  grid-column-end: 5;
  grid-row-start: 1;
  grid-row-end: 3;
}
.search-box{
  grid-column-start: 14;
  grid-column-end: 24;
  grid-row-start: 1;
  grid-row-end: 1;
}
.search-example{
  grid-column-start: 14;
  grid-column-end: 24;
  grid-row-start: 2;
  grid-row-end: 2;
  vertical-align: top;
  text-align: left;
  line-height: 10px;
}
.menu{
  grid-column-start: 7;
  grid-column-end: 20;
  grid-row-start: 2;
  grid-row-end: 3;
}
.el-footer{
  bottom: 0;
  width: 100%;
  height: 100px;
  background-color: #ffffff;
}
</style>

<script>
export default {
  name: 'AMPSphere',
  data() {
    return {
      home: 'home',
      activeMenuItem: '',
      searchTerm: '',
      loading: false,
      url: require('./assets/ampsphere_logo.svg'),
    };
  },
  created() {
    // let self = this
    // // https://stackoverflow.com/questions/50768678/axios-ajax-show-loading-when-making-ajax-request
    // this.axios.interceptors.request.use((config) => {
    //   self.loading = true
    //   // trigger 'loading=true' event here
    //   return config;
    // }, (error) => {
    //   self.loading = false
    //   // trigger 'loading=false' event here
    //   return Promise.reject(error);
    // });
    // this.axios.interceptors.response.use((response) => {
    //   self.loading = true
    //   // trigger 'loading=false' event here
    //   return response;
    // }, (error) => {
    //   self.loading = false
    //   // trigger 'loading=false' event here
    //   return Promise.reject(error);
    // });
  },
  mounted() {
    this.activeMenuItem=window.location.href.split('/')[3];
  },
  computed: {
    year: function () {
      return new Date().getFullYear();
    }
  },
  methods: {
    textSearch(){
      if (this.searchTerm.startsWith('AMP')) {
        window.open('/AMP?accession=' + this.searchTerm, '_blank')
      } else if (this.searchTerm.startsWith('SPHERE')) {
        window.open('/family?accession=' + this.searchTerm, '_blank')
      } else {
        window.open(encodeURI('/text_search?query=' + this.searchTerm), '_blank')}
      }
  }
}
</script>