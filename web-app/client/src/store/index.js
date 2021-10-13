import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    // app state
    state: {
        originalImageBase64: "",
        segmentedImageBase64: "",
        base64Prefix: "",
        showRatingComponent: true,
    },
    // manipulating the app state
    mutations: {
        setOriginalImageBase64(state, base64) {
            state.originalImageBase64 = base64;
        },
        setSegmentedImageBase64(state, base64) {
            state.segmentedImageBase64 = base64;
        },
        setBase64Prefix(state, prefix) {
            state.base64Prefix = prefix;
        },
        setShowRatingComponent(state, bool) {
            state.showRatingComponent = bool;
        },
    },
    actions: {},
    modules: {},
});
