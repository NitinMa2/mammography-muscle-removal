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
        </div>
        <!-- Spinner for Loading -->
        <div class="text-center mt-15">
            <v-progress-circular
                v-if="isLoading"
                indeterminate
                color="teal"
                size="40"
                width="5"
                class="spinner-custom"
            ></v-progress-circular>
        </div>
        <!-- Tabs component -->
        <Tabs v-if="segmentedImageSrc.length" />
    </v-container>
</template>

<script>
import SegmentationService from "@/services/SegmentationService";
import Tabs from "@/components/Tabs";

export default {
    name: "Home",

    components: {
        Tabs,
    },
    data: () => ({
        loader: null,
        uploadLoading: false,
        isLoading: false,
    }),
    computed: {
        segmentedImageSrc() {
            return this.$store.state.segmentedImageBase64;
        },
    },
    methods: {
        async handleUpload() {
            // fun fact api
            // url = "https://catfact.ninja/fact"
            // let response = await fetch(url);
            // let data = await response.json();
            // this.funFact = data.fact;

            // loading animation
            try {
                this.loader = "uploadLoading";
                this.$refs.imageInput.click();
            } catch (err) {
                console.log(err);
            }
        },
        async onImageSelected(event) {
            // reference: https://www.youtube.com/watch?v=J2Wp4_XRsWc

            // only if an image is selected
            if (event.target.files.length) {
                // set spinner
                this.isLoading = true;
                // set rating component
                this.$store.commit("setShowRatingComponent", true);

                // reset any current selection
                this.$store.commit("setOriginalImageBase64", "");
                this.$store.commit("setBase64Prefix", "");
                this.$store.commit("setSegmentedImageBase64", "");

                // handle image
                const image = event.target.files[0];
                let imagename = image.name;
                // validation
                if (imagename.lastIndexOf(".") <= 0) {
                    return alert("Please enter a vaild file");
                }
                const fileReader = new FileReader();
                fileReader.readAsDataURL(image);
                fileReader.addEventListener("load", () => {
                    // store the original image in the app state
                    this.$store.commit(
                        "setOriginalImageBase64",
                        fileReader.result
                    );
                    // store the image prefix in the app state
                    this.$store.commit(
                        "setBase64Prefix",
                        fileReader.result.split(",")[0] + ","
                    );
                    // API request to backend
                    SegmentationService.postMammogram(
                        fileReader.result.split(",")[1]
                    )
                        .then((res) => {
                            // store the segmented image in the app state
                            this.$store.commit("setSegmentedImageBase64", res);
                            // set spinner
                            this.isLoading = false;
                        })
                        .catch((e) => {
                            alert(
                                "There has been an error. Please contact our team."
                            );
                            // set spinner
                            this.isLoading = false;
                        });
                });
            }
        },
    },
    watch: {
        loader() {
            // loading animation logic
            const l = this.loader;
            this[l] = !this[l];

            setTimeout(() => (this[l] = false), 3000);

            this.loader = null;
        },
    },
};
</script>
