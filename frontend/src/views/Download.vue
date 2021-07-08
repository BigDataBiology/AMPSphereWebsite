<template>
    <div class="Dwonload">
        <el-row type="flex" justify="left">
            <el-col :span="5" :offset="1" type="flex" justify="middle">
                <h2>Downloads</h2>
            </el-col>
        </el-row>

        <el-row type="flex" justify="center">
            <el-col type="flex" justify="middle">
                <el-card shadow="always">
                    <el-row type="flex" justify="center">
                        <el-col type="flex" justify="middle">
                            <el-tabs v-model="activeName" tab-position="left">
                                <el-tab-pane label="AMP DB" name="ampdb">
                                    <el-table
                                            v-loading="tableLoading"
                                            element-loading-spinner="el-icon-loading"
                                            :data="AMPDB"
                                            stripe
                                            border
                                            highlight-current-row>
                                        <el-table-column
                                                prop="name"
                                                label="Name"
                                                header-align="center"
                                                align="center"
                                                sortable>
                                        </el-table-column>
                                        <el-table-column
                                                prop="times"
                                                label="Download Times"
                                                header-align="center"
                                                align="center"
                                                sortable>
                                        </el-table-column>
                                        <el-table-column
                                                prop="time"
                                                label="Upload Time"
                                                header-align="center"
                                                align="center"
                                                sortable>
                                        </el-table-column>
                                        <el-table-column
                                                label="Download"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <el-button icon="el-icon-download" circle
                                                           @click=ampDbDownload(scope.row.name)>
                                                </el-button>
                                            </template>
                                        </el-table-column>
                                    </el-table>
                                </el-tab-pane>
                                <el-tab-pane label="HMMER DB" name="hmmerdb">
                                    <el-table
                                            v-loading="tableLoading"
                                            element-loading-spinner="el-icon-loading"
                                            :data="HMMERDB"
                                            stripe
                                            border
                                            highlight-current-row>
                                        <el-table-column
                                                prop="name"
                                                label="Name"
                                                header-align="center"
                                                align="center"
                                                sortable>
                                        </el-table-column>
                                        <el-table-column
                                                prop="times"
                                                label="Download Times"
                                                header-align="center"
                                                align="center"
                                                sortable>
                                        </el-table-column>
                                        <el-table-column
                                                prop="time"
                                                label="Upload Time"
                                                header-align="center"
                                                align="center"
                                                sortable>
                                        </el-table-column>
                                        <el-table-column
                                                label="Download"
                                                header-align="center"
                                                align="center">
                                            <template slot-scope="scope">
                                                <el-button icon="el-icon-download" circle
                                                           @click=hmmerDbDownload(scope.row.name)>
                                                </el-button>
                                            </template>
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
        name: 'Dwonload',

        data() {
            return {
                activeName: 'ampdb',

                AMPDB: [],
                HMMERDB: [],
                tableLoading: false,
            }
        },

        mounted() {
            let self = this;
            this.tableLoading = true;
            this.axios.get('/amp/db').then(function (response) {
                if (response.status === 200) {
                    self.AMPDB = response.data['AMPDB'];
                }
                self.tableLoading = false;
            }).catch(function (error) {
                console.log(error);
            });
            this.axios.get('/hmmer/db').then(function (response) {
                if (response.status === 200) {
                    self.HMMERDB = response.data['HMMERDB'];
                }
                self.tableLoading = false;
            }).catch(function (error) {
                console.log(error);
            });
        },

        methods: {
            ampDbDownload(name) {
                let self = this;
                this.tableLoading = true;
                this.axios.get('/amp/ampDbDownload', {
                    params: {
                        name: name
                    },
                    responseType: "blob"
                }).then(function (response) {
                    if (response.status === 200) {
                        var url = window.URL.createObjectURL(response.data);
                        var a = document.createElement("a");
                        document.body.appendChild(a);
                        a.href = url;
                        a.download = name;
                        a.click();
                    }
                    self.tableLoading = false;
                }).catch(function (error) {
                    console.log(error);
                });
            },
            hmmerDbDownload(name) {
                let self = this;
                this.tableLoading = true;
                this.axios.get('/hmmer/hmmerDbDownload', {
                    params: {
                        name: name
                    },
                    responseType: "blob"
                }).then(function (response) {
                    if (response.status === 200) {
                        var url = window.URL.createObjectURL(response.data);
                        var a = document.createElement("a");
                        document.body.appendChild(a);
                        a.href = url;
                        a.download = name;
                        a.click();
                    }
                    self.tableLoading = false;
                }).catch(function (error) {
                    console.log(error);
                });
            }
        }
    }
</script>
