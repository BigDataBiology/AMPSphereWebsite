<template>
    <div class="Environment_Card">
        <el-row :gutter="12" type="flex" justify="end">
            <el-col :span="5" type="flex" justify="middle">
                <el-select v-model="environment"
                           placeholder="Select an environment"
                           :disabled="selectLoading"
                           clearable
                           filterable
                           @change="selectSearch">
                    <el-option
                            v-for="item in options"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-col>
        </el-row>

        <el-row type="flex" justify="left">
            <el-col :span="5" :offset="1" type="flex" justify="middle">
                <h2>Environment Card</h2>
            </el-col>
            <el-col :span="6" type="flex" justify="middle">
                <h3 v-if="!isNull">
                    <el-tag type="success" effect="dark">
                        {{Environment_AMP[0].Environment}}
                    </el-tag>
                </h3>
                <h3 v-else-if="tabLoading" effect="dark">
                    <el-tag type="danger">
                        Searching
                    </el-tag>
                </h3>
                <h3 v-else>
                    <el-tag type="warning" effect="dark">
                        No Data. Just select it:)
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
                                            :data="Environment_AMP"
                                            stripe
                                            border>
                                        <el-table-column
                                                prop="AMP_Count"
                                                label="Sequences"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <router-link
                                                        :to="{path:'/amp',query:{Environment:scope.row.Environment}}">
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
                                    </el-table>
                                </el-tab-pane>
                                <el-tab-pane label="Sequences" name="sequence">
                                    <el-pagination
                                            style="margin-bottom: 18px"
                                            background
                                            :page-size.sync="sPageSize"
                                            :total="sCount"
                                            :current-page.sync="sCurrentPage"
                                            layout="total, sizes, prev, next"
                                            :page-sizes="[10, 20, 30]"
                                            @size-change="sHandleSizeChange"
                                            @current-change="sHandleCurrentChange">
                                    </el-pagination>
                                    <el-table
                                            v-loading="tableLoading"
                                            element-loading-spinner="el-icon-loading"
                                            :data="Environment_Sequence"
                                            stripe
                                            border
                                            highlight-current-row>
                                        <el-table-column
                                                label="AMP ID"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <router-link :to="{path:'/amp_card',query:{AMP_ID:scope.row.AMP_ID}}">
                                                    <el-tag type="info">
                                                        <i class="el-icon-connection"></i>{{scope.row.AMP_ID}}
                                                    </el-tag>
                                                </router-link>
                                            </template>
                                        </el-table-column>
                                        <el-table-column
                                                prop="Sequence"
                                                label="Sequence"
                                                header-align="center">
                                        </el-table-column>
                                        <el-table-column
                                                label="Family ID"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <router-link
                                                        :to="{path:'/family',query:{Family_ID:scope.row.Family_ID}}">
                                                    <el-tag type="info">
                                                        <i class="el-icon-connection"></i>{{ scope.row.Family_ID }}
                                                    </el-tag>
                                                </router-link>
                                            </template>
                                        </el-table-column>
                                    </el-table>
                                </el-tab-pane>
                                <el-tab-pane label="Families" name="family">
                                    <el-pagination
                                            style="margin-bottom: 18px"
                                            background
                                            :page-size.sync="fPageSize"
                                            :total="fCount"
                                            :current-page.sync="fCurrentPage"
                                            layout="total, sizes, prev, next"
                                            :page-sizes="[10, 20, 30]"
                                            @size-change="fHandleSizeChange"
                                            @current-change="fHandleCurrentChange">
                                    </el-pagination>
                                    <el-table
                                            v-loading="tableLoading"
                                            element-loading-spinner="el-icon-loading"
                                            :data="Environment_Family"
                                            stripe
                                            border
                                            highlight-current-row>
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
                                        <el-table-column
                                                prop="AMP_Count"
                                                label="Sequences"
                                                header-align="center"
                                                align="center">
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
        name: 'Environment_Card',

        data() {
            return {
                environment: '',
                options: [{
                    value: 'Freshwater',
                    label: 'Freshwater'
                }, {
                    value: 'Gut',
                    label: 'Gut'
                }, {
                    value: 'Marine',
                    label: 'Marine'
                }, {
                    value: 'Milk',
                    label: 'Milk'
                }, {
                    value: 'Oral_Cavity',
                    label: 'Oral Cavity'
                }, {
                    value: 'Respiratory_Tract',
                    label: 'Respiratory Tract'
                }, {
                    value: 'Skin',
                    label: 'Skin'
                }, {
                    value: 'Soil',
                    label: 'Soil'
                }, {
                    value: 'Surface',
                    label: 'Surface'
                }, {
                    value: 'Vagina',
                    label: 'Vagina'
                }, {
                    value: 'Wastewater',
                    label: 'Wastewater'
                }],
                selectLoading: false,

                isNull: true,
                tabLoading: false,
                activeName: 'basic',
                Environment_AMP: [],

                sCount: 0,
                sPageSize: 10,
                sCurrentPage: 1,
                Environment_Sequence: [],
                fCount: 0,
                fPageSize: 10,
                fCurrentPage: 1,
                Environment_Family: [],
                tableLoading: false,
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
                if (this.$route.query.Environment) {
                    this.environment = this.$route.query.Environment;
                }
                this.isNull = true;
                this.tabLoading = true;
                this.search();
            }
        },

        methods: {
            sHandleSizeChange() {
                this.tableLoading = true;
                this.sequenceSearch();
            },

            sHandleCurrentChange() {
                this.tableLoading = true;
                this.sequenceSearch();
            },

            fHandleSizeChange() {
                this.tableLoading = true;
                this.familySearch();
            },

            fHandleCurrentChange() {
                this.tableLoading = true;
                this.familySearch();
            },

            selectSearch() {
                if (this.environment !== "") {
                    this.selectLoading = true;
                    this.isNull = true;
                    this.tabLoading = true;
                    this.search();
                } else {
                    this.Environment_AMP = [];
                    this.sCount = 0;
                    this.Environment_Sequence = [];
                    this.fCount = 0;
                    this.Environment_Family = [];
                    this.isNull = true;
                }
            },

            search() {
                let self = this;
                this.axios.get('/environment/index', {
                    params: {
                        environment: this.environment,
                        sPageSize: this.sPageSize,
                        sCurrentPage: this.sCurrentPage,
                        fPageSize: this.fPageSize,
                        fCurrentPage: this.fCurrentPage,
                    }
                }).then(function (response) {
                    if (response.status === 200) {
                        self.Environment_AMP = response.data['Environment_AMP'];
                        self.sCount = response.data['sCount'];
                        self.Environment_Sequence = response.data['Environment_Sequence'];
                        self.fCount = response.data['fCount'];
                        self.Environment_Family = response.data['Environment_Family'];
                        self.isNull = false;
                    } else if (response.status === 204) {
                        self.Environment_AMP = [];
                        self.sCount = 0;
                        self.Environment_Sequence = [];
                        self.fCount = 0;
                        self.Environment_Family = [];
                        self.isNull = true;
                    }
                    self.selectLoading = false;
                    self.tabLoading = false;
                    self.tableLoading = false;
                }).catch(function (error) {
                    console.log(error);
                });
            },

            sequenceSearch() {
                let self = this;
                this.axios.get('/environment/sequence', {
                    params: {
                        environment: this.environment,
                        sPageSize: this.sPageSize,
                        sCurrentPage: this.sCurrentPage,
                    }
                }).then(function (response) {
                    if (response.status === 200) {
                        self.sCount = response.data['sCount'];
                        self.Environment_Sequence = response.data['Environment_Sequence'];
                        self.isNull = false;
                    } else if (response.status === 204) {
                        self.sCount = 0;
                        self.Environment_Sequence = [];
                        self.isNull = true;
                    }
                    self.selectLoading = false;
                    self.tabLoading = false;
                    self.tableLoading = false;
                }).catch(function (error) {
                    console.log(error);
                });
            },

            familySearch() {
                let self = this;
                this.axios.get('/environment/family', {
                    params: {
                        environment: this.environment,
                        fPageSize: this.fPageSize,
                        fCurrentPage: this.fCurrentPage,
                    }
                }).then(function (response) {
                    if (response.status === 200) {
                        self.fCount = response.data['fCount'];
                        self.Environment_Family = response.data['Environment_Family'];
                        self.isNull = false;
                    } else if (response.status === 204) {
                        self.fCount = 0;
                        self.Environment_Family = [];
                        self.isNull = true;
                    }
                    self.selectLoading = false;
                    self.tabLoading = false;
                    self.tableLoading = false;
                }).catch(function (error) {
                    console.log(error);
                });
            },
        }
    }
</script>
