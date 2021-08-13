<template>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <div id="AMPSphere">
    <el-container>
      <el-header height="200px">
        <div class="header-wrapper">
          <div class="logo">
            <el-image style="height: 200px; width: 200px" :src="url" lazy>
            </el-image>
          </div>
          <div class="search-box"><el-input placeholder="accession"
                                           v-model="text"
                                           maxlength="10"
                                           show-word-limit=true>
            <template v-slot:append>
              <el-button type="success"
                         icon="el-icon-search">
                Search
              </el-button>
            </template>
          </el-input>
            Examples:
            <el-link href="/AMP?ampId=AMP10.000_000" target="_blank" type="primary">AMP10.000_000</el-link>,
            <el-link href="/family?accession=SPHERE-III.001_396" target="_blank" type="primary">SPHERE-III.001_396</el-link>
          </div>
          <div class="menu">
            <el-menu mode="horizontal" :default-active="activeMenuItem" :router="true">
              <el-menu-item index="home">Home</el-menu-item>
              <el-menu-item index="browse_data">Browse data</el-menu-item>
              <el-menu-item index="tools">Tools</el-menu-item>
              <el-menu-item index="api">API</el-menu-item>
              <el-menu-item index="downloads">Downloads</el-menu-item>
<!--              <el-menu-item index="citation">Citation</el-menu-item>-->
              <el-menu-item index="help">Help</el-menu-item>
              <el-menu-item index="about">About</el-menu-item>
              <el-menu-item index="contact">Contact</el-menu-item>
            </el-menu>
          </div>
        </div>
      </el-header>

      <el-main>
        <el-row>
          <el-col><router-view/></el-col>
        </el-row>
      </el-main>

      <el-footer height="120px">
        <el-row type="flex" justify="center">
          <el-col :span="22" :offset="1" type="flex" justify="bottom">
            <el-divider></el-divider>
            Powered by
            <el-link href="https://vuejs.org/index.html" type="success">Vue.js</el-link>
            <el-divider direction="vertical"></el-divider>
            <el-link href="https://element.eleme.cn/#/en-US" type="primary">Element</el-link>
            <el-divider direction="vertical"></el-divider>
            <el-link href="https://fastapi.tiangolo.com/" type="success">FastAPI</el-link>
          </el-col>
        </el-row>
        <el-row type="flex" justify="center">
          <el-col :span="22" :offset="1" type="flex" justify="bottom">
            &copy;2021-{{year}}
            <el-link href="https://www.fudan.edu.cn/" type="warning">Fudan University</el-link>
            All Rights Reserved.
          </el-col>
        </el-row>

      </el-footer>
    </el-container>
  </div>
</template>

<style>
.header-wrapper {
  display: grid;
  grid-template-columns: repeat(24, 1fr);
  grid-template-rows: repeat(4, 1fr);
}
.logo{
  grid-column-start: 2;
  grid-column-end: 5;
  grid-row-start: 1;
  grid-row-end: 4;
}
.search-box{
  grid-column-start: 14;
  grid-column-end: 24;
  grid-row-start: 2;
  grid-row-end: 2;
}
.search-example{
  grid-column-start: 14;
  grid-column-end: 24;
  grid-row-start: 3;
  grid-row-end: 3;
  vertical-align: top;
  text-align: left;
  line-height: 10px;
}
.menu{
  grid-column-start: 6;
  grid-column-end: 20;
  grid-row-start: 3;
  grid-row-end: 4;
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
      activeMenuItem:'',
      url: require('./assets/ampsphere_logo.svg'),
    };
  },
  computed: {
    year: function () {
      return new Date().getFullYear();
    }
  },
  mounted() {
    this.activeMenuItem=window.location.href.split('/')[3];
  }
}
</script>