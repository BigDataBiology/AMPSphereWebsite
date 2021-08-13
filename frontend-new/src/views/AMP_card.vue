<template>
    <div class="AMP_Card">
        <el-row :gutter="12" type="flex" justify="end">
            <el-col :span="8" type="flex" justify="middle">
                <el-input v-model="ampId" :maxlength="16" show-word-limit placeholder="Input an AMP ID like 'GAS000001'"
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
            <el-col :span="3" :offset="1" type="flex" justify="middle">
                <h2>AMP Card</h2>
            </el-col>
            <el-col :span="6" type="flex" justify="middle">
                <h3 v-if="!isNull">
                    <el-tag type="success" effect="dark">
                        {{AMP_Family[0].AMP_ID}}
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
                                            :data="AMP_Family"
                                            stripe>
                                        <el-table-column
                                                prop="Sequence"
                                                label="Sequence"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="Length"
                                                label="Length"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="Family_ID"
                                                label="Family ID"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <router-link
                                                        :to="{path:'/family',query:{Family_ID:scope.row.Family_ID}}">
                                                    <el-tag type="info">
                                                        <i class="el-icon-connection"></i>{{scope.row.Family_ID}}
                                                    </el-tag>
                                                </router-link>
                                            </template>
                                        </el-table-column>
                                    </el-table>
                                </el-tab-pane>
                                <el-tab-pane label="Features" name="feature">
                                    <el-table
                                            :data="AMP_Feature"
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
                                            :data="AMP_Feature"
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
                                            :data="AMP_Feature"
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
                                            :data="AMP_Feature"
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
                                        <el-table-column
                                                prop="Level_I"
                                                label="Level_I"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="Level_II"
                                                label="Level_II"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="Level_III"
                                                label="Level_III"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                    </el-table>
                                </el-tab-pane>
                                <el-tab-pane label="Prediction" name="prediction">
                                    <el-table
                                            :data="AMP_Prediction"
                                            stripe>
                                        <el-table-column
                                                prop="AMP_Class"
                                                label="AMP Class"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="AMP_Probability"
                                                label="AMP Probability"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="Hemolysis_Class"
                                                label="Hemolysis Class"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                        <el-table-column
                                                prop="Hemolysis_Probability"
                                                label="Hemolysis Probability"
                                                header-align="center"
                                                align="center">
                                        </el-table-column>
                                    </el-table>
                                </el-tab-pane>
                                <el-tab-pane label="Metagenomes" name="metagenome">
                                    <el-tag style="margin-right: 18px; margin-bottom: 18px"
                                            v-for="item in AMP_Metagenome" :key="item.id"
                                            type="info">
                                        <el-link icon="el-icon-link"
                                                 :href="'https://www.ncbi.nlm.nih.gov/sra/?term='+item.metagenomes"
                                                 type="info" target="_blank" :underline="false">
                                            {{item.metagenomes}}
                                        </el-link>
                                    </el-tag>
                                </el-tab-pane>
                                <el-tab-pane label="Countries" name="country">
                                    <el-table
                                            :data="AMP_Country"
                                            stripe>
                                        <el-table-column
                                                prop="Asia"
                                                label="Asia"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <el-tag v-if="scope.row.Asia>0" type="info" effect="dark">
                                                    {{scope.row.Asia}}
                                                </el-tag>
                                                <el-tag v-else type="info" effect="plain">
                                                    {{scope.row.Asia}}
                                                </el-tag>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="Europe"
                                                label="Europe"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <el-tag v-if="scope.row.Europe>0" type="info" effect="dark">
                                                    {{scope.row.Europe}}
                                                </el-tag>
                                                <el-tag v-else type="info" effect="plain">
                                                    {{scope.row.Europe}}
                                                </el-tag>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="Africa"
                                                label="Africa"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <el-tag v-if="scope.row.Africa>0" type="info" effect="dark">
                                                    {{scope.row.Africa}}
                                                </el-tag>
                                                <el-tag v-else type="info" effect="plain">
                                                    {{scope.row.Africa}}
                                                </el-tag>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="South_America"
                                                label="South America"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <el-tag v-if="scope.row.South_America>0" type="info" effect="dark">
                                                    {{scope.row.South_America}}
                                                </el-tag>
                                                <el-tag v-else type="info" effect="plain">
                                                    {{scope.row.South_America}}
                                                </el-tag>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="North_America"
                                                label="North America"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <el-tag v-if="scope.row.North_America>0" type="info" effect="dark">
                                                    {{scope.row.North_America}}
                                                </el-tag>
                                                <el-tag v-else type="info" effect="plain">
                                                    {{scope.row.North_America}}
                                                </el-tag>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="Oceania"
                                                label="Oceania"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <el-tag v-if="scope.row.Oceania>0" type="info" effect="dark">
                                                    {{scope.row.Oceania}}
                                                </el-tag>
                                                <el-tag v-else type="info" effect="plain">
                                                    {{scope.row.Oceania}}
                                                </el-tag>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="Pacific_Ocean"
                                                label="Pacific Ocean"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <el-tag v-if="scope.row.Pacific_Ocean>0" type="info" effect="dark">
                                                    {{scope.row.Pacific_Ocean}}
                                                </el-tag>
                                                <el-tag v-else type="info" effect="plain">
                                                    {{scope.row.Pacific_Ocean}}
                                                </el-tag>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="New_Zaeland"
                                                label="New Zaeland"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <el-tag v-if="scope.row.New_Zaeland>0" type="info" effect="dark">
                                                    {{scope.row.New_Zaeland}}
                                                </el-tag>
                                                <el-tag v-else type="info" effect="plain">
                                                    {{scope.row.New_Zaeland}}
                                                </el-tag>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="na"
                                                label="na"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <el-tag v-if="scope.row.na>0" type="info" effect="dark">
                                                    {{scope.row.na}}
                                                </el-tag>
                                                <el-tag v-else type="info" effect="plain">
                                                    {{scope.row.na}}
                                                </el-tag>
                                            </template>
                                        </el-table-column>
                                    </el-table>
                                    <el-row type="flex" justify="center">
                                        <div id="country" style="width: 400px;height:300px;"></div>
                                    </el-row>
                                </el-tab-pane>
                                <el-tab-pane label="Environments" name="environment">
                                    <el-table
                                            :data="AMP_Environment"
                                            stripe>
                                        <el-table-column
                                                prop="Freshwater"
                                                label="Freshwater"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <router-link
                                                        :to="{path:'/environment',query:{Environment:'Freshwater'}}">
                                                    <el-tag v-if="scope.row.Freshwater>0" type="info" effect="dark">
                                                        <i class="el-icon-connection"></i> {{scope.row.Freshwater}}
                                                    </el-tag>
                                                    <el-tag v-else type="info" effect="plain">
                                                        {{scope.row.Freshwater}}
                                                    </el-tag>
                                                </router-link>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="Gut"
                                                label="Gut"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <router-link :to="{path:'/environment',query:{Environment:'Gut'}}">
                                                    <el-tag v-if="scope.row.Gut>0" type="info" effect="dark">
                                                        <i class="el-icon-connection"></i> {{scope.row.Gut}}
                                                    </el-tag>
                                                    <el-tag v-else type="info" effect="plain">
                                                        {{scope.row.Gut}}
                                                    </el-tag>
                                                </router-link>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="Marine"
                                                label="Marine"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <router-link :to="{path:'/environment',query:{Environment:'Marine'}}">
                                                    <el-tag v-if="scope.row.Marine>0" type="info" effect="dark">
                                                        <i class="el-icon-connection"></i> {{scope.row.Marine}}
                                                    </el-tag>
                                                    <el-tag v-else type="info" effect="plain">
                                                        {{scope.row.Marine}}
                                                    </el-tag>
                                                </router-link>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="Milk"
                                                label="Milk"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <router-link :to="{path:'/environment',query:{Environment:'Milk'}}">
                                                    <el-tag v-if="scope.row.Milk>0" type="info" effect="dark">
                                                        <i class="el-icon-connection"></i> {{scope.row.Milk}}
                                                    </el-tag>
                                                    <el-tag v-else type="info" effect="plain">
                                                        {{scope.row.Milk}}
                                                    </el-tag>
                                                </router-link>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="Oral_Cavity"
                                                label="Oral Cavity"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <router-link
                                                        :to="{path:'/environment',query:{Environment:'Oral_Cavity'}}">
                                                    <el-tag v-if="scope.row.Oral_Cavity>0" type="info" effect="dark">
                                                        <i class="el-icon-connection"></i> {{scope.row.Oral_Cavity}}
                                                    </el-tag>
                                                    <el-tag v-else type="info" effect="plain">
                                                        {{scope.row.Oral_Cavity}}
                                                    </el-tag>
                                                </router-link>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="Respiratory_Tract"
                                                label="Respiratory Tract"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <router-link
                                                        :to="{path:'/environment',query:{Environment:'Respiratory_Tract'}}">
                                                    <el-tag v-if="scope.row.Respiratory_Tract>0" type="info"
                                                            effect="dark">
                                                        <i class="el-icon-connection"></i>
                                                        {{scope.row.Respiratory_Tract}}
                                                    </el-tag>
                                                    <el-tag v-else type="info" effect="plain">
                                                        {{scope.row.Respiratory_Tract}}
                                                    </el-tag>
                                                </router-link>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="Skin"
                                                label="Skin"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <router-link :to="{path:'/environment',query:{Environment:'Skin'}}">
                                                    <el-tag v-if="scope.row.Skin>0" type="info" effect="dark">
                                                        <i class="el-icon-connection"></i> {{scope.row.Skin}}
                                                    </el-tag>
                                                    <el-tag v-else type="info" effect="plain">
                                                        {{scope.row.Skin}}
                                                    </el-tag>
                                                </router-link>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="Soil"
                                                label="Soil"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <router-link :to="{path:'/environment',query:{Environment:'Soil'}}">
                                                    <el-tag v-if="scope.row.Soil>0" type="info" effect="dark">
                                                        <i class="el-icon-connection"></i> {{scope.row.Soil}}
                                                    </el-tag>
                                                    <el-tag v-else type="info" effect="plain">
                                                        {{scope.row.Soil}}
                                                    </el-tag>
                                                </router-link>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="Surface"
                                                label="Surface"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <router-link :to="{path:'/environment',query:{Environment:'Surface'}}">
                                                    <el-tag v-if="scope.row.Surface>0" type="info" effect="dark">
                                                        <i class="el-icon-connection"></i> {{scope.row.Surface}}
                                                    </el-tag>
                                                    <el-tag v-else type="info" effect="plain">
                                                        {{scope.row.Surface}}
                                                    </el-tag>
                                                </router-link>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="Vagina"
                                                label="Vagina"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <router-link :to="{path:'/environment',query:{Environment:'Vagina'}}">
                                                    <el-tag v-if="scope.row.Vagina>0" type="info" effect="dark">
                                                        <i class="el-icon-connection"></i> {{scope.row.Vagina}}
                                                    </el-tag>
                                                    <el-tag v-else type="info" effect="plain">
                                                        {{scope.row.Vagina}}
                                                    </el-tag>
                                                </router-link>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="Wastewater"
                                                label="Wastewater"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <router-link
                                                        :to="{path:'/environment',query:{Environment:'Wastewater'}}">
                                                    <el-tag v-if="scope.row.Wastewater>0" type="info" effect="dark">
                                                        <i class="el-icon-connection"></i> {{scope.row.Wastewater}}
                                                    </el-tag>
                                                    <el-tag v-else type="info" effect="plain">
                                                        {{scope.row.Wastewater}}
                                                    </el-tag>
                                                </router-link>
                                            </template>
                                        </el-table-column>
                                    </el-table>
                                    <el-row type="flex" justify="center">
                                        <div id="environment" style="width: 400px;height:300px;"></div>
                                    </el-row>
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
        name: 'AMP_Card',

        data() {
            return {
                ampId: '',
                type: 'primary',
                searchLoading: false,

                isNull: true,
                tabLoading: false,
                activeName: 'basic',
                AMP_Family: [],
                AMP_Feature: [],
                AMP_Country: [],
                AMP_Environment: [],
                AMP_Metagenome: {},
                AMP_Prediction: []
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
                if (this.$route.query.AMP_ID) {
                    this.ampId = this.$route.query.AMP_ID;
                }
                this.isNull = true;
                this.tabLoading = true;
                this.search();
            }
        },

        methods: {
            clickSearch() {
                if (this.ampId !== "") {
                    this.type = "danger";
                    this.searchLoading = true;
                    this.isNull = true;
                    this.tabLoading = true;
                    this.search();
                } else {
                    this.AMP_Family = [];
                    this.AMP_Feature = [];
                    this.AMP_Metagenome = {};
                    this.AMP_Prediction = [];
                    this.AMP_Country = [];
                    this.AMP_Environment = [];
                    this.isNull = true;
                    //this.drawCountryChart();
                    //this.drawEnvironmentChart();
                }
            },

            search() {
                let self = this;
                this.axios.get('/amp/', {
                    params: {
                        ampId: this.ampId,
                    }
                }).then(function (response) {
                    if (response.status === 200) {
                        self.AMP_Family = response.data['AMP_Family'];
                        self.AMP_Feature = response.data['AMP_Feature'];
                        self.AMP_Metagenome = response.data['AMP_Metagenome'];
                        self.AMP_Prediction = response.data['AMP_Prediction'];
                        self.AMP_Country = response.data['AMP_Country'];
                        self.AMP_Environment = response.data['AMP_Environment'];
                        self.AMP_Graphs = response.data['AMP_Graphs'];
                        self.isNull = false;
                        //self.drawCountryChart();
                        //self.drawEnvironmentChart();

                    } else if (response.status === 204) {
                        self.AMP_Family = [];
                        self.AMP_Feature = [];
                        self.AMP_Metagenome = {};
                        self.AMP_Prediction = [];
                        self.AMP_Country = [];
                        self.AMP_Environment = [];
                        self.isNull = true;
                        //self.drawCountryChart();
                        //self.drawEnvironmentChart();
                    }
                    self.type = 'primary';
                    self.searchLoading = false;
                    self.tabLoading = false;
                }).catch(function (error) {
                    console.log(error);
                });
            },

            drawCountryChart() {
                let self = this;
                // 基于准备好的dom，初始化echarts实例
                var myChart = this.$echarts.init(document.getElementById('country'));

                if (self.AMP_Country.length > 0) {
                    delete self.AMP_Country[0]['id'];
                    delete self.AMP_Country[0]['AMP_ID'];

                    // 指定图表的配置项和数据
                    var option = {
                        toolbox: {
                            feature: {
                                magicType: {
                                    type: ['line', 'bar'],
                                    title: {
                                        line: 'for line charts',
                                        bar: 'for line charts',
                                    }
                                },
                                saveAsImage: {
                                    title: 'save as image',
                                    pixelRatio: 2
                                }
                            }
                        },
                        xAxis: {
                            type: 'value',
                            axisLabel: {
                                fontSize: 14
                            },
                            splitLine: {
                                show: false
                            }
                        },
                        grid: [{
                            top: '10%',
                            bottom: '5%',
                            left: '5%',
                            right: '10%',
                            containLabel: true
                        }],
                        yAxis: {
                            type: 'category',
                            data: Object.keys(self.AMP_Country[0]),
                            axisLabel: {
                                rotate: 30,
                                fontSize: 14
                            },
                            splitLine: {
                                show: false
                            }
                        },
                        series: [{
                            type: 'bar',
                            data: Object.keys(self.AMP_Country[0]).map(function (key) {
                                return self.AMP_Country[0][key];
                            }),
                            color: '#000000',
                            label: {
                                show: true,
                                position: 'right',
                                fontSize: 14
                            },
                        }],
                    };

                    // 使用刚指定的配置项和数据显示图表。
                    myChart.setOption(option);
                } else {
                    myChart.clear();
                }
            },

            drawEnvironmentChart() {
                let self = this;
                // 基于准备好的dom，初始化echarts实例
                var myChart = this.$echarts.init(document.getElementById('environment'));

                if (self.AMP_Environment.length > 0) {
                    delete self.AMP_Environment[0]['id'];
                    delete self.AMP_Environment[0]['AMP_ID'];

                    // 指定图表的配置项和数据
                    var option = {
                        toolbox: {
                            feature: {
                                magicType: {
                                    type: ['line', 'bar'],
                                    title: {
                                        line: 'for line charts',
                                        bar: 'for line charts',
                                    }
                                },
                                saveAsImage: {
                                    title: 'save as image',
                                    pixelRatio: 2
                                }
                            }
                        },
                        xAxis: {
                            type: 'value',
                            axisLabel: {
                                fontSize: 14
                            },
                            splitLine: {
                                show: false
                            }
                        },
                        grid: [{
                            top: '10%',
                            bottom: '5%',
                            left: '5%',
                            right: '10%',
                            containLabel: true
                        }],
                        yAxis: {
                            type: 'category',
                            data: Object.keys(self.AMP_Environment[0]),
                            axisLabel: {
                                rotate: 30,
                                fontSize: 14
                            },
                            splitLine: {
                                show: false
                            }
                        },
                        series: [{
                            type: 'bar',
                            data: Object.keys(self.AMP_Environment[0]).map(function (key) {
                                return self.AMP_Environment[0][key];
                            }),
                            color: '#000000',
                            label: {
                                show: true,
                                position: 'right',
                                fontSize: 14
                            },
                        }],
                    };

                    // 使用刚指定的配置项和数据显示图表。
                    myChart.setOption(option);
                } else {
                    myChart.clear();
                }
            }
        }
    }
</script>
