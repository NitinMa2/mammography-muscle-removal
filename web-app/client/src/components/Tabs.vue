<template>
    <v-container>
        <v-card>
            <v-tabs
                v-model="tab"
                background-color="transparent"
                grow
                show-arrows
            >
                <v-tabs-slider color="teal lighten-3"></v-tabs-slider>
                <v-tab v-for="item in items" :key="item">
                    {{ item }}
                </v-tab>
            </v-tabs>

            <v-tabs-items v-model="tab">
                <v-tab-item v-for="item in items" :key="item">
                    <v-card
                        class="d-flex flex-column flex-md-row justify-space-around pa-4 pa-sm-14"
                        flat
                    >
                        <div class="tab__image text-center">
                            <img v-if="tab === 0" :src="originalImageSrc" />
                            <img v-else :src="segmentedImageSrc" />
                        </div>
                        <div class="tab__actions">
                            <div class="tab__actions--buttons">
                                <v-btn
                                    :loading="downloadLoading"
                                    :disabled="downloadLoading"
                                    color="primary"
                                    class="ma-2 white--text"
                                    @click="handleDownload"
                                >
                                    Download Output
                                    <v-icon right dark>
                                        mdi-cloud-download
                                    </v-icon>
                                </v-btn>

                                <!-- <v-btn
                                    :loading="emailLoading"
                                    :disabled="emailLoading || true"
                                    color="primary"
                                    class="ma-2 white--text"
                                >
                                    Email Output
                                    <v-icon right dark>
                                        mdi-email-send
                                    </v-icon>
                                </v-btn> -->
                            </div>
                            <div
                                class="tab__actions--rate d-flex flex-column flex-sm-row"
                            >
                                <p class="mr-sm-2">Rate this result:</p>
                                <div>
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
        // emailLoading: false,
        tab: null,
        items: ["Original", "Segmented"],
        imageSource: "",
    }),
    computed: {
        originalImageSrc() {
            return this.$store.state.originalImageBase64;
        },
        segmentedImageSrc() {
            return (
                this.$store.state.base64Prefix +
                this.$store.state.segmentedImageBase64
            );
        },
    },
    methods: {
        handleDownload() {
            // download the image
            try {
                let link = document.createElement("a");
                document.body.appendChild(link);
                link.setAttribute("href", this.segmentedImageSrc);
                link.setAttribute("download", "segmented-image");
                link.click();
                document.body.removeChild(link);
            } catch (err) {
                console.log(err);
            }
        },
    },
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
    width: 80%;
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
