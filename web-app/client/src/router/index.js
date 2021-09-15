import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import Team from "@/views/Team.vue";
import API from "@/views/API.vue";

Vue.use(VueRouter);

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/team",
        name: "Team",
        component: Team,
    },
    {
        path: "/api-reference",
        name: "API",
        component: API,
    },
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes,
});

export default router;
