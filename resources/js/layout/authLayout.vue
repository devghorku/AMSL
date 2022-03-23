<template>
    <v-app v-cloak>
        <v-main >
            <router-view/>
        </v-main>
        <v-snackbar
                :timeout="2500"
                :value="!!snackbar.message"
                right
                top
                :color="snackbar.type"
        >
            {{snackbar.message}}
            <template v-slot:action="{ attrs }">
                <v-btn
                        color="white"
                        icon
                        v-bind="attrs"
                        @click="$store.commit('RESET_ALERT')"
                >
                    <v-icon>mdi-close</v-icon>
                </v-btn>
            </template>
        </v-snackbar>
    </v-app>
</template>

<script>
    import {mapState} from 'vuex'

    export default {
        name: 'App',
        computed: {
            ...mapState(['snackbar'])
        },
        data: () => ({

        }),
        methods: {

        }
    };
</script>
