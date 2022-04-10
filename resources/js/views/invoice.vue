<template>
  <v-container>
    <v-form @submit.prevent="addInvoice()" ref="addForm">
      <v-row class="mt-6">
        <v-col cols="12" md="6">
          <v-text-field label="Invoice ID"
                        large
                        outlined
                        :rules="[v=> !!v || 'Invoice ID is required']"
                        v-model="form.invoice_id"
          >
          </v-text-field>
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field label="Date"
                        large
                        outlined
                        :rules="[v=> !!v || 'Date is required']"
                        v-model="form.date"
          >
          </v-text-field>
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field label="From Date"
                        large
                        outlined
                        :rules="[v=> !!v || 'From Date is required']"
                        v-model="form.from_date"
          >
          </v-text-field>
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field label="To Date"
                        large
                        outlined
                        :rules="[v=> !!v || 'To Date is required']"
                        v-model="form.to_date"
          >
          </v-text-field>
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field label="To Date"
                        large
                        outlined
                        :rules="[v=> !!v || 'To Date is required']"
                        v-model="form.to_date"
          >
          </v-text-field>
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field label="To Date"
                        large
                        outlined
                        :rules="[v=> !!v || 'To Date is required']"
                        v-model="form.to_date"
          >
          </v-text-field>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>
<script>
export default {
  name: 'invoice',
  data() {
    return {
      form: {},
    }
  }
}
</script>