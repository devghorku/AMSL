<template>
  <v-app v-cloak>
    <v-navigation-drawer
        v-model="drawer"
        :clipped="true"
        fixed
        app
        color="#2D3744"
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
      <v-list dense>
      <v-list-group
        v-for="item in items"
        :key="item.title"
        no-action
        active-class="list_group"
      >
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" style="font-size: 16px;"></v-list-item-title>
          </v-list-item-content>
        </template>
          <v-divider></v-divider>
        <v-list-item
          v-for="child in item.items"
          :key="child.title"
          :to="child.link"
          active-class="list_item"
        >
          <v-list-item-content>
            <v-list-item-title v-text="child.title" ></v-list-item-title>
          </v-list-item-content>
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

      {title: 'Expense ', link: '',items:[
          {title:'Expense', link:'/expense'},
          {title:'Expense Category', link:'/expense-category'}
        ]},
      {title: 'Income ', link: '',items:[
          {title:'Income', link:'/income'},
          {title:'Income Category', link:'/income-category'}
        ]},
      {title: 'Employee ', link: '',items:[
          {title:'Employee', link:'/employee'},
          {title:'Employee Category', link:'/employee-category'}
        ]},
      {title: 'Payroll ', link: '',items:[
          {title:'Payroll', link:'/payroll'},
        ]},
      {title: 'Invoice ', link: '',items:[
          {title:'Invoice', link:'/invoice'},
          {title:'Invoice Items', link:'/invoice-items'}
        ]},

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

.v-list-group--active{
  background: #171717;
  .v-list-item--active {
    .v-list-item__content {
      .v-list-item__title {
        font-weight: bold;

        color: white !important;
         background: #171717;
      }
    }
  }

    .v-list-group__items {
      .v-list-item {
        background: #171717;
        color: gray;
      }
      .v-list-item--active {
        background: #171717;
        color: white;
        &::before{
          display: none !important;
        }
      }

    }

}
.list_group{
  font-weight: bold;
  background: #171717;
  v-list-group__items{
    background: #171717;
  }
}
.list_item{
  font-weight: bold !important;
  font-size:20px !important;
  color:#171717;
.v-list-item__content{
   .v-list-item__title{
    font-weight: bold;
     color: white;
  }
}
}

.v-list-group__items{
  .v-list-item {
    padding-left: 40px !important;
  }
}
</style>
