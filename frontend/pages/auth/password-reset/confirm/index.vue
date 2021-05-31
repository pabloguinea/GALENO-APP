<template>
  <div class="">
    <div id="page-title" class="padding-tb-30px gradient-white">
      <div class="container text-center">
        <ol class="breadcrumb opacity-5">
          <li><nuxt-link to="/">Home</nuxt-link></li>
          <li class="active">Login</li>
        </ol>
        <h1 class="font-weight-300">Set a new new_password</h1>
      </div>
    </div>

    <div class="container margin-bottom-100px">
      <!--======= log_in_page =======-->
      <div
        id="log-in"
        class="site-form log-in-form box-shadow border-radius-10"
      >
        <div class="form-output">
          <form v-on:submit.prevent="onSubmit">
            
            <div class="form-group label-floating">
              <label class="control-label">new_password</label>
              <input
                class="form-control"
                placeholder=""
                type="password"
                v-model="form.new_password"
              />
            </div>

            <div class="form-group label-floating">
              <label class="control-label">Confirm your new_password</label>
              <input
                class="form-control"
                placeholder=""
                type="password"
                v-model="form.re_new_password"
              />
            </div>

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
              type="submit"
              class="btn btn-md btn-primary full-width"
              value="Save and Login"
            />

            <div class="or"></div>

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
export default {
  layout: "public",

  transitions: "page",
  head() {
    return {
      title: `${this.title} | Medical Health Services`,
    };
  },
  data() {
    return {
      title: "Log in",
      form:{
        new_password: "amilest7777",
        re_new_password: "amilest7777",
        uid: '',
        token: ''
      }
    };
  },
  mounted(){
    this.form.uid = this.$route.query.uid;
    this.form.token = this.$route.query.token;
  },
  methods: {
    async onSubmit() {
      
      await this.$axios.post("/auth/users/reset_password_confirm/", this.form);

      this.$toast.success(
        "Your new_password was successfully confirmed. Now you can login with your credentials."
      );

      this.$router.push("/auth/login");

    },
  },
};
</script>

<style>
</style>
