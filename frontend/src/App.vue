<template>
    <div id="app">
        <el-container>
            <el-header>
                <el-row type="flex" justify="center">
                    <el-col :span="22" type="flex" justify="middle">
                        <el-menu mode="horizontal" :default-active="activeIndex" :router="true">
                            <el-menu-item index="/">
                                <el-image style="height: 54px;width: 54px" :src="url" lazy></el-image>
                            </el-menu-item>
                            <el-menu-item index="/home">
                                Global AMP Survey database (GAS)
                            </el-menu-item>
                            <el-submenu index="browse">
                                <template slot="title">Browse</template>
                                <el-menu-item index="amp">AMPs</el-menu-item>
                                <el-menu-item index="amp_card">AMP Card</el-menu-item>
                                <el-menu-item index="family">Families</el-menu-item>
                                <el-menu-item index="environment">Environments</el-menu-item>
                            </el-submenu>
                            <el-submenu index="tools">
                                <template slot="title">Tools</template>
                                <el-menu-item index="blastp">Blastp</el-menu-item>
                                <el-menu-item index="hmm">HMM</el-menu-item>
                                <el-menu-item index="macrel">Macrel</el-menu-item>
                            </el-submenu>
                            <el-menu-item index="download">Downloads</el-menu-item>
                            <el-menu-item index="contact">Contact</el-menu-item>
                        </el-menu>
                    </el-col>
                </el-row>
            </el-header>

            <el-main>
                <el-row type="flex" justify="center">
                    <el-col :span="22" type="flex" justify="middle">
                        <router-view/>
                    </el-col>
                </el-row>
            </el-main>

            <el-footer height="120px">
                <el-row type="flex" justify="center">
                    <el-col :span="22" type="flex" justify="top">
                        <el-divider></el-divider>
                        Powered by
                        <el-link href="https://vuejs.org/index.html" type="success">Vue.js</el-link>
                        <el-divider direction="vertical"></el-divider>
                        <el-link href="https://element.eleme.cn/#/en-US" type="primary">Element</el-link>
                        <el-divider direction="vertical"></el-divider>
                        <el-link href="https://www.codeigniter.com/" type="danger">Codeigniter</el-link>
                        .
                    </el-col>
                </el-row>
                <el-row type="flex" justify="center">
                    <el-col :span="22" type="flex" justify="bottom">
                        &copy;2020-{{year}}
                        <el-link href="https://www.fudan.edu.cn/" type="warning">Fudan University</el-link>
                        All Rights Reserved.
                    </el-col>
                </el-row>
            </el-footer>
        </el-container>
    </div>
</template>

<style>
    .el-menu--horizontal > .el-menu-item.is-active {
        border-bottom: 2px solid #FFFFFF;
        color: #000;
    }

    .el-menu--horizontal > .el-submenu.is-active .el-submenu__title {
        border-bottom: 2px solid #FFFFFF;
        color: #000;
    }
</style>

<script>
    export default {
        name: 'app',

        data() {
            return {
                activeIndex: 'home',
                url: require('./assets/logo.png'),
            };
        },

        computed: {
            year: function () {
                return new Date().getFullYear();
            }
        }
    }
</script>
