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
</style>
