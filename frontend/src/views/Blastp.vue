<template>
    <div class="Blastp">
        <el-row type="flex" justify="left">
            <el-col :span="5" :offset="1" type="flex" justify="middle">
                <h2>BLASTP</h2>
            </el-col>
        </el-row>

        <el-row type="flex" justify="center">
            <el-col type="flex" justify="middle">
                <el-card :shadow="shadow">
                    <el-row type="flex" justify="center">
                        <el-col type="flex" justify="middle">
                            <el-tabs v-loading="tabLoading" element-loading-spinner="el-icon-loading"
                                     v-model="activeName" tab-position="left">
                                <el-tab-pane label="Query" name="query">
                                    <h4>Query Method</h4>
                                    <el-row type="flex" justify="left">
                                        <el-switch
                                                v-model="sequenceType"
                                                inactive-text="Paste sequences in FASTA format."
                                                active-text="OR Submit a file in FASTA format.">
                                        </el-switch>
                                    </el-row>
                                    <el-row style="margin-top: 18px" type="flex" justify="left">
                                        <el-input v-if="!sequenceType" type="textarea" v-model="sequence"
                                                  :maxlength="1000" show-word-limit
                                                  :rows="6"
                                                  resize="none" clearable>
                                        </el-input>
                                        <el-upload v-else
                                                   ref="upload"
                                                   :action="$baseURL+'/blastp/file'"
                                                   :data="uploadData"
                                                   drag
                                                   :auto-upload="false"
                                                   :limit="1"
                                                   :on-success="handleSuccess"
                                                   :on-error="handleError"
                                                   :before-upload="beforeUpload">
                                            <i class="el-icon-upload"></i>
                                            <div class="el-upload__text">Drag or click here to upload</div>
                                            <div class="el-upload__tip" slot="tip">FASTA format, limited to 500kb.</div>
                                        </el-upload>
                                    </el-row>
                                    <el-button v-if="!sequenceType" type="text" @click="pasteExample">Paste example
                                    </el-button>
                                    <h4>E-value</h4>
                                    <el-row type="flex" justify="left">
                                        <el-col :span="6" type="flex" justify="middle">
                                            <el-input v-model="evalue" clearable></el-input>
                                        </el-col>
                                    </el-row>
                                    <h4>Results Type</h4>
                                    <el-row type="flex" justify="left">
                                        <el-switch
                                                v-model="resultType"
                                                inactive-text="Get results from this web page."
                                                active-text="OR get results by downloading a file.">
                                        </el-switch>
                                    </el-row>
                                    <el-button style="margin-top: 18px" size="medium" :type="type" :loading="runLoading"
                                               :icon="icon"
                                               @click="run">RUN
                                    </el-button>
                                    <el-divider></el-divider>
                                    <el-row type="flex" justify="center">
                                        <h4>Results</h4>
                                    </el-row>
                                    <el-row type="flex" justify="center">
                                        <el-table
                                                v-if="!resultType"
                                                v-loading="tableLoading"
                                                element-loading-spinner="el-icon-loading"
                                                :data="Blastp_Sequence_Results"
                                                stripe
                                                border
                                                highlight-current-row>
                                            <el-table-column
                                                    prop="qseqid"
                                                    label="qseqid"
                                                    header-align="center"
                                                    align="center"
                                                    sortable>
                                            </el-table-column>
                                            <el-table-column
                                                    label="AMP ID"
                                                    header-align="center"
                                                    align="center"
                                                    sortable>
                                                <template slot-scope="scope">
                                                    <router-link
                                                            :to="{path:'/amp_card',query:{AMP_ID:scope.row.AMP_ID}}">
                                                        <el-tag type="info">
                                                            <i class="el-icon-connection"></i>{{scope.row.AMP_ID}}
                                                        </el-tag>
                                                    </router-link>
                                                </template>
                                            </el-table-column>
                                            <el-table-column
                                                    prop="Family_ID"
                                                    label="Family ID"
                                                    header-align="center"
                                                    align="center"
                                                    sortable>
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
                                                    prop="evalue"
                                                    label="evalue"
                                                    header-align="center"
                                                    align="center"
                                                    sortable>
                                            </el-table-column>
                                            <el-table-column
                                                    prop="score"
                                                    label="score"
                                                    header-align="center"
                                                    align="center"
                                                    sortable>
                                            </el-table-column>
                                            <el-table-column
                                                    prop="qcovs"
                                                    label="qcovs"
                                                    header-align="center"
                                                    align="center"
                                                    sortable>
                                            </el-table-column>
                                        </el-table>
                                        <el-button v-if="resultType&&!isNull" icon="el-icon-download" circle
                                                   @click=download()>
                                        </el-button>
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
        name: 'Blastp',

        data() {
            return {
                isNull: true,
                activeName: 'query',
                tabLoading: false,

                sequenceType: false,
                sequence: '',
                evalue: '10.0',
                resultType: false,
                type: 'primary',
                icon: 'el-icon-video-play',
                runLoading: false,

                Blastp_Sequence_Results: [],
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
            },
            uploadData: function () {
                return {
                    evalue: this.evalue,
                    resultType: this.resultType
                }
            }
        },

        methods: {
            pasteExample() {
                this.sequence = '>E1\n' +
                    'AAAAAAAARLSVLAAATPVALRWLLAVLARHRLVVM\n' +
                    '>E2\n' +
                    'AAAAAAAHEPPRGQPGRIKRTQGAQGKDGCGLAARAL\n' +
                    '>E3\n' +
                    'AAAAAAAHEPPRGQPGRIKRTQGAQGKEGCGLAARAL\n' +
                    '>E4\n' +
                    'AAAAAAGISLLGAAGLRRKRK'
            },

            run() {
                if (this.sequence !== "" && !this.sequenceType) {
                    this.type = 'danger';
                    this.icon = 'el-icon-loading'
                    this.runLoading = true;
                    this.isNull = true;
                    this.tableLoading = true;
                    let self = this;
                    this.axios.post('/blastp/index', this.$qs.stringify({
                        sequence: this.sequence,
                        evalue: this.evalue,
                        resultType: this.resultType
                    }))
                        .then(function (response) {
                            if (response.status === 200) {
                                self.Blastp_Sequence_Results = response.data['Blastp_Sequence_Results'];
                                self.isNull = false;
                            }
                            self.type = 'primary';
                            self.icon = 'el-icon-video-play';
                            self.runLoading = false;
                            self.tableLoading = false;
                        }).catch(function (error) {
                        console.log(error);
                    });
                } else if (this.sequenceType) {
                    this.$refs.upload.submit();
                } else {
                    this.Blastp_Sequence_Results = [];
                    this.isNull = true;
                }
            },

            beforeUpload(file) {
                this.type = 'danger';
                this.icon = 'el-icon-loading'
                this.runLoading = true;
                this.isNull = true;
                this.tableLoading = true;

                const isLt500kb = file.size < 512 * 1024;
                if (!isLt500kb) {
                    this.type = 'primary';
                    this.icon = 'el-icon-video-play';
                    this.runLoading = false;
                    this.Blastp_Sequence_Results = [];
                    this.isNull = true;
                    this.tableLoading = false;
                    this.$message.error('The file is limited to 500kb.');
                }
                return isLt500kb;
            },

            handleSuccess(response) {
                this.Blastp_Sequence_Results = response['Blastp_Sequence_Results'];
                this.isNull = false;
                this.type = 'primary';
                this.icon = 'el-icon-video-play';
                this.runLoading = false;
                this.tableLoading = false;
            },

            handleError() {
                this.$message.error('The file is limited to 500kb.');
                this.Blastp_Sequence_Results = [];
                this.isNull = false;
                this.type = 'primary';
                this.icon = 'el-icon-video-play';
                this.runLoading = false;
                this.tableLoading = false;
            },

            download() {
                let self = this;
                this.tabLoading = true;
                this.axios.get('/blastp/download', {
                    params: {
                        url: this.Blastp_Sequence_Results
                    },
                    responseType: "blob"
                }).then(function (response) {
                    if (response.status === 200) {
                        var url = window.URL.createObjectURL(response.data);
                        var a = document.createElement("a");
                        document.body.appendChild(a);
                        a.href = url;
                        a.download = 'output.txt';
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
