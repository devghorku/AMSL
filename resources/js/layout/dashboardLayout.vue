<template>
  <v-app v-cloak>
    <v-navigation-drawer
        v-model="drawer"
        :clipped="true"
        fixed
        app
        color="primary"
        dark
    >
      <!--            <v-list dense>-->
      <!--                <template v-for="(item, i) in items">-->
      <!--                    <v-list-item-->
      <!--                            :key="i"-->
      <!--                            :to="item.link"-->
      <!--                    >-->
      <!--                        <v-list-item-content>-->
      <!--                            <v-list-item-title v-text="item.title"/>-->
      <!--                        </v-list-item-content>-->
      <!--                    </v-list-item>-->
      <!--                    <v-divider :key="'d'+i"></v-divider>-->
      <!--                </template>-->

      <!--            </v-list>-->
      <v-list dense active-class="white--text">
      <v-list-group sub-group active-class="white--text"
      >
        <template v-slot:activator>
          <v-list-item-title>Expense</v-list-item-title>
        </template>

  <v-list-item to="/expense" active-class="white--text"><v-list-item-title>Expense</v-list-item-title>
        </v-list-item>
        <v-divider/>
        <v-list-item to="/expense-category" active-class="white--text"><v-list-item-title>Expense Category</v-list-item-title>
        </v-list-item>
         <v-divider/>
 <v-list-item to="/expense-category" active-class="white--text"><v-list-item-title>Expense Category</v-list-item-title>
        </v-list-item>
         <v-divider/>
         <v-list-item to="/expense-category" active-class="white--text"><v-list-item-title>Expense Category</v-list-item-title>
        </v-list-item>
      </v-list-group>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
        :clipped-left="true"
        fixed
        app
        elevation="1"
    >
      <v-btn color="primary" @click.stop="drawer = !drawer" small tile outlined>
        menu
      </v-btn>

      <v-spacer/>
      <div class="px-2 d-flex align-center">
        <div class="text-sm-h6 primary--text text-center">Store Management Software</div>
      </div>
      <v-spacer/>
      <v-btn small color="primary" tile outlined @click="logout">
        Profile
      </v-btn>
    </v-app-bar>

    <v-main class="lightWhite">
      <router-view/>
    </v-main>
    <!--        <v-footer dark inset app absolute>-->
    <!--            <div>© 2022 <a href="https://www.fiverr.com/hasibarmanku">Devghor</a> , All Rights Reserved</div>-->
    <!--        </v-footer>-->
    <v-snackbar
        :timeout="2500"
        :value="!!snackbar.message"
        right
        top
        :color="snackbar.type"
    >
      {{ snackbar.message }}
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
    items: [
      {title: 'Dashboard', link: '/', icon: 'mdi-grid'},
      {title: 'Expense ', link: '/import', icon: 'mdi-grid'},
      {title: 'Export', link: '/export', icon: 'mdi-grid'},
      {title: 'Product', link: '/product', icon: 'mdi-grid'},
      {title: 'Product Type', link: '/product-type', icon: 'mdi-grid'},
      {title: 'Unit', link: '/unit', icon: 'mdi-grid'},
      {title: 'Report', link: '/report', icon: 'mdi-grid'},
      {title: 'Backup', link: '/backup', icon: 'mdi-grid'},
    ],
    drawer: true,
  }),
  methods: {
    async logout() {
      await this.$store.dispatch('logout');
      this.$router.push('/login')
    }
  }
};
</script>
