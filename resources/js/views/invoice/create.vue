<template>
  <v-container>
    <v-form @submit.prevent="addInvoice"
            ref="addForm">
      <v-row class="mt-6">
        <v-col cols="12" md="5">
          <v-col cols="12" md="8">
            <v-text-field label="Client Name"
                          large
                          outlined
                          dense
                          type="name"
                          hide-details
                          :rules="[v=> !!v || 'Client Name is required']"
                          v-model="form.client_name"
            >
            </v-text-field>
          </v-col>
          <v-col cols="12" md="8">
            <v-textarea label="Client Address"
                        large
                        outlined
                        type="text"
                        dense
                        hide-details
                        rows="2"
                        :rules="[v=> !!v || 'Client Address is required']"
                        v-model="form.client_address"
            >
            </v-textarea>
          </v-col>
          <v-col cols="12" md="8">
            <v-text-field label="Client Phone"
                          large
                          outlined
                          type="text"
                          dense
                          hide-details
                          :rules="[v=> !!v || 'Client Address is required']"
                          v-model="form.client_phone"
            >
            </v-text-field>
          </v-col>
        </v-col>
        <v-col cols="12" md="7" class="d-flex flex-column align-end">
          <v-text-field label="Invoice ID"
                        large
                        outlined
                        type="text"
                        dense
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
              <v-text-field
                  label="Date"
                  outlined
                  dense
                  v-bind="attrs"
                  v-on="on"
                  :rules="[v=> !!v || 'field is required']"
                  v-model="form.date"
              ></v-text-field>
            </template>
            <v-date-picker
                v-model="form.date"
                @input="menu1 = false"
            ></v-date-picker>
          </v-menu>

          <v-row class="d-flex flex-row pa-3">
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
                  <v-text-field
                      label="From Date"
                      outlined
                      readonly
                      v-bind="attrs"
                      v-on="on"
                      dense
                      hide-details
                      :rules="[v=> !!v || 'field is required']"
                      v-model="form.from_date"
                  ></v-text-field>
                </template>
                <v-date-picker
                    v-model="form.from_date"
                    @input="menu2 = false"
                ></v-date-picker>
              </v-menu>

            </div>
            <div class="pr-5"
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
                      readonly
                      v-bind="attrs"
                      v-on="on"
                      dense
                      hide-details
                      :rules="[v=> !!v || 'field is required']"
                      v-model="form.to_date"
                  ></v-text-field>
                </template>
                <v-date-picker
                    v-model="form.to_date"
                    @input="menu3 = false"
                ></v-date-picker>
              </v-menu>

            </div>
            <v-spacer></v-spacer>
            <div>
              <v-btn class="info">Last Month</v-btn>
            </div>
          </v-row>
        </v-col>
      </v-row>
      <v-row class="mt-10 ">
        <v-col cols="12">
          <v-data-table
              :headers="headers"
              :items="form.invoices"
          >
            <template v-slot:item.name="{ item,index }">
              <v-text-field large
                            outline
                            dense
                            class="my-2"
                            :rules="[v=> !!v || 'Item is required']"
                            v-model="form.invoices[index].product_name"
              >
              </v-text-field>
            </template>
            <template v-slot:item.desc="{ item,index }">
              <v-text-field label="Item"
                            large
                            outlined
                            dense
                            class="my-2"
                            type="name"
                            :rules="[v=> !!v || 'Item is required']"
                            v-model="form.invoices[index].product_name"
              >
              </v-text-field>
            </template>
            <template v-slot:item.quantity="{ item,index }">
              <v-text-field label="Item"
                            large
                            outlined
                            dense
                            class="my-2"
                            type="name"
                            :rules="[v=> !!v || 'Item is required']"
                            v-model="form.invoices[index].product_name"
              >
              </v-text-field>
            </template>
            <template v-slot:item.base="{ item,index }">
              <v-text-field label="Item"
                            large
                            outlined
                            dense
                            class="my-2"
                            type="name"
                            :rules="[v=> !!v || 'Item is required']"
                            v-model="form.invoices[index].product_name"
              >
              </v-text-field>
            </template>
            <template v-slot:item.base="{ item,index }">
              <v-text-field label="Item"
                            large
                            outlined
                            dense
                            class="my-2"
                            type="name"
                            :rules="[v=> !!v || 'Item is required']"
                            v-model="form.invoices[index].product_name"
              >
              </v-text-field>
            </template>
            <template v-slot:item.unit_price="{ item,index }">
              <v-text-field

                            outlined
                            dense
                            class="my-2"
                            type="name"
                            :rules="[v=> !!v || 'Item is required']"
                            v-model="form.invoices[index].product_name"
              >
              </v-text-field>
            </template>
            <template v-slot:item.actions="{ item,index }">
              <v-btn x-small color="error" class="text-none"
                     v-if="form.invoices.length>1"
                     @click="removeInvoices(index)">Delete</v-btn>
            </template>
          </v-data-table>

        </v-col>
      </v-row>
      <v-row class="justify-center">
        <v-col cols="12" md="9">
          <v-btn color="success" block @click="addInvoiceItem"> Add Item</v-btn>
        </v-col>
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
        <v-col cols="12" md="6" class="d-flex flex-column">
          <v-text-field label="Vat"
                        large
                        outlined
                        dense
                        type="number"
                        :rules="[v=> !!v || 'field is required']"
                        v-model="form.vat"
          >
          </v-text-field>
          <v-text-field label="Discount"
                        large
                        outlined
                        dense
                        type="number"
                        v-model="form.discount"
          >
          </v-text-field>
          <v-text-field label="Due"
                        large
                        outlined
                        dense
                        type="text"
                        :rules="[v=> !!v || 'field is required']"
                        v-model="form.due"
          >
          </v-text-field>
          <v-text-field label="Total"
                        large
                        outlined
                        dense
                        readonly
          >
          </v-text-field>
        </v-col>
      </v-row>
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
        },
        {text: 'Description', value: 'desc', sortable: false},
        {text: 'Quantity', value: 'quantity', sortable: false},
        {text: 'Base', value: 'base', sortable: false},
        {text: 'Unit Price', value: 'unit_price', sortable: false},
        {text: 'Total', value: 'total', sortable: false},
        {text: '', value: 'actions', sortable: false},
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
  async mounted() {
    const res2 = await this.$api.get(this.url);
    console.log(res2)
  },
  methods: {
    addInvoiceItem(){
      this.form.invoices.push({
            product_name: '',
            description: '',
            quantity: 0,
            base: '',
            unit_price: 1
          })
    },
    removeInvoices(idx){
      if(this.form.invoices.length>1){
        this.form.invoices.splice(idx,1)
      }
    },
    async submit() {
      const form = {
        invoice_id: '#feb11321',
        invoice_date: new Date().toISOString().substring(0, 10),
        from_date: null,
        to_date: null,
        client_name: 'hasib',
        client_address: 'asdasdasdsadsd',
        client_phone: '',
        vat: 0,
        due: 0,
        discount: 0,
        comment: 'sdadsad',
        invoices: [
          {
            product_name: 'a',
            description: 'asdasdsad',
            quantity: 1,
            base: 'hr',
            unit_price: 10
          },
          {
            product_name: 'b',
            description: 'asdasdsad sadsa',
            quantity: 2,
            base: 'hr',
            unit_price: 10
          }
        ]
      };
      const res = await this.$api.post(this.url, form);
      console.log(res)

    }
  }
}
</script>