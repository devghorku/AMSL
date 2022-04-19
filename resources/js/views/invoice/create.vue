<template>
  <v-container class="invoice mb-8">
    <v-form @submit.prevent="addInvoice"
            ref="form" class="cus-input">
      <v-row class="mt-6">
        <v-col cols="12" sm="6" md="4">
          <v-text-field label="Client Name"
                        outlined
                        dense
                        type="name"
                        :rules="[v=> !!v || 'Client Name is required']"
                        v-model="form.client_name"
          >
          </v-text-field>
          <v-textarea label="Client Address"
                      outlined
                      dense
                      rows="2"
                      v-model="form.client_address"
          >
          </v-textarea>
          <v-text-field label="Client Phone"
                        outlined
                        dense
                        v-model="form.client_phone"
          >
          </v-text-field>
        </v-col>
        <v-col cols="12" sm="6" md="8" class="d-flex flex-column align-end">
          <v-text-field label="Invoice ID"
                        class="pt-2"
                        outlined
                        dense
                        hide-details
                        style="max-width: 200px"
                        :rules="[v=> !!v || 'Invoice ID is required']"
                        v-model="form.invoice_id"
          >
          </v-text-field>
          <v-menu
              v-model="menu1"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field class="pt-2"
                            label="Date"
                            outlined
                            dense
                            v-bind="attrs"
                            v-on="on"
                            hide-details
                            style="max-width: 200px"
                            :rules="[v=> !!v || 'field is required']"
                            v-model="form.invoice_date"
              ></v-text-field>
            </template>
            <v-date-picker
                v-model="form.invoice_date"
                @input="menu1 = false"
            ></v-date-picker>
          </v-menu>

          <v-row class="d-flex flex-row pa-3 justify-end">
            <div class="pr-5"
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
                  <v-text-field class="pt-2"
                                label="From Date"
                                outlined
                                readonly
                                v-bind="attrs"
                                v-on="on"
                                dense
                                hide-details
                                style="max-width: 150px"
                                v-model="form.from_date"
                  ></v-text-field>
                </template>
                <v-date-picker
                    v-model="form.from_date"
                    @input="menu2 = false"
                ></v-date-picker>
              </v-menu>

            </div>
            <div class="pr-lg-5 pr-0"
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
                  <v-text-field class="pt-2"
                                label="To Date"
                                outlined
                                readonly
                                v-bind="attrs"
                                v-on="on"
                                dense
                                hide-details
                                style="max-width: 150px"
                                v-model="form.to_date"
                  ></v-text-field>
                </template>
                <v-date-picker
                    v-model="form.to_date"
                    @input="menu3 = false"
                ></v-date-picker>
              </v-menu>

            </div>
            <div style="max-width: 150px" class="pt-2">
              <v-btn class="info text-none">Last Month</v-btn>
            </div>
          </v-row>
        </v-col>
      </v-row>
      <v-row class="mt-10 ">
        <v-col cols="12">
          <v-data-table
              :headers="headers"
              :items="form.invoices"
              hide-default-footer
          >
            <template v-slot:item.name="{ item,index }">
              <v-text-field outlined
                            dense
                            class="my-2"
                            hide-details
                            :rules="[v=> !!v || 'Item is required']"
                            v-model="form.invoices[index].product_name"
              >
              </v-text-field>
            </template>
            <template v-slot:item.desc="{ item,index }">
              <v-text-field outlined
                            dense
                            class="my-2"
                            hide-details
                            v-model="form.invoices[index].description"
              >
              </v-text-field>
            </template>
            <template v-slot:item.quantity="{ item,index }">
              <v-text-field outlined
                            dense
                            class="my-2"
                            type="number"
                            hide-details
                            :rules="[v=> !!v || 'Item is required']"
                            v-model="form.invoices[index].quantity"
              >
              </v-text-field>
            </template>
            <template v-slot:item.base="{ item,index }">
              <v-text-field outlined
                            dense
                            class="my-2"
                            type="name"
                            hide-details
                            v-model="form.invoices[index].base"
              >
              </v-text-field>
            </template>
            <template v-slot:item.unit_price="{ item,index }">
              <v-text-field outlined
                            dense
                            class="my-2"
                            type="number"
                            hide-details
                            :rules="[v=> !!v || 'Item is required']"
                            v-model="form.invoices[index].unit_price"
              >
              </v-text-field>
            </template>
            <template v-slot:item.actions="{ item,index }">
              <v-btn x-small color="error" class="text-none"
                     v-if="form.invoices.length>1"
                     @click="removeInvoices(index)">Delete
              </v-btn>
            </template>
            <template v-slot:item.total="{ item,index }">
              {{item.quantity*item.unit_price}}
            </template>
          </v-data-table>

        </v-col>
      </v-row>
      <v-row class="justify-end">
        <v-btn color="success" @click="addInvoiceItem" small class="px-5 ma-4"> Add Item</v-btn>
      </v-row>
      <v-row>
        <v-col cols="12" md="6">
          <v-textarea label="Comment"
                      large
                      outlined
                      dense
                      rows="4"
                      hide-details
                      :rules="[v=> !!v || 'field is required']"
                      v-model="form.comment"
          >
          </v-textarea>
        </v-col>
        <v-col cols="12" md="6" class="d-flex flex-column align-end">
          <v-text-field label="Vat"
                        outlined
                        dense
                        type="number"
                        style="max-width: 200px"
                        v-model="form.vat"
          >
          </v-text-field>
          <v-text-field label="Discount"
                        outlined
                        dense
                        type="number"
                        style="max-width: 200px"
                        v-model="form.discount"
          >
          </v-text-field>
          <v-text-field label="Due"
                        outlined
                        dense
                        type="number"
                        style="max-width: 200px"
                        v-model="form.due"
          >
          </v-text-field>
          <div
                        style="max-width: 200px"
          >
          Total: {{invoice_total}}
          </div>
        </v-col>
      </v-row>
      <div class="justify-center text-center">
        <v-btn
                  color="primary"
                  class="text-none font-weight-bold"
                  type="submit"
                  small
                  @click="submit"
              >
                Submit
              </v-btn>
      </div>

    </v-form>

  </v-container>
</template>
<script>
export default {
  name: 'create',
  data() {
    return {
      url: 'invoice/',
      menu1: false,
      menu2: false,
      menu3: false,
      headers: [
        {
          text: 'name',
          align: 'start',
          sortable: false,
          value: 'name',
          width: '200px',
        },
        {text: 'Description', value: 'desc', sortable: false, width: '250px',},
        {text: 'Quantity', value: 'quantity', sortable: false, width: '150px',},
        {text: 'Base', value: 'base', sortable: false, width: '150px',},
        {text: 'Unit Price', value: 'unit_price', sortable: false, width: '150px',},
        {text: 'Total', value: 'total', sortable: false, width: '150px', align: 'right'},
        {text: '', value: 'actions', sortable: false, width: '80px',},
      ],
      form: {
        invoice_id: '',
        invoice_date: new Date().toISOString().substring(0, 10),
        from_date: '',
        to_date: '',
        client_name: '',
        client_address: '',
        client_phone: '',
        vat: 0,
        due: 0,
        discount: 0,
        comment: '',
        invoices: [
          {
            product_name: '',
            description: '',
            quantity: 0,
            base: '',
            unit_price: 1
          }
        ]
      },
    }
  },
  computed:{
    invoice_total(){
      let total=0;
      this.form.invoices.forEach((item)=>{
        total=total+(item.quantity*item.unit_price)
      })
      let sum=total+(total*this.form.vat/100)-this.form.discount
      return sum;
    }
  },
  async mounted() {
    const res2 = await this.$api.get(this.url);
    console.log(res2)
  },
  methods: {
    addInvoiceItem() {
      this.form.invoices.push({
        product_name: '',
        description: '',
        quantity: 0,
        base: '',
        unit_price: 1
      })
    },
    async submit() {
      if (this.$refs.form.validate()) {
        try {
          const res = await this.$api.post(this.url, this.form);
          await this.$store.dispatch('set_alert', {msg: 'Created Successfully', type: 'success'});
          this.$refs.form.reset();
        } catch (err) {
          this.$globalFunc.errorAlert(err.response)
        }
      }

    },
    removeInvoices(idx) {
      if (this.form.invoices.length > 1) {
        this.form.invoices.splice(idx, 1)
      }
    },
  }
}
</script>
<style lang="scss">

</style>