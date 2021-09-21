<template>
    <v-app id="inspire">
        <NavBar />

        <v-main>
            <router-view />
        </v-main>
    </v-app>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
export default {
    name: "App",
    components: { NavBar },
};
</script>

<style lang="scss">
* {
    margin: 0;
    padding: 0;
    -moz-box-sizing: border-box;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    transition: all 0.5s;
}

h1 {
    text-align: center;
    font-weight: 500;
    max-width: 600px;
    margin: 30px auto;
}

.v-application {
    background-color: rgb(245, 245, 245) !important;
}

/* ------ */
/* Upload */
/* ------ */
.div__upload {
    width: 100%;
    text-align: center;
}
#fact {
    margin: 30px auto 0 auto;
    max-width: 600px;
}
/* --------------------- */
/* Responsive Typography */
/* --------------------- */
@media (max-width: 768px) {
    h1 {
        font-size: 5vw;
    }
}
@media (max-width: 470px) {
    h1 {
        font-size: 6.5vw;
    }
    .v-btn__content {
        font-size: 11px;
    }
}
</style>
