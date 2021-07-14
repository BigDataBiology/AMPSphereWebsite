<template>
    <div class="AMP">
        <el-card shadow="always">
            <el-row :gutter="20" type="flex" justify="center">
                <el-col :span="5" type="flex" justify="middle">
                    <h4>Search Filter</h4>
                    <el-button size="medium" :type="type" :loading="searchLoading" icon="el-icon-search"
                               @click="filter">Search
                    </el-button>
                    <el-button size="medium" circle :loading="searchLoading" icon="el-icon-refresh" @click="reset">
                    </el-button>
                    <el-divider></el-divider>
                    <h4>AMP ID (Keyword)</h4>
                    <el-input v-model="ampId" :maxlength="16" show-word-limit clearable></el-input>
                    <p>example: GAS000001</p>
                    <h4>Family ID (Keyword)</h4>
                    <el-input v-model="familyId" :maxlength="16" show-word-limit clearable></el-input>
                    <p>example: GAF531</p>
                    <h4>Environment (Keyword)</h4>
                    <el-select v-model="environment"
                               clearable
                               multiple
                               filterable>
                        <el-option
                                v-for="item in options"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                        </el-option>
                    </el-select>
                    <el-divider></el-divider>
                    <h4>Sequence (Fuzzy)</h4>
                    <el-input type="textarea" v-model="sequence" :maxlength="100" show-word-limit :rows="3"
                              resize="none" clearable></el-input>
                    <p>example: AATPVALRWLLA</p>
                    <el-divider></el-divider>
                    <h4>Sequence Length</h4>
                    {{length[0]}}-{{length[1]}}
                    <el-slider
                            v-model="length"
                            :min="10"
                            :max="100"
                            :step="1"
                            range>
                    </el-slider>
                    <h4>pI Range</h4>
                    {{pI[0]}}-{{pI[1]}}
                    <el-slider
                            v-model="pI"
                            :min="0"
                            :max="15"
                            :step="0.1"
                            range>
                    </el-slider>
                    <h4>Charge Range</h4>
                    {{charge[0]}}-{{charge[1]}}
                    <el-slider
                            v-model="charge"
                            :min="-50"
                            :max="50"
                            :step="1"
                            range>
                    </el-slider>
                    <el-divider></el-divider>
                    <el-button size="medium" :type="type" :loading="searchLoading" icon="el-icon-search"
                               @click="filter">Search
                    </el-button>
                    <el-button size="medium" circle :loading="searchLoading" icon="el-icon-refresh" @click="reset">
                    </el-button>
                </el-col>
                <el-col :span="19" type="flex" justify="middle">
                    <el-pagination
                            style="margin-bottom: 18px"
                            background
                            :page-size.sync="pageSize"
                            :total="count"
                            :current-page.sync="currentPage"
                            layout="total, sizes, prev, next"
                            :page-sizes="[10, 20, 30]"
                            @size-change="handleSizeChange"
                            @current-change="handleCurrentChange">
                    </el-pagination>
                    <el-table
                            v-loading="tableLoading"
                            element-loading-spinner="el-icon-loading"
                            :data="tableData"
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
                                prop="pI"
                                label="pI"
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
                                label="Family ID"
                                header-align="center"
                                align="center">
                            <template slot-scope="scope">
                                <router-link :to="{path:'/family',query:{Family_ID:scope.row.Family_ID}}">
                                    <el-tag type="info">
                                        <i class="el-icon-connection"></i>{{ scope.row.Family_ID }}
                                    </el-tag>
                                </router-link>
                            </template>
                        </el-table-column>
                    </el-table>
                </el-col>
            </el-row>
        </el-card>
    </div>
</template>

<script>
    export default {
        name: 'AMP',

        data() {
            return {
                count: 0,
                pageSize: 10,
                currentPage: 1,
                tableData: [],
                tableLoading: false,

                type: 'primary',
                searchLoading: false,
                ampId: '',
                familyId: '',
                environment: [],
                sequence: '',
                length: [10, 100],
                pI: [0, 15],
                charge: [-50, 50],

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
            }
        },

        mounted() {
            if (Object.keys(this.$route.query).length !== 0) {
                if (this.$route.query.Family_ID) {
                    this.familyId = this.$route.query.Family_ID;
                }
                if (this.$route.query.Environment) {
                    this.environment.push(this.$route.query.Environment);
                }
            }
            this.tableLoading = true;
            this.search();
        },

        methods: {
            handleSizeChange() {
                this.tableLoading = true;
                this.search();
            },

            handleCurrentChange() {
                this.tableLoading = true;
                this.search();
            },

            filter() {
                this.type = 'danger';
                this.searchLoading = true;
                this.tableLoading = true;
                this.search();
            },

            reset() {
                this.ampId = '';
                this.familyId = '';
                this.environment = [];
                this.sequence = '';
                this.length = [10, 100];
                this.pI = [0, 15];
                this.charge = [-50, 50];
                this.filter()
            },

            search() {
                let self = this;
                this.axios.get('/amp/', {
                    params: {
                        pageSize: this.pageSize,
                        currentPage: this.currentPage,
                        ampId: this.ampId,
                        familyId: this.familyId,
                        environment: this.environment,
                        sequence: this.sequence,
                        minLength: this.length[0],
                        maxLength: this.length[1],
                        minpI: this.pI[0],
                        maxpI: this.pI[1],
                        minCharge: this.charge[0],
                        maxCharge: this.charge[1]
                    }
                }).then(function (response) {
                    if (response.status === 200) {
                        self.count = response.data['count'];
                        self.tableData = response.data['AMP'];
                    }
                    self.type = 'primary';
                    self.searchLoading = false;
                    self.tableLoading = false;
                }).catch(function (error) {
                    console.log(error);
                });
            }
        }
    }
</script>
