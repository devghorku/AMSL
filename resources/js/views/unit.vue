<template>
    <v-container>

        <v-card class="my-2">
            <div class="text-right d-flex flex-wrap justify-space-between align-center primary pa-3">
                <div class="white--text text-h6 font-weight-bold">
                    All Units
                </div>
                <div class="d-flex flex-wrap justify-space-between align-center">
                    <v-text-field v-model="search"
                                  dense
                                  hide-details
                                  class="mx-2"
                                  style="max-width: 150px;"
                                  label="Search"
                                  dark
                                  solo
                                  @keyup="getSearch"
                    >

                    </v-text-field>
                    <v-btn color="secondary" class="text-none" @click="addModal=true">Add Unit</v-btn>
                </div>
            </div>
            <v-card-text>
                <v-data-table :headers="headers"
                              dense
                              :items="tableData"
                              :loading="loading"
                              :options.sync="options"
                              :server-items-length="total"
                >
                    <template v-slot:item.action="{ item }">
                        <div class="d-flex align-center">
                            <v-btn small color="primary" @click="openEditModal(item)" class="ma-1 text-none">
                                Edit
                            </v-btn>
                            <v-btn small color="error" @click="deleteItem=item,deleteModal=true" class="ma-1 text-none">
                                Delete
                            </v-btn>
                        </div>

                    </template>
                </v-data-table>
            </v-card-text>
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
        </v-dialog>
        <v-dialog v-model="editModal" max-width="600px" overlay-opacity="0.9">
            <v-card>
                <v-form @submit.prevent="updateItem()" ref="editForm">
                    <v-card-title class="justify-end">
                        <span class="text-h5">Update Unit</span>
                        <v-spacer></v-spacer>
                        <v-btn  @click="editModal=false" small text>
                            x
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

        <v-dialog v-model="deleteModal" max-width="400px" overlay-opacity="0.9">
            <v-card>
                <v-card-title class="py-2">
                    <span class="text-h6 error--text font-weight-bold ">Delete Warning</span>
                </v-card-title>
                <v-divider></v-divider>
                <v-card-text class="text-center warning--text pa-7">
                    Are You sure to delete this item? All data related this item will be changed!
                </v-card-text>
                <v-divider></v-divider>
                <v-card-actions class="justify-end" @click="deleteModal=false,deleteItem={}">
                    <v-btn color="primary" class="font-weight-bold text-none" small>
                        Cancel
                    </v-btn>
                    <v-btn color="error"
                           @click="deleteItemConfirm()"
                           small
                           class="font-weight-bold text-none">
                        Delete
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-container>
</template>

<script>

    export default {
        name: "unit",
        watch: {
            options: {
                handler() {
                    this.getData()
                },
                deep: true,
            },
        },
        data() {
            return {
                url: 'admin/unit/',
                form: {},
                editForm: {},
                deleteItem: {},
                addModal: false,
                editModal: false,
                deleteModal: false,
                search: '',
                loading: false,
                total: 0,
                options: {},
                headers: [
                    {text: 'Name', value: 'name'},
                    {text: 'Action', value: 'action', width: '100px', align: 'center',sortable:false},
                ],
                tableData: []
            }
        },

        methods: {
            async getData() {
                try {
                    this.loading = true;
                    const {sortBy, sortDesc, page, itemsPerPage} = this.options;
                    const params = {
                        page: page,
                        search: this.search,
                        per_page: itemsPerPage,
                        ordering: this.$globalFunc.getOrder(sortBy, sortDesc)
                    };
                    const res = await this.$api.get(this.url, {params: params});
                    this.tableData = res.data.results;
                    this.total = res.data.count;
                    this.loading = false;
                } catch (err) {
                    this.loading = false;
                    // await this.$store.dispatch('set_alert', {msg: 'error occur', type: 'error'})
                }
            },
            getSearch: _.debounce(function () {
                this.options.page = 1;
                this.getData()
            }, 400),
            async deleteItemConfirm() {
                try {
                    let res = await this.$api.delete(this.url + this.deleteItem.id + '/');
                    await this.$store.dispatch('set_alert', {msg: res.data.message, type: res.data.type});
                    if (res.type === 'success') {
                        this.deleteItem = {};
                    }
                } catch (err) {
                    await this.$store.dispatch('set_alert', {msg: 'error occur', type: 'error'})
                }
                this.deleteModal=false;
                await this.getData();
            },
            openEditModal(item) {
                this.editForm = JSON.parse(JSON.stringify(item));
                this.editModal = true;
            },
            async addItem() {
                if (this.$refs.form.validate()) {
                    try {
                        const res = await this.$api.post(this.url, this.form);
                        await this.$store.dispatch('set_alert', {msg: 'Created Successfully', type: 'success'});
                        this.$refs.form.reset();
                        this.getData();
                        this.addModal=false;
                    } catch (err) {
                        this.$globalFunc.errorAlert(err.response)
                    }
                }

            },
            async updateItem() {
                if (this.$refs.editForm.validate()) {
                    try {
                        const res = await this.$api.patch(this.url+this.editForm.id+'/', this.editForm);
                        await this.$store.dispatch('set_alert', {msg: 'Update Successfully', type: 'success'});
                        this.$refs.editForm.reset();
                        this.getData();
                        this.editModal=false;
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