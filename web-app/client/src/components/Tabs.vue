<template>
    <div>
        <!-- Tabs -->
        <div class="tabs">
            <!-- Original Tab -->
            <input
                type="radio"
                id="original"
                name="segmentation-tabs"
                checked="checked"
            />
            <label for="original">Original</label>
            <div class="tab__content">
                <div class="tab__image">
                    <img src="@/assets/placeholder.png" />
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
                        <v-btn class="mt-n3" text icon color="blue lighten-2">
                            <v-icon>mdi-thumb-up</v-icon>
                        </v-btn>
                        <v-btn class="mt-n3" text icon color="red lighten-2">
                            <v-icon>mdi-thumb-down</v-icon>
                        </v-btn>
                    </div>
                </div>
            </div>

            <!-- Segmented Tab -->
            <input type="radio" id="segmented" name="segmentation-tabs" />
            <label for="segmented">Segmented</label>
            <div class="tab__content">
                <div class="tab__image">
                    <img src="@/assets/placeholder2.png" />
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
                        <v-btn class="mt-n3" text icon color="blue lighten-2">
                            <v-icon>mdi-thumb-up</v-icon>
                        </v-btn>
                        <v-btn class="mt-n3" text icon color="red lighten-2">
                            <v-icon>mdi-thumb-down</v-icon>
                        </v-btn>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Tabs",

    data: () => ({
        loader: null,
        downloadLoading: false,
        emailLoading: false,
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
    box-shadow: #b2dfdb 0px 3px 18px;
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
    border-bottom: solid 5px #00897b;
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
</style>
