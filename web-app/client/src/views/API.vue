<template>
    <div class="api pt-10 pb-10">
        <h1>API Reference</h1>
        <p class="subhead mb-10">
            Feel free to run our segmentation algorithm through an API request
            or even integrate it in a project of your own! Do let our team know
            if you plan to use the API as it will mean a lot for us to know that
            it is of use to others.
        </p>
        <v-card class="mx-auto about--card">
            <v-card-text>
                <div style="text-align:center" class="pa-md-6">
                    <span class="POST">Segment</span>
                    <span class="Segment"> Endpoint</span>
                    <v-bottom-navigation color="primary" class="mt-5 pt-1"
                        ><h3>https://team02-fyp-api.herokuapp.com/segment</h3>
                    </v-bottom-navigation>
                    <br />
                    <p class="text--primary text-body-1">
                        A valid API call should be made as a
                        <strong>POST</strong> request to
                    </p>
                    <p class="api-url">
                        https://team02-fyp-api.herokuapp.com/segment
                    </p>
                    <p>with a JSON body</p>
                    <p class="api-url">
                        { "base64Image" : "base_64_image_string" }
                    </p>
                    <p>
                        <strong>Note: </strong>
                        <code>base_64_image_string</code> is the base64 encoding
                        of a digital mammogram with a MLO view.
                    </p>
                    <p>
                        <strong>Example: </strong>
                        <code>{ "base64Image" : "asdaGVsbG8=" }</code>
                    </p>
                </div>
            </v-card-text>
        </v-card>
    </div>
</template>

<style lang="scss" scoped>
.subhead {
    max-width: 800px;
    width: 90%;
    margin-left: auto;
    margin-right: auto;
    text-align: center;
}
.about--card {
    max-width: 1000px;
    width: 90%;
}

.v-bottom-navigation.v-item-group.theme--light {
    background-color: lightgray;
}

h3 {
    color: #3366bb;
}

h3 {
    margin-top: 1.75%;
}

p.api-url {
    color: #3366bb;
}

span.POST {
    color: #3366bb;
    font-size: x-large;
}

span.Segment {
    font-size: x-large;
}
</style>
