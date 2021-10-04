<template>
  <div class="API">
    <h1>This is the API Reference / Manual page</h1>
    <v-card class="mx-auto about--card">
      <v-card-text>
        <div style="text-align:center" class="pa-md-6">
          <span class="POST">POST</span> <span class="Segment">Segment</span>
          <br />
          <br />
          <v-bottom-navigation :value="value" color="primary"
            ><h3>{api_url}/segment/{base64_string}</h3>
          </v-bottom-navigation>
          <br />
          <p class="text--primary text-body-1 mb-6">
            This Post Method with segment endpoint takes in a base64 encoded
            image in string format and gives a json response with the segmented
            image in base64 encoded string.
          </p>
          <br />
          <p class="text--primary text-body-1">
            A valid API call example will look like
          </p>
          <p class="api-url">
            {api_url}/segment/{base64_string}
          </p>
          <p>with response</p>
                    <p class="api-url">{"Segmented" : "base_64_image_string"}
          </p>
        </div>
      </v-card-text>
    </v-card>
  </div>
</template>

<style lang="scss" scoped>
.about--card {
  max-width: 1000px;
  width: 90%;
}
.team--wrapper {
  display: flex;
  flex-wrap: wrap;
  .team--card {
    max-width: 400px;
    width: 90%;
    margin: 20px;
    border-radius: 10px !important;
  }
  .col-half {
    width: 50%;
  }
}
@media only screen and (max-width: 790px) {
  .col-half {
    width: 100% !important;
  }
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
