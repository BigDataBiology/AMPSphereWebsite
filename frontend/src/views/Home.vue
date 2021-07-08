<template>
    <div class="Home">
        <el-row type="flex" justify="center">
            <el-image style="width: 25%" :src="url" lazy></el-image>
        </el-row>

        <el-row type="flex" justify="center">
            <h1>Welecome to Global AMP Survey database (GAS).</h1>
        </el-row>

        <el-row type="flex" justify="center">
            <el-col type="flex" justify="middle">
                <el-card shadow="always">
                    <div slot="header">
                        About
                    </div>
                    <div>
                        <p>Blah, blah, blah...</p>
                    </div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        name: 'Home',

        data() {
            return {
                url: require('../assets/logo.png'),
            }
        },

        mounted() {
            this.axios.post('/home/index').then(function (response) {
                if (response.status === 200) {
                    console.log('你在电脑前看这段文字，\n' +
                        '写文字的人在百度等你。\n' +
                        'N年前你来到了这个世界，\n' +
                        'N年后你想改变世界。\n' +
                        '\n' +
                        '期待你脚踏祥云，\n' +
                        '与百度一起改变世界。')
                }
            }).catch(function (error) {
                console.log(error);
            });
        }
    }
</script>
