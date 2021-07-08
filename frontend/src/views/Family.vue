<template>
    <div class="Family_Card">
        <el-row :gutter="12" type="flex" justify="end">
            <el-col :span="8" type="flex" justify="middle">
                <el-input v-model="familyId" :maxlength="16" show-word-limit
                          placeholder="Input a Family ID like 'GAF531'"
                          clearable></el-input>
            </el-col>
            <el-col :span="3" type="flex" justify="middle">
                <el-button size="medium" :type="type" :loading="searchLoading" icon="el-icon-search"
                           @click="clickSearch">
                    Search
                </el-button>
            </el-col>
        </el-row>

        <el-row type="flex" justify="left">
            <el-col :span="4" :offset="1" type="flex" justify="middle">
                <h2>Family Card</h2>
            </el-col>
            <el-col :span="6" type="flex" justify="middle">
                <h3 v-if="!isNull">
                    <el-tag type="success" effect="dark">
                        {{Family_AMP[0].Family_ID}}
                    </el-tag>
                </h3>
                <h3 v-else-if="tabLoading" effect="dark">
                    <el-tag type="danger">
                        Searching
                    </el-tag>
                </h3>
                <h3 v-else>
                    <el-tag type="warning" effect="dark">
                        No Data. Just search it:)
                    </el-tag>
                </h3>
            </el-col>
        </el-row>

        <el-row type="flex" justify="center">
            <el-col type="flex" justify="middle">
                <el-card :shadow="shadow">
                    <el-row type="flex" justify="center">
                        <el-col type="flex" justify="middle">
                            <el-tabs v-loading="tabLoading" element-loading-spinner="el-icon-loading"
                                     v-model="activeName" tab-position="left">
                                <el-tab-pane label="Basic" name="basic">
                                    <el-table
                                            :data="Family_AMP"
                                            stripe
                                            border>
                                        <el-table-column
                                                prop="AMP_Count"
                                                label="Sequences"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <router-link
                                                        :to="{path:'/amp',query:{Family_ID:scope.row.Family_ID}}">
                                                    <el-tag type="info">
                                                        <i class="el-icon-connection"></i>{{scope.row.AMP_Count}}
                                                    </el-tag>
                                                </router-link>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="Length_Avg"
                                                label="Avg Length"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                label="Clustering level"
                                                header-align="center"
                                                align="center">
                                            3
                                        </el-table-column>
                                    </el-table>
                                    <el-row type="flex" justify="center">
                                        <h4>Environments</h4>
                                    </el-row>
                                    <router-link v-if="Family_Environment.Freshwater!='0'" :to="{path:'/environment',query:{Environment:'Freshwater'}}">
                                        <el-tag style="margin-right: 18px; margin-bottom: 18px" type="info">
                                            <i class="el-icon-connection"></i>Freshwater
                                        </el-tag>
                                    </router-link>
                                    <router-link v-if="Family_Environment.Gut!='0'" :to="{path:'/environment',query:{Environment:'Gut'}}">
                                        <el-tag style="margin-right: 18px; margin-bottom: 18px" type="info">
                                            <i class="el-icon-connection"></i>Gut
                                        </el-tag>
                                    </router-link>
                                    <router-link v-if="Family_Environment.Marine!='0'" :to="{path:'/environment',query:{Environment:'Marine'}}">
                                        <el-tag style="margin-right: 18px; margin-bottom: 18px" type="info">
                                            <i class="el-icon-connection"></i>Marine
                                        </el-tag>
                                    </router-link>
                                    <router-link v-if="Family_Environment.Milk!='0'" :to="{path:'/environment',query:{Environment:'Milk'}}">
                                        <el-tag style="margin-right: 18px; margin-bottom: 18px" type="info">
                                            <i class="el-icon-connection"></i>Milk
                                        </el-tag>
                                    </router-link>
                                    <router-link v-if="Family_Environment.Oral_Cavity!='0'" :to="{path:'/environment',query:{Environment:'Oral_Cavity'}}">
                                        <el-tag style="margin-right: 18px; margin-bottom: 18px" type="info">
                                            <i class="el-icon-connection"></i>Oral_Cavity
                                        </el-tag>
                                    </router-link>
                                    <router-link v-if="Family_Environment.Respiratory_Tract!='0'" :to="{path:'/environment',query:{Environment:'Respiratory_Tract'}}">
                                        <el-tag style="margin-right: 18px; margin-bottom: 18px" type="info">
                                            <i class="el-icon-connection"></i>Respiratory_Tract
                                        </el-tag>
                                    </router-link>
                                    <router-link v-if="Family_Environment.Skin!='0'" :to="{path:'/environment',query:{Environment:'Skin'}}">
                                        <el-tag style="margin-right: 18px; margin-bottom: 18px" type="info">
                                            <i class="el-icon-connection"></i>Skin
                                        </el-tag>
                                    </router-link>
                                    <router-link v-if="Family_Environment.Soil!='0'" :to="{path:'/environment',query:{Environment:'Soil'}}">
                                        <el-tag style="margin-right: 18px; margin-bottom: 18px" type="info">
                                            <i class="el-icon-connection"></i>Soil
                                        </el-tag>
                                    </router-link>
                                    <router-link v-if="Family_Environment.Surface!='0'" :to="{path:'/environment',query:{Environment:'Surface'}}">
                                        <el-tag style="margin-right: 18px; margin-bottom: 18px" type="info">
                                            <i class="el-icon-connection"></i>Surface
                                        </el-tag>
                                    </router-link>
                                    <router-link v-if="Family_Environment.Vagina!='0'" :to="{path:'/environment',query:{Environment:'Vagina'}}">
                                        <el-tag style="margin-right: 18px; margin-bottom: 18px" type="info">
                                            <i class="el-icon-connection"></i>Vagina
                                        </el-tag>
                                    </router-link>
                                    <router-link v-if="Family_Environment.Wastewater!='0'" :to="{path:'/environment',query:{Environment:'Wastewater'}}">
                                        <el-tag style="margin-right: 18px; margin-bottom: 18px" type="info">
                                            <i class="el-icon-connection"></i>Wastewater
                                        </el-tag>
                                    </router-link>
                                    <el-divider></el-divider>
                                    <el-row type="flex" justify="center">
                                        <h4>Downloads</h4>
                                    </el-row>
                                    <el-table
                                            :data="Family_Avg_Feature"
                                            stripe
                                            border>
                                        <el-table-column
                                                label="HMM Logo"
                                                header-align="center"
                                                align="center">
                                            <el-button icon="el-icon-picture" circle
                                                       @click=logoDownload(familyId)>
                                            </el-button>
                                        </el-table-column>
                                        <el-table-column
                                                label="Tree Figure"
                                                header-align="center"
                                                align="center">
                                            <el-button icon="el-icon-s-fold" circle
                                                       @click=treesFiguresDownload(familyId)>
                                            </el-button>
                                        </el-table-column>
                                        <el-table-column
                                                label="Alignment"
                                                header-align="center"
                                                align="center">
                                            <el-button icon="el-icon-files" circle
                                                       @click=alnDownload(familyId)>
                                            </el-button>
                                        </el-table-column>
                                        <el-table-column
                                                label="Tree"
                                                header-align="center"
                                                align="center">
                                            <el-button icon="el-icon-notebook-2" circle
                                                       @click=treesDownload(familyId)>
                                            </el-button>
                                        </el-table-column>
                                        <el-table-column
                                                label="HMM"
                                                header-align="center"
                                                align="center">
                                            <el-button icon="el-icon-document" circle
                                                       @click=hmmDownload(familyId)>
                                            </el-button>
                                        </el-table-column>
                                        <el-table-column
                                                label="Features"
                                                header-align="center"
                                                align="center">
                                            <el-button icon="el-icon-data-analysis" circle
                                                       @click=familyFeatureDownload(familyId)>
                                            </el-button>
                                        </el-table-column>
                                    </el-table>
                                </el-tab-pane>
                                <el-tab-pane label="Avg Features" name="avg_feature">
                                    <el-table
                                            :data="Family_Avg_Feature"
                                            stripe
                                            border>
                                        <el-table-column
                                                prop="tinyAA"
                                                label="tinyAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="smallAA"
                                                label="smallAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="aliphaticAA"
                                                label="aliphaticAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="aromaticAA"
                                                label="aromaticAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="nonpolarAA"
                                                label="nonpolarAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="polarAA"
                                                label="polarAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="chargedAA"
                                                label="chargedAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="basicAA"
                                                label="basicAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                    </el-table>
                                    <el-table
                                            :data="Family_Avg_Feature"
                                            stripe
                                            border>
                                        <el-table-column
                                                prop="acidicAA"
                                                label="acidicAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="charge"
                                                label="charge"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="pI"
                                                label="pI"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="aindex"
                                                label="aindex"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="instaindex"
                                                label="instaindex"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="boman"
                                                label="boman"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="hydrophobicity"
                                                label="hydrophobicity"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="hmoment"
                                                label="hmoment"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                    </el-table>
                                    <el-table
                                            :data="Family_Avg_Feature"
                                            stripe
                                            border>
                                        <el-table-column
                                                prop="SA_Group1_residue0"
                                                label="SA.Group1.residue0"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="SA_Group2_residue0"
                                                label="SA.Group2.residue0"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="SA_Group3_residue0"
                                                label="SA.Group3.residue0"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="HB_Group1_residue0"
                                                label="HB.Group1.residue0"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="HB_Group2_residue0"
                                                label="HB.Group2.residue0"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="HB_Group3_residue0"
                                                label="HB.Group3.residue0"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                    </el-table>
                                    <el-table
                                            :data="Family_Avg_Feature"
                                            stripe
                                            border>
                                        <el-table-column
                                                prop="AGG"
                                                label="AGG"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="AMYLO"
                                                label="AMYLO"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="TURN"
                                                label="TURN"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="HELIX"
                                                label="HELIX"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="HELAGG"
                                                label="HELAGG"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="BETA"
                                                label="BETA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                    </el-table>
                                </el-tab-pane>
                                <el-tab-pane label="Std Features" name="std_feature">
                                    <el-table
                                            :data="Family_Std_Feature"
                                            stripe
                                            border>
                                        <el-table-column
                                                prop="tinyAA"
                                                label="tinyAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="smallAA"
                                                label="smallAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="aliphaticAA"
                                                label="aliphaticAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="aromaticAA"
                                                label="aromaticAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="nonpolarAA"
                                                label="nonpolarAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="polarAA"
                                                label="polarAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="chargedAA"
                                                label="chargedAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="basicAA"
                                                label="basicAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                    </el-table>
                                    <el-table
                                            :data="Family_Std_Feature"
                                            stripe
                                            border>
                                        <el-table-column
                                                prop="acidicAA"
                                                label="acidicAA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="charge"
                                                label="charge"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="pI"
                                                label="pI"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="aindex"
                                                label="aindex"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="instaindex"
                                                label="instaindex"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="boman"
                                                label="boman"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="hydrophobicity"
                                                label="hydrophobicity"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="hmoment"
                                                label="hmoment"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                    </el-table>
                                    <el-table
                                            :data="Family_Std_Feature"
                                            stripe
                                            border>
                                        <el-table-column
                                                prop="SA_Group1_residue0"
                                                label="SA.Group1.residue0"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="SA_Group2_residue0"
                                                label="SA.Group2.residue0"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="SA_Group3_residue0"
                                                label="SA.Group3.residue0"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="HB_Group1_residue0"
                                                label="HB.Group1.residue0"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="HB_Group2_residue0"
                                                label="HB.Group2.residue0"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="HB_Group3_residue0"
                                                label="HB.Group3.residue0"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                    </el-table>
                                    <el-table
                                            :data="Family_Std_Feature"
                                            stripe
                                            border>
                                        <el-table-column
                                                prop="AGG"
                                                label="AGG"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="AMYLO"
                                                label="AMYLO"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="TURN"
                                                label="TURN"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="HELIX"
                                                label="HELIX"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="HELAGG"
                                                label="HELAGG"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="BETA"
                                                label="BETA"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                    </el-table>
                                </el-tab-pane>
                            </el-tabs>
                        </el-col>
                    </el-row>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<style>
    .el-tabs__item {
        font-size: 17px;
    }
</style>

<script>
    export default {
        name: 'Family_Card',

        data() {
            return {
                familyId: '',
                type: 'primary',
                searchLoading: false,

                isNull: true,
                tabLoading: false,
                activeName: 'basic',
                Family_AMP: [],
                Family_Environment: [],
                Family_Avg_Feature: [],
                Family_Std_Feature: [],
            }
        },

        computed: {
            shadow: function () {
                if (this.isNull) {
                    return 'never';
                } else {
                    return 'always';
                }
            }
        },

        mounted() {
            if (Object.keys(this.$route.query).length !== 0) {
                if (this.$route.query.Family_ID) {
                    this.familyId = this.$route.query.Family_ID;
                }
                this.isNull = true;
                this.tabLoading = true;
                this.search();
            }
        },

        methods: {
            clickSearch() {
                if (this.familyId !== "") {
                    this.type = "danger";
                    this.searchLoading = true;
                    this.isNull = true;
                    this.tabLoading = true;
                    this.search();
                } else {
                    this.Family_AMP = [];
                    this.Family_Environment = [];
                    this.Family_Avg_Feature = [];
                    this.Family_Std_Feature = [];
                    this.isNull = true;
                }
            },

            search() {
                let self = this;
                this.axios.get('/family/index', {
                    params: {
                        familyId: this.familyId,
                    }
                }).then(function (response) {
                    if (response.status === 200) {
                        self.Family_AMP = response.data['Family_AMP'];
                        self.Family_Environment = response.data['Family_Environment'][0];
                        self.Family_Avg_Feature = response.data['Family_Avg_Feature'];
                        self.Family_Std_Feature = response.data['Family_Std_Feature'];
                        self.isNull = false;
                    } else if (response.status === 204) {
                        self.Family_AMP = [];
                        self.Family_Environment = response.data['Family_Environment'][0];
                        self.Family_Avg_Feature = [];
                        self.Family_Std_Feature = [];
                        self.isNull = true;
                    }
                    self.type = 'primary';
                    self.searchLoading = false;
                    self.tabLoading = false;
                }).catch(function (error) {
                    console.log(error);
                });
            },

            logoDownload(file) {
                this.download("logo/", file + ".pdf");
            },

            treesFiguresDownload(file) {
                this.download("trees_figures/", file + ".ascII.txt");
            },

            alnDownload(file) {
                this.download("aln/", file + ".aln");
            },

            treesDownload(file) {
                this.download("trees/", file + ".nwk");
            },

            hmmDownload(file) {
                this.download("hmm/", file + ".hmm");
            },

            familyFeatureDownload(file) {
                this.download("family_feature/", file + ".feat");
            },

            download(path, file) {
                let self = this;
                this.tabLoading = true;
                this.axios.get('/family/download', {
                    params: {
                        url: path + file
                    },
                    responseType: "blob"
                }).then(function (response) {
                    if (response.status === 200) {
                        var url = window.URL.createObjectURL(response.data);
                        var a = document.createElement("a");
                        document.body.appendChild(a);
                        a.href = url;
                        a.download = file;
                        a.click();
                    }
                    self.tabLoading = false;
                }).catch(function (error) {
                    console.log(error);
                });
            }
        }
    }
</script>
