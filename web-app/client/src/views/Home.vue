<template>
    <v-container>
        <!-- Title -->
        <h1>Automated Pectoral Muscle Removal System for Mammograms</h1>

        <!-- Upload -->
        <div class="div__upload">
            <v-btn
                :loading="uploadLoading"
                :disabled="uploadLoading"
                color="primary"
                class="ma-2 white--text"
                @click="handleUpload"
            >
                Upload Image
                <v-icon right dark>
                    mdi-cloud-upload
                </v-icon>
            </v-btn>
            <input
                type="file"
                style="display: none"
                ref="imageInput"
                accept="image/*"
                @change="onImageSelected"
            />
            <!-- <p v-if="funFact.length != 0" id="fact">{{ funFact }}</p> -->
        </div>
        <Tabs v-if="originalImageSrc.length" />
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
    computed: {
        originalImageSrc() {
            return this.$store.state.originalImageSrc;
        },
    },
    methods: {
        async handleUpload() {
            // url = "https://catfact.ninja/fact"
            // let response = await fetch(url);
            // let data = await response.json();

            // this.funFact = data.fact;
            try {
                this.loader = "uploadLoading";
                this.$refs.imageInput.click();

                // await SegmentationService.postDocument();
                // this.funFact = await SegmentationService.getDocuments();
            } catch (err) {
                console.log(err);
            }
        },
        onImageSelected(event) {
            // https://www.youtube.com/watch?v=J2Wp4_XRsWc
            const image = event.target.files[0];
            let imagename = image.name;
            // validation
            if (imagename.lastIndexOf(".") <= 0) {
                return alert("Please enter a vaild file");
            }
            const fileReader = new FileReader();
            fileReader.readAsDataURL(image);
            fileReader.addEventListener("load", () => {
                // this.imageUrl = fileReader.result;
                // console.log(fileReader.result);
                this.$store.commit("setOriginalImageSrc", fileReader.result);
                this.$store.commit("setSegmentedImageSrc", fileReader.result);
            });
            // console.log(image);
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
