const path = require("path");
module.exports = {
    // where the client build files are saved
    outputDir: path.resolve(__dirname, "../server/public"),
    // for accessing the api from the client in dev env
    devServer: {
        proxy: {
            "/api": {
                target: "http://localhost:5000",
            },
        },
    },
    transpileDependencies: ["vuetify"],
    chainWebpack: (config) => {
        config.plugin("html").tap((args) => {
            args[0].title = "Pectoral Muscle Segmentation | Team 02 FYP";
            return args;
        });
    },
};
