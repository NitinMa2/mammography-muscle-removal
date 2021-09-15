<template>
    <v-container>
        <v-card>
            <v-tabs v-model="tab" background-color="transparent" grow>
                <v-tab v-for="item in items" :key="item">
                    {{ item }}
                </v-tab>
            </v-tabs>

            <v-tabs-items v-model="tab">
                <v-tab-item v-for="item in items" :key="item">
                    <v-card class="d-flex justify-space-around pa-14" flat>
                        <div class="tab__image">
                            <img
                                v-if="tab === 0"
                                src="https://play-lh.googleusercontent.com/IeNJWoKYx1waOhfWF6TiuSiWBLfqLb18lmZYXSgsH1fvb8v1IYiZr5aYWe0Gxu-pVZX3"
                            />
                            <img
                                v-else
                                src="https://pbs.twimg.com/profile_images/1285655593592791040/HtwPZgej.jpg"
                            />
                        </div>
                        <div class="tab__actions">
                            <div class="tab__actions--buttons">
                                <v-btn
                                    :loading="downloadLoading"
                                    :disabled="downloadLoading"
                                    color="primary"
                                    class="ma-2 white--text"
                                >
                                    Download Output
                                    <v-icon right dark>
                                        mdi-cloud-download
                                    </v-icon>
                                </v-btn>

                                <v-btn
                                    :loading="emailLoading"
                                    :disabled="emailLoading"
                                    color="primary"
                                    class="ma-2 white--text"
                                >
                                    Email Output
                                    <v-icon right dark>
                                        mdi-email-send
                                    </v-icon>
                                </v-btn>
                            </div>
                            <div class="tab__actions--rate">
                                <p class="mr-2">Rate this result:</p>
                                <v-btn
                                    class="mt-n3"
                                    text
                                    icon
                                    color="blue lighten-2"
                                >
                                    <v-icon>mdi-thumb-up</v-icon>
                                </v-btn>
                                <v-btn
                                    class="mt-n3"
                                    text
                                    icon
                                    color="red lighten-2"
                                >
                                    <v-icon>mdi-thumb-down</v-icon>
                                </v-btn>
                            </div>
                        </div>
                    </v-card>
                </v-tab-item>
            </v-tabs-items>
        </v-card>
    </v-container>
</template>

<script>
export default {
    name: "Tabs",

    data: () => ({
        loader: null,
        downloadLoading: false,
        emailLoading: false,
        tab: null,
        items: ["Original", "Segmented"],
        imageSource: "",
    }),
    watch: {
        loader() {
            const l = this.loader;
            this[l] = !this[l];

            setTimeout(() => (this[l] = false), 3000);

            this.loader = null;
        },
    },
};
</script>

<style scoped>
/* ----------- */
/* Tabs Content */
/* ----------- */
.tab__image img {
    max-width: 300px;
}
.tab__actions {
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
</style>
