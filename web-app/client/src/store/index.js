import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        originalImageSrc: "",
        segmentedImageSrc: "",
    },
    mutations: {
        setOriginalImageSrc(state, src) {
            // state.originalImageSrc = src;
            state.originalImageSrc = require("@/assets/original.jpg");
            // console.log(src.split(",")[1]);
        },
        setSegmentedImageSrc(state, src) {
            // state.originalImageSrc = src;
            state.segmentedImageSrc = require("@/assets/segmented.jpg");
            // console.log(src.split(",")[1]);
        },
    },
    actions: {},
    modules: {},
});
