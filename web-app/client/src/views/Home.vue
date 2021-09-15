<template>
    <v-container>
        <!-- Title -->
        <h1>Automated Pectoral Muscle Removal System for Mammograms</h1>

        <!-- Upload -->
        <div class="div__upload">
            <v-btn
                :loading="uploadLoading"
                :disabled="uploadLoading"
                color="teal darken-1"
                class="ma-2 white--text"
                @click="handleUpload"
            >
                Upload Image
                <v-icon right dark>
                    mdi-cloud-upload
                </v-icon>
            </v-btn>
            <p v-if="funFact.length != 0" id="fact">{{ funFact }}</p>
        </div>
        <Tabs />
    </v-container>
</template>

<script>
import SegmentationService from "@/SegmentationService";
import Tabs from "@/components/Tabs";

export default {
    name: "Home",

    components: {
        Tabs,
    },
    data: () => ({
        funFact: "Fun Fact API",
        loader: null,
        uploadLoading: false,
    }),
    methods: {
        async handleUpload() {
            // url = "https://catfact.ninja/fact"
            // let response = await fetch(url);
            // let data = await response.json();

            // this.funFact = data.fact;
            try {
                this.loader = "uploadLoading";
                await SegmentationService.postDocument();
                this.funFact = await SegmentationService.getDocuments();
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
