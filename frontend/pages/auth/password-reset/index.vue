<template>
  <div class="">
    <div id="page-title" class="padding-tb-30px gradient-white">
      <div class="container text-center">
        <ol class="breadcrumb opacity-5">
          <li><nuxt-link to="/">Home</nuxt-link></li>
          <li class="active">Login</li>
        </ol>
        <h1 class="font-weight-300">Reset your password</h1>
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
                v-model="form.email"
              />
            </div>

            <input
              type="submit"
              class="btn btn-md btn-primary full-width"
              value="Reset"
            />

            <div class="or"></div>

            <p>
              Do you remember your password?
              <nuxt-link to="/auth/login">Sig In!</nuxt-link>
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
      form: {
        email: "amilest7777@gmail.com",
      },
    };
  },
  methods: {
    async onSubmit() {
      await this.$axios.post("/auth/users/reset_password/", this.form);

      this.$toast.success(
        "Your password was successfully resetted. Please check your inbox email, We sent an link to create a new password."
      );

      this.$router.push("/auth/login");
    },
  },
};
</script>

<style>
</style>
