module.exports = {
    publicPath: './',
    outputDir: 'dist',
    lintOnSave: true,
    runtimeCompiler: true, //关键点在这
    // 调整内部的 webpack 配置。
    // 查阅 https://github.com/vuejs/vue-doc-zh-cn/vue-cli/webpack.md
    chainWebpack: (config) => {
        config
            .plugin('html')
            .tap(args => {
                args[0].title = 'AMPSphere'
                args[0].meta = {viewport: 'width=device-width,initial-scale=1,user-scalable=no'}
                return args
            })
    },
    configureWebpack: {
        externals: {
            "plotly.js": "Plotly",
        }
    },
    devServer: {
        open: process.platform === 'darwin',
        host: '0.0.0.0',
        port: 8080,
        https: false,
        hotOnly: false,
        // 查阅 https://github.com/vuejs/vue-doc-zh-cn/vue-cli/cli-service.md#配置代理
        proxy: null, // string | Object
    },
    pluginOptions: {
        quasar: {
            importStrategy: 'kebab',
            rtlSupport: false
        }
    },
    transpileDependencies: [
        'quasar'
    ]
}