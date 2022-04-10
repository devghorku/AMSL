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
        <v-col cols="12" md="7" class="justify-end">
          <v-col cols="12">
            <v-text-field label="Invoice ID"
                          large
                          outlined
                          type="text"
                          dense
                          hide-details
                          :rules="[v=> !!v || 'Invoice ID is required']"
                          v-model="form.invoice_id"
            >
            </v-text-field>
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
                    label="Date"
                    outlined
                    dense
                    hide-details
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

          </v-col>
          <v-col cols="12">
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

        </v-col>
      </v-row>
      <v-row class="mt-10 px-3 ">
        <v-col cols="12" md="2">
          <v-text-field label="Item"
                        large
                        outlined
                        dense
                        type="name"
                        :rules="[v=> !!v || 'Item is required']"
                        v-model="form.product_name"
          >
          </v-text-field>
        </v-col>
        <v-col cols="12" md="2">
          <v-text-field label="Description"
                        large
                        outlined
                        dense
                        type="text"
                        :rules="[v=> !!v || 'Product Description is required']"
                        v-model="form.description"
          >
          </v-text-field>
        </v-col>
        <v-col cols="12" md="2">
          <v-text-field label="Quantity"
                        large
                        outlined
                        dense
                        type="text"
                        :rules="[v=> !!v || 'Product Quantity is required']"
                        v-model="form.quantity"
          >
          </v-text-field>
        </v-col>
        <v-col cols="12" md="1">
          <v-text-field label="Base"
                        large
                        outlined
                        dense
                        type="text"
                        :rules="[v=> !!v || 'field is required']"
                        v-model="form.base"
          >
          </v-text-field>
        </v-col>
        <v-col cols="12" md="2">
          <v-text-field label="Unit Price"
                        large
                        outlined
                        dense
                        type="text"
                        :rules="[v=> !!v || 'field is required']"
                        v-model="form.unit_price"
          >
          </v-text-field>
        </v-col>
        <v-col cols="12" md="2">
          <v-text-field label="SubTotal"
                        large
                        dense
                        readonly

          >
          </v-text-field>
        </v-col>
        <v-col cols="12" md="1">
          <v-btn text>X</v-btn>
        </v-col>
      </v-row>
      <v-row class="justify-center">
        <v-col cols="12" md="9">
          <v-btn color="success" block>Add Item</v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="6">
          <v-textarea label="Comment"
                      large
                      outlined
                      dense
                      type="text"
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
                        type="text"
                        :rules="[v=> !!v || 'field is required']"
                        v-model="form.vat"
          >
          </v-text-field>
          <v-text-field label="Discount"
                        large
                        outlined
                        dense
                        type="text"
                        :rules="[v=> !!v || 'field is required']"
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
    <v-btn @click="submit">submit</v-btn>
  </v-container>
</template>
<script>
export default {
  name: 'create',
  data() {
    return {
      url:'invoice/',
      menu1: false,
      menu2: false,
      menu3: false,
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
        invoice_set: [
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
  async mounted(){
    const res2 = await this.$api.get(this.url);
    console.log(res2)
  },
  methods:{
    async submit(){
      const  form = {
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