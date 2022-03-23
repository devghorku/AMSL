<template>
  <div>
    <v-container style="min-height: 90vh" class="d-flex">
      <v-card max-width="500" class="ma-auto pa-12" color="grey darken-2" elevation="10">
        <v-card-title class="justify-center text-h5 primary--text">
          Login
        </v-card-title>
        <v-card-text>
          <v-form @submit.prevent="handleSubmit" ref="form">
            <v-row>
              <v-col cols="12">
                <label class="text-h6 white--text">Username</label>
                <v-text-field
                              v-model="form.username"
                              outlined
                              type="email"
                              autocomplete="off"
                              class="white--text"
                              :rules="[v=> !!v || 'Username is required']"
                              dense>

                </v-text-field>
              </v-col>
              <v-col cols="12">
                 <label class="text-h6 white--text">Password</label>
                <v-text-field v-model="form.password"
                              outlined
                              autocomplete="off"
                              :rules="[v=> !!v || 'Password is required']"
                              type="password"
                              dense>

                </v-text-field>
              </v-col>
              <v-col cols="12" class="text-center">
                <v-btn type="submit" color="primary" class="black--text font-weight-bold px-12">Login</v-btn>
              </v-col>
            </v-row>
          </v-form>
        </v-card-text>

      </v-card>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "login",
  layout:'auth',
  data(){
    return{
      form:{}
    }
  },
  methods:{
    async handleSubmit(){
      if(this.$refs.form.validate()){
        try {
         await this.$store.dispatch('login', this.form);
          this.$router.push('/')
        }catch (e) {
          this.$store.dispatch('set_alert', {msg: 'login error', type: 'error'})
        }
      }
    }
  }
}
</script>

<style scoped>

</style>