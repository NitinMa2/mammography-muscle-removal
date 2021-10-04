<template>
    <div class="team pt-10 pb-10">
        <h1>About The Project</h1>
        <v-card class="mx-auto about--card">
            <v-card-text>
                <div style="text-align:center" class="pa-md-6">
                    <div class="text-h5">Inspiration</div>
                    <p class="text--primary text-body-1 mb-6">
                        In 2020, there were 2.3 million women diagnosed with
                        breast cancer making it the most prevalent type of
                        cancer. According to the World Health Organization,
                        early detection is the best method of combating this
                        condition. This project is one part of a larger
                        operation to develop an automated breast cancer
                        detection system.
                    </p>
                    <div class="text-h5">Challenge</div>
                    <p class="text--primary text-body-1 mb-6">
                        A major difficulty in detecting breast cancer from
                        mammograms is that the density of calcified tissue
                        closely resembles that of the pectoral muscle, so it
                        takes on a similar appearance in a digital mammogram and
                        leads to false positives.
                    </p>
                    <div class="text-h5">Aspiration</div>
                    <p class="text--primary text-body-1">
                        The goal of this project is to automatically detect and
                        remove the pectoral muscle region so that detection of
                        breast cancer is accurate.
                    </p>
                </div>
            </v-card-text>
        </v-card>
        <h1>The Team</h1>
        <div class="text-body-1">
            <p style="text-align: center">
                We are an international team of students who developed this as
                part of our Final Year Project at Monash University.
            </p>
            <p style="text-align: center">
                Our team hopes that this project serves as a valuable
                contribution towards the field of beast cancer detection.
            </p>
        </div>
        <div class="team--wrapper">
            <!-- James -->
            <div class="col-half">
                <v-card class="mx-auto team--card" tile>
                    <v-img
                        height="100%"
                        src="https://cdn.vuetifyjs.com/images/cards/server-room.jpg"
                        gradient="to top right, rgba(100,115,201,.33), rgba(25,32,72,.8)"
                        class="pb-4"
                    >
                        <v-row align="end" class="fill-height">
                            <v-col align-self="start" class="pa-0" cols="12">
                                <v-avatar
                                    class="profile"
                                    color="grey"
                                    size="164"
                                    tile
                                >
                                    <img src="@/assets/james.jpeg" />
                                </v-avatar>
                            </v-col>
                            <v-col class="py-0">
                                <v-list-item color="rgba(0, 0, 0, .4)" dark>
                                    <v-list-item-content>
                                        <v-list-item-title class="text-h6">
                                            James Gan
                                        </v-list-item-title>
                                        <v-list-item-subtitle
                                            class="text-uppercase"
                                            >Project
                                            Manager</v-list-item-subtitle
                                        >
                                    </v-list-item-content>
                                </v-list-item>
                            </v-col>
                        </v-row>
                    </v-img>
                </v-card>
            </div>
            <div class="col-half">
                <!-- Nitin -->
                <v-card class="mx-auto team--card" tile>
                    <v-img
                        height="100%"
                        src="https://cdn.vuetifyjs.com/images/cards/server-room.jpg"
                        gradient="to top right, rgba(100,115,201,.33), rgba(25,32,72,.8)"
                        class="pb-4"
                    >
                        <v-row align="end" class="fill-height">
                            <v-col align-self="start" class="pa-0" cols="12">
                                <v-avatar
                                    class="profile"
                                    color="grey"
                                    size="164"
                                    tile
                                >
                                    <img src="@/assets/nitin.png" />
                                </v-avatar>
                            </v-col>
                            <v-col class="py-0">
                                <v-list-item color="rgba(0, 0, 0, .4)" dark>
                                    <v-list-item-content>
                                        <v-list-item-title class="text-h6">
                                            Nitin Mathew
                                        </v-list-item-title>
                                        <v-list-item-subtitle
                                            class="text-uppercase"
                                            >Tech Lead</v-list-item-subtitle
                                        >
                                    </v-list-item-content>
                                </v-list-item>
                            </v-col>
                        </v-row>
                    </v-img>
                </v-card>
            </div>
            <div class="col-half">
                <!-- Usama -->
                <v-card class="mx-auto team--card" tile>
                    <v-img
                        height="100%"
                        src="https://cdn.vuetifyjs.com/images/cards/server-room.jpg"
                        gradient="to top right, rgba(100,115,201,.33), rgba(25,32,72,.8)"
                        class="pb-4"
                    >
                        <v-row align="end" class="fill-height">
                            <v-col align-self="start" class="pa-0" cols="12">
                                <v-avatar
                                    class="profile"
                                    color="grey"
                                    size="164"
                                    tile
                                >
                                    <img src="@/assets/usama.jpg" />
                                </v-avatar>
                            </v-col>
                            <v-col class="py-0">
                                <v-list-item color="rgba(0, 0, 0, .4)" dark>
                                    <v-list-item-content>
                                        <v-list-item-title class="text-h6">
                                            Usama Mian
                                        </v-list-item-title>
                                        <v-list-item-subtitle
                                            class="text-uppercase"
                                            >Research Lead</v-list-item-subtitle
                                        >
                                    </v-list-item-content>
                                </v-list-item>
                            </v-col>
                        </v-row>
                    </v-img>
                </v-card>
            </div>
            <div class="col-half">
                <!-- Yasir -->
                <v-card class="mx-auto team--card" tile>
                    <v-img
                        height="100%"
                        src="https://cdn.vuetifyjs.com/images/cards/server-room.jpg"
                        gradient="to top right, rgba(100,115,201,.33), rgba(25,32,72,.8)"
                        class="pb-4"
                    >
                        <v-row align="end" class="fill-height">
                            <v-col align-self="start" class="pa-0" cols="12">
                                <v-avatar
                                    class="profile"
                                    color="grey"
                                    size="164"
                                    tile
                                >
                                    <img src="@/assets/yasir.png" />
                                </v-avatar>
                            </v-col>
                            <v-col class="py-0">
                                <v-list-item color="rgba(0, 0, 0, .4)" dark>
                                    <v-list-item-content>
                                        <v-list-item-title class="text-h6">
                                            Yasir Azhari
                                        </v-list-item-title>
                                        <v-list-item-subtitle
                                            class="text-uppercase"
                                            >Quality
                                            Assurance</v-list-item-subtitle
                                        >
                                    </v-list-item-content>
                                </v-list-item>
                            </v-col>
                        </v-row>
                    </v-img>
                </v-card>
            </div>
        </div>
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
</style>
