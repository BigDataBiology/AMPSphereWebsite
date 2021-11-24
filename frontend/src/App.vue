<template>
  <div id="AMPSphere" class="q-pa-md">
  <q-layout view="hHh lpR fFf" class="shadow-2 rounded-borders">
    <q-header reveal bordered class="bg-white text-black" reveal-offset="100px" height-hint="160" style="height: 160px">
      <div class="row q-pl-auto q-pr-auto" style="height: 150px">
        <div class="col-0 col-xl-2 bg-white"></div>
        <div class="col-12 col-xl-8">
          <div class="row justify-center q-my-none q-pb-none q-px-md" style="height: 100px">
            <div class="col-xs-4 col-sm-2 col-md-1">
              <a href="/home">
              <q-img :src="require('./assets/logo.png')" sizes="(max-width: 100px) 100px, 100px" style="height: 100px" alt="Cannot load" fit="scale-down"></q-img>
              </a>
            </div>
            <div class="col-xs-8 col-sm-8 col-md-6 offset-sm-1 offset-md-5">
              <q-input  clearable clear-icon="close" filled color="primary" label="Search" v-model="searchTerm"
                        type="search" hint="Entity accession, Habitat (Aquatic) or Host (Homo sapiens)"
                        style="max-width: 600px" @keydown.enter.prevent="textSearch()">
                <template v-slot:append>
                  <q-btn @click="textSearch()" label="Search" icon-right="search"></q-btn>
                </template>
              </q-input>
            </div>
          </div>
          <div class="row justify-center q-my-none q-pt-none q-px-md" style="height: 50px">
            <div class="col-12">
              <q-tabs align="center" class="bg-primary text-white" v-model="activeMenuItem" inline-label>
                <q-route-tab to="/home" label="Home" />
                <q-route-tab to="/browse_data" label="Browse" />
                <q-route-tab to="/about" label="About" />
                <q-route-tab to="/downloads" label="Downloads" />
                <q-route-tab to="/contact" label="Contact" />
              </q-tabs>
            </div>
          </div>
        </div>
        <div class="col-0 col-xl-2 bg-white"></div>
      </div>
    </q-header>

    <q-page-container>
      <!--     TODO  Define space on different screen size inside each view component.-->
      <!--     template-->
      <!--      <div class="row justify-center">-->
      <!--        <div class="col-xs-0 col-xl-2 bg-white"></div>-->
      <!--        <div class="col-12 col-xl-8 justify-center q-pr-md q-ma-auto">-->
      <!--          content...-->
      <!--        </div>-->
      <!--        <div class="col-xs-0 col-xl-2 bg-white"></div>-->
      <!--      </div>-->
      <router-view class="q-px-md q-pt-md" />
    </q-page-container>

    <q-footer reveal bordered class="bg-white text-white" >
      <div class="row text-center q-pa-xs">
<!--        <div class="col-0 col-sm-1 col-md-2 bg-white"></div>-->
        <div class="col-12 text-black">
        </div>
<!--        <div class="col-0 col-sm-1 col-md-2 bg-white"></div>-->
<!--        <div class="col-0 col-sm-1 col-md-2 bg-white"></div>-->
        <div class="col-12 text-black">
          &copy;2021-{{year}}
          <cite>AMPSphere authors</cite>.
        </div>
<!--        <div class="col-0 col-sm-1 col-md-2 bg-white"></div>-->
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
        window.open('/AMP?accession=' + this.searchTerm, '_self')
      } else if (this.searchTerm.startsWith('SPHERE')) {
        window.open('/family?accession=' + this.searchTerm, '_self')
      } else {
        window.open(encodeURI('/text_search?query=' + this.searchTerm), '_self')}
      }
  }
}
</script>
