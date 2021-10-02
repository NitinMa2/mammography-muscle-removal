<template>
    <v-navigation-drawer dark app permanent expand-on-hover>
        <v-list>
            <v-list-item class="px-2">
                <v-list-item-avatar>
                    <img src="@/assets/monash-logo.jpg" alt="monash logo" />
                </v-list-item-avatar>
            </v-list-item>

            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class="text-h6">
                        Pectoral Muscle
                    </v-list-item-title>
                    <v-list-item-title class="text-h6">
                        Removal
                    </v-list-item-title>
                    <v-list-item-subtitle>Team 02</v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list nav dense flat>
            <v-list-item link :to="{ name: 'Home' }">
                <v-list-item-icon>
                    <v-icon>mdi-view-dashboard</v-icon>
                </v-list-item-icon>
                <v-list-item-title>Home</v-list-item-title>
            </v-list-item>
            <v-list-item link :to="{ name: 'Team' }">
                <v-list-item-icon>
                    <v-icon>mdi-account-group</v-icon>
                </v-list-item-icon>
                <v-list-item-title>Meet The Team</v-list-item-title>
            </v-list-item>
            <v-list-item link :to="{ name: 'API' }">
                <v-list-item-icon>
                    <v-icon>mdi-api</v-icon>
                </v-list-item-icon>
                <v-list-item-title>API Reference</v-list-item-title>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>

<script>
export default {};
</script>

<style></style>
