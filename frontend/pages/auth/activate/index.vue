<template>
  <div class="">
    <div id="page-title" class="padding-tb-30px gradient-white">
      <div class="container text-center">
        <ol class="breadcrumb opacity-5">
          <li><nuxt-link to="/">Home</nuxt-link></li>
          <li class="active">Login</li>
        </ol>
        <h1 class="font-weight-300">Activating your account</h1>
      </div>
    </div>

    <div class="container margin-bottom-100px">
      <!--======= log_in_page =======-->
      <div
        id="log-in"
        class="site-form log-in-form box-shadow border-radius-10"
      >
        <div class="form-output">
          <ring-loader class=" d-flex justify-content-center" :loading="loading" :color="color" :size="size"></ring-loader>
          <form v-on:submit.prevent="onSubmit">
           
             <div class="form-group label-floating">
              <label class="control-label">Uid</label>
              <input
                class="form-control"
                placeholder=""
                type="text"
                readonly
                v-model="form.uid"
              />
            </div>
            
             <div class="form-group label-floating">
              <label class="control-label">Token</label>
              <input
                class="form-control"
                placeholder=""
                type="text"
                readonly
                v-model="form.token"
              />
            </div>


            <input
              :disabled="(!form.uid || form.uid === '') || (!form.token || form.token === '') "
              type="submit"
              class="btn btn-md btn-primary full-width"
              value="Activate"
            />

            <div class="or"></div>

            <p>
              Do you have an account?
              <nuxt-link to="/auth/login">Sig In!</nuxt-link>
            </p>

            <p>
              Don't you have an account?
              <nuxt-link to="/auth/register">Register Now!</nuxt-link>
            </p>
          </form>

          
        </div>
      </div>
      <!--======= // log_in_page =======-->
    </div>
  </div>
</template>

<script>
import RingLoader from 'vue-spinner/src/RingLoader.vue'

export default {
  
  layout: "public",

  transitions: "page",
  components: {
    'RingLoader': RingLoader
  },
  head() {
    return {
      title: `${this.title} | Medical Health Services`,
    };
  },
  data() {
    return {
      title: "Log in",
      form: {
        uid: '',
        token: ''
      }
    };
  },
  mounted(){
    this.onSubmit()
  },
  methods: {
    async onSubmit() {
      
      this.form = this.$route.query;

      await this.$axios.post("/auth/users/activation/", this.form);

      this.$toast.success(
        "Your account was successfully activated. Now you can login with your credentials."
      );

      this.$router.push('/auth/login')

    },
  },
};
</script>

<style>
</style>
