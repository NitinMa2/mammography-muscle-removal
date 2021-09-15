<template>
    <div>
        <!-- Title -->
        <h1>Automated Pectoral Muscle Removal System for Mammograms</h1>

        <!-- Upload -->
        <div class="div__upload">
            <button @click="handleUpload">
                <i class="fa fa-upload"></i>
                Upload Image
            </button>
            <p v-if="funFact.length != 0" id="fact">{{ funFact }}</p>
        </div>

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
                    <!-- <img src="@/assets/placeholder.png" /> -->
                </div>
                <div class="tab__actions">
                    <div class="tab__actions--buttons">
                        <button>
                            <i class="fa fa-download"></i>
                            Download Output
                        </button>

                        <button>
                            <i class="fa fa-envelope"></i>
                            Email Output
                        </button>
                    </div>
                    <div class="tab__actions--rate">
                        <p>Rate this result:</p>
                        <div class="rate__icon rate__icon--green">
                            <i class="fa fa-smile-o"></i>
                        </div>
                        <div class="rate__icon rate__icon--red">
                            <i class="fa fa-frown-o"></i>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Segmented Tab -->
            <input type="radio" id="segmented" name="segmentation-tabs" />
            <label for="segmented">Segmented</label>
            <div class="tab__content">
                <div class="tab__image">
                    <!-- <img src="@/assets/placeholder2.png" /> -->
                </div>
                <div class="tab__actions">
                    <div class="tab__actions--buttons">
                        <button>
                            <i class="fa fa-download"></i>
                            Download Output
                        </button>

                        <button>
                            <i class="fa fa-envelope"></i>
                            Email Output
                        </button>
                    </div>
                    <div class="tab__actions--rate">
                        <p>Rate this result:</p>
                        <div class="rate__icon rate__icon--green">
                            <i class="fa fa-smile-o"></i>
                        </div>
                        <div class="rate__icon rate__icon--red">
                            <i class="fa fa-frown-o"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "HelloWorld",

    data: () => ({
        funFact: "Fun Fact API",
    }),
    methods: {
        async handleUpload() {
            // url = "https://catfact.ninja/fact"
            // let response = await fetch(url);
            // let data = await response.json();

            // this.funFact = data.fact;
            try {
                await SegmentationService.postDocument();
                this.funFact = await SegmentationService.getDocuments();
            } catch (err) {
                console.log(err);
            }
        },
    },
};
</script>
