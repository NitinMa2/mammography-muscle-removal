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

p,
h1,
h2,
h3,
h4,
h5,
h6,
button,
input,
textarea {
    font-family: "Roboto", sans-serif;
}

h1 {
    text-align: center;
    font-weight: 500;
    max-width: 600px;
    margin: 30px auto;
}

button {
    background-color: #4db7d8;
    color: #ffffff;
    padding: 10px 20px;
    margin: 5px;
    border-radius: 8px;
    border: none;
    font-size: 1.2em;
}

button:hover {
    box-shadow: rgba(100, 100, 111, 0.3) 0px 7px 29px 0px;
    transform: translateY(-5px);
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

/* ---- */
/* Tabs */
/* ---- */
.tabs {
    display: flex;
    flex-wrap: wrap;
    max-width: 800px;
    margin: 50px auto;
    padding: 20px 30px;
    border-radius: 8px;
    box-shadow: rgba(115, 197, 222, 0.45) 0px 3px 18px;
    justify-content: center;
}
.tabs input[type="radio"] {
    display: none;
}
.tabs label {
    padding: 8px 17px;
    margin-right: 10px;
    transition: none;
    order: 0;
}
.tabs input[type="radio"]:checked + label {
    border-bottom: solid 5px #4db7d8;
}
.tab__content {
    width: 100%;
    padding-top: 30px;
    display: none;
    order: 1;
}
/* Logic to display the correct tabs */
.tabs input[type="radio"]:checked + label + .tab__content {
    display: flex;
}

/* ----------- */
/* Tabs Content */
/* ----------- */
.tab__image img {
    max-width: 300px;
}
.tab__actions {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.tab__actions--buttons {
    display: flex;
    flex-direction: column;
}
.tab__actions--rate {
    display: flex;
    align-items: center;
    margin-top: 20px;
}
/* Rating */
.rate__icon {
    margin: 7px;
    font-size: 1.5em;
}
.rate__icon:hover {
    transform: scale(1.2);
}
.rate__icon--green {
    color: rgb(3, 151, 3);
}
.rate__icon--red {
    color: rgb(201, 0, 0);
}
</style>
