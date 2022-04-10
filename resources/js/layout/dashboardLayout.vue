<template>
  <v-app v-cloak>
    <v-navigation-drawer
        v-model="drawer"
        :clipped="true"
        fixed
        app
        color="sidebarBg"
        dark
        class="own-sidebar"
    >
      <v-list dense>
        <template v-for="(item,idx) in items"
        >
          <v-list-item v-if="!(item.items && item.items.length>0)"
                       :key="idx"
                       active-class="sideActive primary--text"
                       :to="item.link">
            <v-list-item-content>
              <v-list-item-title v-text="item.title">
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-group
              v-else
              no-action
              active-class="white--text"
              :key="idx"
          >
            <template v-slot:activator>
              <v-list-item-content>
                <v-list-item-title v-text="item.title"></v-list-item-title>
              </v-list-item-content>
            </template>
            <v-divider></v-divider>
            <v-list-item
                v-for="child in item.items"
                :key="child.title"
                :to="child.link"
                active-class="sideActive primary--text"
            >
              <v-list-item-content>
                <v-list-item-title v-text="child.title"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
          <v-divider :key="'d'+idx"></v-divider>
        </template>

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

      {
        title: 'Expense ', link: '', items: [
          {title: 'Expense', link: '/expense'},
          {title: 'Expense Category', link: '/expense-category'}
        ]
      },
      {
        title: 'Income ', link: '', items: [
          {title: 'Income', link: '/income'},
          {title: 'Income Category', link: '/income-category'}
        ]
      },
      {
        title: 'Employee ', link: '', items: [
          {title: 'Employee', link: '/employee'},
          {title: 'Employee Category', link: '/employee-category'}
        ]
      },
      {title: 'Payroll ', link: '/payroll'},
      {
        title: 'Invoice ', link: '', items: [
          {title: 'Invoice Create', link: '/invoice'},
          {title: 'Invoice List', link: '/invoice-list'}
        ]
      },

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
<style scoped lang="scss">

.own-sidebar {
  .v-list-item--active {
    .v-list-item__content {
      .v-list-item__title {
        font-weight: bold;
      }
    }

    &::before {
      display: none !important;
    }
  }

  .v-list-group__items {
    .v-list-item {
      color: gray;
    }
  }

  .v-list-group--active {
    background: var(--v-sideActive-base);

  }

  .v-list-group__items {
    .v-list-item {
      padding-left: 40px !important;
    }
  }
}

</style>
