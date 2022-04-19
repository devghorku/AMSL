<template>
  <v-container>
    <div class="text-right my-4">
      <v-btn @click="addModal=true" small class="text-none" color="primary">
        Add Employee
      </v-btn>
    </div>

    <v-card class="my-2 pa-3">
      <data-table
          :url="url"
          :tableHeadline="'Manage Employee'"
          :headers="headers"
          class="custom-table-adjust"
          ref="dataTable"
          :otherFilter="{active:active}"
          @updateModal="updateModal"
          is-expand
      >
        <template v-slot:other_filter>
          <v-switch
              @change="getData()"
              v-model="active"
              dense
              inset
              label="Is Active"
              class="mx-4"
          ></v-switch>
        </template>
        <template v-slot:item.status="{ item }">
          <v-switch
              @change="toggleItem(item)"
              v-model="item.active"
              dense
              inset
          ></v-switch>
        </template>
        <template v-slot:expanded-item="{ headers,item  }">
          <td :colspan="headers.length">
            {{item }}
          </td>
        </template>
      </data-table>
    </v-card>
    <v-dialog v-model="addModal" max-width="600px" overlay-opacity="0.9">
      <v-card>
        <v-form @submit.prevent="addItem()" ref="form" class="cus-input">
          <v-card-title class="justify-end">
            <span class="text-h5">Add Employee</span>
            <v-spacer></v-spacer>
            <v-btn @click="addModal=false" small text class="text-none">
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
                      label="Category"
                      outlined
                      dense
                      :items="employeeCategoryList"
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
                      label="Name"
                      outlined
                      dense
                      type="text"
                      :rules="[v=> !!v || 'Name is required']"
                      v-model="form.name"
                  ></v-text-field>
                </v-col>
                <v-col
                    cols="12"
                >
                  <v-text-field
                      label="Employee ID"
                      outlined
                      dense
                      type="text"
                      :rules="[v=> !!v || 'Employee ID is required']"
                      v-model="form.employee_id"
                  ></v-text-field>
                </v-col>
                <v-col
                    cols="12"
                >
                  <v-text-field
                      label="NID/Passport"
                      outlined
                      dense
                      type="text"
                      :rules="[v=> !!v || 'NID/Passport is required']"
                      v-model="form.nid"
                  ></v-text-field>
                </v-col>
                <v-col
                    cols="12"
                >
                  <v-textarea
                      label="Address"
                      outlined
                      dense
                      type="text"
                      :rules="[v=> !!v || 'Address is required']"
                      rows="2"
                      v-model="form.address"
                  ></v-textarea>
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
                          label="Birth Date"
                          outlined
                          dense
                          readonly
                          v-bind="attrs"
                          v-on="on"
                          :rules="[v=> !!v || 'field is required']"
                          v-model="form.birth_date"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                        v-model="form.birth_date"
                        @input="menu2 = false"
                    ></v-date-picker>
                  </v-menu>

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
                      rows="2"
                      hide-details
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
        <v-form @submit.prevent="updateItem()" ref="editForm" class="cus-input">
          <v-card-title class="justify-end">
            <span class="text-h5">Update Employee</span>
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
                      label="Category"
                      outlined
                      dense
                      :items="employeeCategoryList"
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
                      label="Name"
                      outlined
                      dense
                      type="text"
                      :rules="[v=> !!v || 'Name is required']"
                      v-model="editForm.name"
                  ></v-text-field>
                </v-col>
                <v-col
                    cols="12"
                >
                  <v-text-field
                      label="Employee ID"
                      outlined
                      dense
                      type="text"
                      :rules="[v=> !!v || 'Employee ID is required']"
                      v-model="editForm.employee_id"
                  ></v-text-field>
                </v-col>
                <v-col
                    cols="12"
                >
                  <v-text-field
                      label="NID/Passport"
                      outlined
                      dense
                      type="text"
                      :rules="[v=> !!v || 'NID/Passport is required']"
                      v-model="editForm.nid"
                  ></v-text-field>
                </v-col>
                <v-col
                    cols="12"
                >
                  <v-textarea
                      label="Address"
                      outlined
                      dense
                      type="text"
                      :rules="[v=> !!v || 'Address is required']"
                      rows="2"
                      v-model="editForm.address"
                  ></v-textarea>
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
                      rows="2"
                      v-model="editForm.description"
                  ></v-textarea>
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
                          label="Birth Date"
                          outlined
                          dense
                          readonly
                          v-bind="attrs"
                          v-on="on"
                          :rules="[v=> !!v || 'field is required']"
                          v-model="editForm.birth_date"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                        v-model="editForm.date"
                        @input="menu2 = false"
                    ></v-date-picker>
                  </v-menu>
                </v-col>
                <v-col
                    cols="12"
                    class="d-flex"
                >
                  <v-checkbox
                      v-model="editForm.active"
                      label="Active"
                      color="secondary"
                      value="True"
                      class="mr-2"
                  ></v-checkbox>
                  <v-checkbox
                      v-model="editForm.active"
                      label="Not Active"
                      color="secondary"
                      value="False"
                      class="ml-2"
                  ></v-checkbox>
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
      url: 'employee/',
      headers: [
        {text: 'Name', value: 'name'},
        {text: 'Profession', value: 'category.name'},
        {text: 'Employee_ID', value: 'employee_id'},
        // {text: 'NID/Passport', value: 'nid'},
        // {text: 'Address', value: 'address'},
        // {text: 'Birth Date', value: 'birth_date'},
        // {text: 'Description', value: 'description'},
        {text: 'Active', value: 'status'},
        {text: 'Action', value: 'actions', width: '100px', align: 'center', sortable: false},
      ],
      menu2: false,
      active: true,
      form: {employee_id: null, nid: null, birth_date: null},
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
    ...mapGetters(['employeeCategoryList'])
  },
  async mounted() {
    await this.$store.dispatch('getEmployeeCategory')
  },
  methods: {
    getData() {
      this.$nextTick(() => {
        this.$refs.dataTable.getData();
      })

    },
    updateModal(form) {
      this.editForm = JSON.parse(JSON.stringify(form));
      this.editForm.category = form.category.id
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
    async toggleItem(item) {
      try {
        const res = await this.$api.patch(this.url + item.id + '/', {active: item.active});
        await this.$store.dispatch('set_alert', {msg: 'Update Successfully', type: 'success'});
        this.$refs.dataTable.getData();
      } catch (err) {
        this.$globalFunc.errorAlert(err.response)
      }
    },

  }
}
</script>

<style scoped>

</style>