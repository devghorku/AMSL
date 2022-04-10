<template>
    <div>
        <div class="header-pane">
            <div class="text-h5 font-weight-bold">{{ tableHeadline }}</div>

        <div class="content-block">
            <div class="d-flex justify-end mb-3">
                <v-spacer></v-spacer>
                <v-text-field
                        v-if="searchField"
                        v-model="search"
                        append-icon="mdi-magnify"
                        label="Search"
                        single-line
                        dense
                        style="max-width:250px"
                        hide-details
                        @keyup="getSearch"
                ></v-text-field>
            </div>
            <v-data-table
                    :headers="headers"
                    :items="tableData"
                    :loading="loading"
                    :options.sync="options"
                    :server-items-length="total"
                    class="elevation-1"
                    :footer-props="{'items-per-page-options': [10, 20, 30, 40, 50]}"
            >
                <template v-for="(slot, name) in $scopedSlots" v-slot:[name]="item">
                    <slot :name="name" v-bind="item"></slot>
                </template>
                <template v-slot:item.actions="{ item }">
                  <div class="d-flex">
                  <v-btn x-small
                            class="mr-2 text-none"
                            @click="$emit('updateModal',item)"
                            color="info"
                  >
                   Edit
                  </v-btn>

                    <v-btn
                            x-small
                            @click="deleteItem(item)"
                            color="error"
                            class="text-none"
                    >
                        Delete
                    </v-btn>
                  </div>
                </template>
            </v-data-table>
            <v-dialog v-model="dialogDelete" max-width="320px">
                <v-card class="pa-3">
                    <v-card-text class="text-h6 delete-modal-title text-center justify-center pa-3 red--text">
                        Are you sure you want to delete this item?
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1"  @click="closeDelete" class="white--text text-none">Cancel</v-btn>
                        <v-btn color="red darken-1"  @click="deleteItemConfirm" class="white--text text-none">OK</v-btn>
                        <v-spacer></v-spacer>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </div>
        </div>
    </div>


</template>

<script>
    export default {
        props: {
            app_name: {
                type: String,
                default: () => ''
            },
            url: {
                type: String,
                default: () => ''
            },
            tableHeadline: {
                type: String,
                default: () => ''
            },
            headers: {
                type: Array,
                default: () => []
            },
            addBtnLink: {
                type: String,
                default: () => ''
            },
            editBtnLink: {
                type: String,
                default: () => ''
            },
            searchField: {
                type: Boolean,
                default: () => true
            },
            addButton: {
                type: Boolean,
                default: () => true
            },
            detailsBtn: {
                type: Boolean,
                default: () => false
            },
            detailsBtnLink: {
                type: String,
                default: () => ''
            },
            exportButton: {
                type: Boolean,
                default: () => false
            },
            importButton: {
                type: Boolean,
                default: () => false
            }

        },
        data: () => ({
            dialogDelete: false,
            deleteItemId: null,
            tableData: [],
            loading: false,
            total: 0,
            search: '',
            options: {},
            excel: null
        }),
        watch: {
            options: {
                handler() {
                    this.getData()
                },
                deep: true,
            },
        },
        computed: {
            // checkAddButtonPerm() {
            //     if (this.app_name) {
            //         return !!this.$globalFunc.isPermit('add_' + this.app_name);
            //     }
            //     return true
            // },
            // checkDeleteButtonPerm() {
            //     if (this.app_name) {
            //         return !!this.$globalFunc.isPermit('delete_' + this.app_name);
            //     }
            //     return true
            // },
            // checkEditButtonPerm() {
            //     if (this.app_name) {
            //
            //         return !!this.$globalFunc.isPermit('change_' + this.app_name);
            //     }
            //     return true
            // },
            // checkDetialsButtonPerm() {
            //     if (this.app_name) {
            //
            //         return !!this.$globalFunc.isPermit('view_' + this.app_name);
            //     }
            //     return true
            // }
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
            deleteItem(item) {
                this.deleteItemId = item.id;
                this.dialogDelete = true
            },
            async deleteItemConfirm() {
                try {
                    let res = await this.$api.delete(this.url + this.deleteItemId + '/');
                    await this.$store.dispatch('set_alert', {msg: res.data.message, type: res.data.type})
                    if (res.type === 'success') {
                        this.deleteItemId = null;
                    }
                } catch (err) {
                    await this.$store.dispatch('set_alert', {msg: 'error occur', type: 'error'})
                }
                this.closeDelete();
                await this.getData();
            },
            closeDelete() {
                this.deleteItemId = null;
                this.dialogDelete = false
            },

        }
    }
</script>

<style scoped>
</style>