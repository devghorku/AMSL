<template>
  <v-container>
    <div class="text-right my-4">
      <v-btn small class="text-none" color="primary" to="/invoice">
        Create Invoice
      </v-btn>
    </div>
    <v-card class="my-2 pa-3">
      <data-table
          :url="url"
          :tableHeadline="'Invoice List'"
          :headers="headers"
          addBtnLink="addCountry"
          editBtnLink="editCountry"
          class="custom-table-adjust"
          ref="dataTable"
          app_name="country"
          is-expand
          :other-filter="{invoice_date:invoice_date}"
      >
        <template v-slot:other_filter>
         <v-menu
              v-model="menu1"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field class="mx-4"
                            label="Date"
                            outlined
                            dense
                            v-bind="attrs"
                            v-on="on"
                            hide-details
                            style="max-width: 200px"
                            v-model="invoice_date"
                            clearable
                            @keyup="getData()"
                            @input="getData()"
              ></v-text-field>
            </template>
            <v-date-picker
                v-model="invoice_date"
                @input="menu1 = false,getData()"
            ></v-date-picker>
          </v-menu>
        </template>
         <template v-slot:item.invoice_date="{ item }">
           {{item.invoice_date | moment("DD MMMM YYYY") }}
         </template>
        <template v-slot:expanded-item="{ headers,item  }">
          <td :colspan="headers.length">
            <div class="pa-5">
              <v-data-table :items="item.invoice" :headers="headersItem" hide-default-footer class="info--text">
                  <template v-slot:item.actions="{ item }">
            <div class="d-flex">
              <v-btn x-small
                     class="mr-2 text-none"
                     @click="$emit('updateModal',item)"
                     color="info"
              >
                Edit
              </v-btn>

              <v-btn
                  x-small
                  @click="deleteItem(item)"
                  color="error"
                  class="text-none"
              >
                Delete
              </v-btn>
            </div>
          </template>
              </v-data-table>
            </div>

          </td>
        </template>
      </data-table>
    </v-card>
<!--    <v-dialog v-model="editModal" max-width="600px" overlay-opacity="0.9">-->
<!--      <v-card>-->
<!--        <v-form @submit.prevent="updateItem()" ref="editForm">-->
<!--          <v-card-title class="justify-end">-->
<!--            <span class="text-h5">Update Employee</span>-->
<!--            <v-spacer></v-spacer>-->
<!--            <v-btn @click="editModal=false" small text class="text-none">-->
<!--              Close-->
<!--            </v-btn>-->
<!--          </v-card-title>-->
<!--          <v-card-text>-->
<!--            <v-container>-->
<!--              <v-btn-->
<!--                  color="primary"-->
<!--                  class="text-none font-weight-bold"-->
<!--                  type="submit"-->
<!--                  small-->
<!--              >-->
<!--                Submit-->
<!--              </v-btn>-->
<!--            </v-container>-->
<!--          </v-card-text>-->
<!--        </v-form>-->
<!--      </v-card>-->
<!--    </v-dialog>-->


  </v-container>
</template>

<script>

import DataTable from "../../component/data-table";
import {mapGetters} from "vuex";

export default {
  name: "list",
  components: {DataTable},
  data() {
    return {
      url: 'invoice/',
      invoice_date:'',
      menu1:false,
      headers: [
        {text: 'Invoice ID', value: 'invoice_id'},
        {text: 'Date', value: 'invoice_date'},
        {text: 'From Date', value: 'from_date'},
        {text: 'To Date', value: 'from_date'},
        {text: 'Client Name', value: 'client_name'},
        {text: 'Client Address', value: 'client_address'},
        {text: 'Vat', value: 'vat'},
        {text: 'Due', value: 'due'},
        {text: 'Comment', value: 'comment'},
        {text: 'Action', value: 'actions', width: '100px', align: 'center', sortable: false},
      ],
      headersItem: [
        {text: 'Name', value: 'product_name'},
        {text: 'Description', value: 'description'},
        {text: 'Quantity', value: 'quantity'},
        {text: 'Base', value: 'base'},
        {text: 'Unit Price', value: 'unit_price'},
        {text: 'Total', value: 'total'},
        {text: 'Action', value: 'actions', width: '100px', align: 'center', sortable: false},
      ],

      form: {},

      loading: false,
      total: 0,
      options: {},

    }
  },
  methods:{
    getData() {
      this.$nextTick(() => {
        this.$refs.dataTable.getData();
      })

    },
  }


}
</script>

<style scoped>

</style>