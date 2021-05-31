<template>
  <div class="">
    <div id="page-title" class="padding-tb-30px gradient-white">
      <div class="container text-center">
        <ol class="breadcrumb opacity-5">
          <li><nuxt-link to="/">Home</nuxt-link></li>
          <li class="active">Login</li>
        </ol>
        <h1 class="font-weight-300">Login</h1>
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
              <label class="control-label">Email</label>
              <input
                class="form-control"
                placeholder=""
                type="email"
                v-model="email"
              />
            </div>
            <div class="form-group label-floating">
              <label class="control-label">Password</label>
              <input
                class="form-control"
                placeholder=""
                type="password"
                v-model="password"
              />
            </div>

            <div class="remember">
              <!--
              <div class="checkbox">
                <label>
                  <input name="optionsCheckboxes" type="checkbox" />
                  Remember Me
                </label>
              </div>
              -->
              <nuxt-link to="/auth/password-reset" class="forgot"
                >Forgot my Password</nuxt-link
              >
            </div>

            <input
              type="submit"
              class="btn btn-md btn-primary full-width"
              value="Login"
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
import { mapState } from "vuex";
export default {
  layout: "public",
  middleware: "public",
  transitions: "page",
  head() {
    return {
      title: `${this.title} | Medical Health Services`,
    };
  },
  data() {
    return {
      title: "Log in",
      email: "amilest7777@gmail.com",
      password: "amilest7777",
    };
  },
  computed: {
    ...mapState({
      authenticated: (state) => state.auth.authenticated,
    }),
  },
  methods: {
    async onSubmit() {
      await this.$store.dispatch("auth/login", {
        email: this.email,
        password: this.password,
      });
    },
  },
  watch: {
    authenticated(value) {
      debugger;
      if(value){
        this.$router.push("/dashboard");
      }
    },
  },
};
</script>

<style>
</style>
