<template>
  <v-container>
    <div class="text-right my-4">
       <v-btn @click="addModal=true" small class="text-none" color="primary">
         Add Payroll
       </v-btn>
    </div>

    <v-card class="my-2 pa-5">
      <data-table
          :url="url"
          :tableHeadline="'Manage Payroll'"
          :headers="headers"
          class="custom-table-adjust"
          ref="dataTable"
          app_name="payroll"
          @updateModal="updateModal"
      >
      </data-table>
    </v-card>
    <v-dialog v-model="addModal" max-width="600px" overlay-opacity="0.9">
      <v-card>
        <v-form @submit.prevent="addItem()" ref="form">
          <v-card-title class="justify-end">
            <span class="text-h5">Add Payroll</span>
            <v-spacer></v-spacer>
            <v-btn @click="addModal=false" small text class="text-none" >
              Close
            </v-btn>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row dense>
                <v-col
                    cols="12"
                >
                  <v-autocomplete
                      label="Employee"
                      outlined
                      dense
                      :items="employeeList"
                      item-text="name"
                      item-value="id"
                      :rules="[v=> !!v || 'Employee is required']"
                      v-model="form.employee"
                  ></v-autocomplete>
                </v-col>
                <v-col
                    cols="12"
                >
                  <v-menu
                      v-model="menu1"
                      :close-on-content-click="false"
                      :nudge-right="40"
                      transition="scale-transition"
                      offset-y
                      min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                          label="Pay Date"
                          outlined
                          dense
                          readonly
                          v-bind="attrs"
                          v-on="on"
                          :rules="[v=> !!v || 'field is required']"
                          v-model="form.pay_date"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                        v-model="form.pay_date"
                        @input="menu1 = false"
                    ></v-date-picker>
                  </v-menu>

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
                          label="From Date"
                          outlined
                          dense
                          readonly
                          v-bind="attrs"
                          v-on="on"
                          :rules="[v=> !!v || 'field is required']"
                          v-model="form.from_date"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                        v-model="form.from_date"
                        @input="menu2 = false"
                    ></v-date-picker>
                  </v-menu>

                </v-col>
                <v-col
                    cols="12"
                >
                  <v-menu
                      v-model="menu3"
                      :close-on-content-click="false"
                      :nudge-right="40"
                      transition="scale-transition"
                      offset-y
                      min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                          label="To Date"
                          outlined
                          dense
                          readonly
                          v-bind="attrs"
                          v-on="on"
                          :rules="[v=> !!v || 'field is required']"
                          v-model="form.to_date"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                        v-model="form.to_date"
                        @input="menu3 = false"
                    ></v-date-picker>
                  </v-menu>

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
                  <v-textarea
                      label="Description"
                      outlined
                      dense
                      type="text"
                      :rules="[v=> !!v || 'Description is required']"
                      v-model="form.description"
                  ></v-textarea>
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
            <span class="text-h5">Update Income</span>
            <v-spacer></v-spacer>
            <v-btn @click="editModal=false" small text class="text-none">
              Close
            </v-btn>
          </v-card-title>
          <v-card-text>
            <v-container>
             <v-row dense>
                <v-col
                    cols="12"
                >
                  <v-autocomplete
                      label="Employee"
                      outlined
                      dense
                      :items="employeeList"
                      item-text="name"
                      item-value="id"
                      :rules="[v=> !!v || 'Employee is required']"
                      v-model="editForm.employee"
                  ></v-autocomplete>
                </v-col>
               <v-col
                    cols="12"
                >
                  <v-menu
                      v-model="menu1"
                      :close-on-content-click="false"
                      :nudge-right="40"
                      transition="scale-transition"
                      offset-y
                      min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                          label="Pay Date"
                          outlined
                          dense
                          readonly
                          v-bind="attrs"
                          v-on="on"
                          :rules="[v=> !!v || 'field is required']"
                          v-model="editForm.pay_date"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                        v-model="editForm.pay_date"
                        @input="menu1 = false"
                    ></v-date-picker>
                  </v-menu>

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
                          label="From Date"
                          outlined
                          dense
                          readonly
                          v-bind="attrs"
                          v-on="on"
                          :rules="[v=> !!v || 'field is required']"
                          v-model="editForm.from_date"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                        v-model="editForm.from_date"
                        @input="menu2 = false"
                    ></v-date-picker>
                  </v-menu>

                </v-col>
                <v-col
                    cols="12"
                >
                  <v-menu
                      v-model="menu3"
                      :close-on-content-click="false"
                      :nudge-right="40"
                      transition="scale-transition"
                      offset-y
                      min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                          label="To Date"
                          outlined
                          dense
                          readonly
                          v-bind="attrs"
                          v-on="on"
                          :rules="[v=> !!v || 'field is required']"
                          v-model="editForm.to_date"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                        v-model="editForm.to_date"
                        @input="menu3 = false"
                    ></v-date-picker>
                  </v-menu>

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
                  <v-textarea
                      label="Description"
                      outlined
                      dense
                      type="text"
                      :rules="[v=> !!v || 'Description is required']"
                      v-model="editForm.description"
                  ></v-textarea>
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
  name: "payroll",
  components: {DataTable},
  data() {
    return {
      url: 'payroll/',
      headers: [
        {text: 'Employee', value: 'employee.name'},
        {text: 'Pay Date', value: 'pay_date'},
        {text: 'From Date', value: 'from_date'},
        {text: 'To Date', value: 'to_date'},
        {text: 'Amount', value: 'amount'},
        {text: 'Description', value: 'description'},
        {text: 'Action', value: 'actions', width: '100px', align: 'center', sortable: false},
      ],
      menu1: false,
      menu2: false,
      menu3: false,
      form: {pay_date:null, from_date:null, to_date:null},
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
    ...mapGetters(['employeeList'])
  },
  async mounted() {
    await this.$store.dispatch('getEmployees')
  },
  methods: {
    updateModal(form) {
      this.editForm = JSON.parse(JSON.stringify(form));
      this.editForm.employee=form.employee.id
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