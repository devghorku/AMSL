<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="4">
        <v-card class="my-2">
        <v-form @submit.prevent="addItem()" ref="form">
          <v-card-title class="justify-end">
            <span class="text-h6 font-weight-bold">Add Income Category</span>
            <v-spacer></v-spacer>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>

                <v-col
                    cols="12"
                >
                  <v-text-field
                      label="Name"
                      outlined
                      dense
                      :rules="[v=> !!v || 'Name is required']"
                      v-model="form.name"
                  ></v-text-field>
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
      </v-col>
      <v-col cols="12" md="8">
        <v-card class="my-2 pa-3">
      <data-table
          :url="url"
          :tableHeadline="'Manage Income'"
          :headers="headers"
          addBtnLink="addCountry"
          editBtnLink="editCountry"
          class="custom-table-adjust_top mx-5"
          ref="dataTable"
          app_name="country"
          @updateModal="updateModal"
      >
      </data-table>
    </v-card>
      </v-col>
    </v-row>
    <v-dialog v-model="editModal" max-width="600px" overlay-opacity="0.9">
      <v-card>
        <v-form @submit.prevent="updateItem()" ref="editForm">
          <v-card-title class="justify-end">
            <span class="text-h5">Update Income Category</span>
            <v-spacer></v-spacer>
            <v-btn @click="editModal=false" small text class="text-none">
              Close
            </v-btn>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>

                <v-col
                    cols="12"
                >
                  <v-text-field
                      label="Name"
                      outlined
                      dense
                      :rules="[v=> !!v || 'Name is required']"
                      v-model="editForm.name"
                  ></v-text-field>
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

export default {
  name: "unit",
  components: {DataTable},
  data() {
    return {
      url: 'income-category/',
      headers: [
        {text: 'Name', value: 'name'},
        {text: 'Action', value: 'actions', width: '100px', align: 'center', sortable: false},
      ],

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

  methods: {
    updateModal(form) {
      this.editForm = JSON.parse(JSON.stringify(form));
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