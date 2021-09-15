import Vue from "vue";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";

Vue.use(Vuetify);

const opts = {
    theme: {
        themes: {
            light: {
                primary: "#388F81",
            },
            dark: {
                primary: "#388F81",
            },
        },
    },
};

export default new Vuetify(opts);
