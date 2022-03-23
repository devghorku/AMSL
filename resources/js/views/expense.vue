<template>
  <v-container>
    <div class="text-right">
       <v-btn @click="addModal=true" small class="text-none" color="primary">
         Add Expense
       </v-btn>
    </div>

    <v-card class="my-2 pa-3">
      <data-table
          :url="url"
          :tableHeadline="'Manage Expense'"
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
    <v-dialog v-model="addModal" max-width="600px" overlay-opacity="0.9">
      <v-card>
        <v-form @submit.prevent="addItem()" ref="form">
          <v-card-title class="justify-end">
            <span class="text-h5">Add Unit</span>
            <v-spacer></v-spacer>
            <v-btn @click="addModal=false" small text>
              x
            </v-btn>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row dense>
                <v-col
                    cols="12"
                >
                  <v-autocomplete
                      label="Category"
                      outlined
                      dense
                      :items="expenseCategoryList"
                      item-text="name"
                      item-value="id"
                      :rules="[v=> !!v || 'Category is required']"
                      v-model="form.category"
                  ></v-autocomplete>
                </v-col>
                <v-col
                    cols="12"
                >
                  <v-text-field
                      label="Amount"
                      outlined
                      dense
                      type="number"
                      :rules="[v=> !!v || 'Amount is required']"
                      v-model="form.amount"
                  ></v-text-field>
                </v-col>
                <v-col
                    cols="12"
                >
                  <v-menu
                      v-model="menu2"
                      :close-on-content-click="false"
                      :nudge-right="40"
                      transition="scale-transition"
                      offset-y
                      min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                          label="Date"
                          outlined
                          dense
                          readonly
                          v-bind="attrs"
                          v-on="on"
                          :rules="[v=> !!v || 'field is required']"
                          v-model="form.date"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                        v-model="form.date"
                        @input="menu2 = false"
                    ></v-date-picker>
                  </v-menu>

                </v-col>
              </v-row>
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
    <v-dialog v-model="editModal" max-width="600px" overlay-opacity="0.9">
      <v-card>
        <v-form @submit.prevent="updateItem()" ref="editForm">
          <v-card-title class="justify-end">
            <span class="text-h5">Update Unit</span>
            <v-spacer></v-spacer>
            <v-btn @click="editModal=false" small text>
              x
            </v-btn>
          </v-card-title>
          <v-card-text>
            <v-container>
             <v-row dense>
                <v-col
                    cols="12"
                >
                  <v-autocomplete
                      label="Category"
                      outlined
                      dense
                      :items="expenseCategoryList"
                      item-text="name"
                      item-value="id"
                      :rules="[v=> !!v || 'Category is required']"
                      v-model="editForm.category"
                  ></v-autocomplete>
                </v-col>
                <v-col
                    cols="12"
                >
                  <v-text-field
                      label="Amount"
                      outlined
                      dense
                      type="number"
                      :rules="[v=> !!v || 'Amount is required']"
                      v-model="editForm.amount"
                  ></v-text-field>
                </v-col>
                <v-col
                    cols="12"
                >
                  <v-menu
                      v-model="menu2"
                      :close-on-content-click="false"
                      :nudge-right="40"
                      transition="scale-transition"
                      offset-y
                      min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                          label="Date"
                          outlined
                          dense
                          readonly
                          v-bind="attrs"
                          v-on="on"
                          :rules="[v=> !!v || 'field is required']"
                          v-model="editForm.date"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                        v-model="editForm.date"
                        @input="menu2 = false"
                    ></v-date-picker>
                  </v-menu>

                </v-col>
              </v-row>
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

import DataTable from "../component/data-table";
import {mapGetters} from "vuex";

export default {
  name: "unit",
  components: {DataTable},
  data() {
    return {
      url: 'expense/',
      headers: [
        {text: 'Category', value: 'category.name'},
        {text: 'Amount', value: 'amount'},
        {text: 'Date', value: 'date'},
        {text: 'Action', value: 'actions', width: '100px', align: 'center', sortable: false},
      ],
      menu2: false,
      form: {},
      editForm: {},
      deleteItem: {},
      addModal: false,
      editModal: false,

      loading: false,
      total: 0,
      options: {},

    }
  },
  computed: {
    ...mapGetters(['expenseCategoryList'])
  },
  async mounted() {
    await this.$store.dispatch('getExpenseCategory')
  },
  methods: {
    updateModal(form) {
      this.editForm = JSON.parse(JSON.stringify(form));
      this.editForm.category=form.category.id
      this.editModal = true;
    },
    async addItem() {
      if (this.$refs.form.validate()) {
        try {
          const res = await this.$api.post(this.url, this.form);
          await this.$store.dispatch('set_alert', {msg: 'Created Successfully', type: 'success'});
          this.$refs.form.reset();
          this.$refs.dataTable.getData();
          this.addModal = false;
        } catch (err) {
          this.$globalFunc.errorAlert(err.response)
        }
      }

    },
    async updateItem() {
      console.log( this.editForm)
      if (this.$refs.editForm.validate()) {
        try {

          const res = await this.$api.patch(this.url + this.editForm.id + '/', this.editForm);
          await this.$store.dispatch('set_alert', {msg: 'Update Successfully', type: 'success'});
          this.$refs.editForm.reset();
          this.$refs.dataTable.getData();
          this.editModal = false;
        } catch (err) {
          this.$globalFunc.errorAlert(err.response)
        }
      }
    },

  }
}
</script>

<style scoped>

</style>