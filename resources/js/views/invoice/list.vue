<template>
  <v-container>

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
          @updateModal="updateModal"
      >
      </data-table>
    </v-card>
    <v-dialog v-model="editModal" max-width="600px" overlay-opacity="0.9">
      <v-card>
        <v-form @submit.prevent="updateItem()" ref="editForm">
          <v-card-title class="justify-end">
            <span class="text-h5">Update Employee</span>
            <v-spacer></v-spacer>
            <v-btn @click="editModal=false" small text class="text-none">
              Close
            </v-btn>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-btn
                  color="primary"
                  class="text-none font-weight-bold"
                  type="submit"
                  small
              >
                Submit
              </v-btn>
            </v-container>
          </v-card-text>
        </v-form>
      </v-card>
    </v-dialog>


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
      url: 'invoice-list/',
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

      form: {},

      loading: false,
      total: 0,
      options: {},

    }
  },

}
</script>

<style scoped>

</style>