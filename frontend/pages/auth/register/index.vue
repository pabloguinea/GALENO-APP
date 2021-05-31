<template>
  <div class="">
    <div id="page-title" class="padding-tb-30px gradient-white">
      <div class="container text-center">
        <ol class="breadcrumb opacity-5">
          <li><nuxt-link to="/">Home</nuxt-link></li>
          <li class="active">Sing Up</li>
        </ol>
        <h1 class="font-weight-300">Sing Up</h1>
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
              <label class="control-label">Your Name</label>
              <input
                class="form-control"
                placeholder=""
                type="text"
                v-model="form.first_name"
              />
            </div>

            <div class="form-group label-floating is-select">
              <label class="control-label">Your Speciality</label>
              <select class="selectpicker form-control" v-model="form.area">
                <option value="P">Pneumology</option>
                <option value="N">Neurology</option>
                <option value="U">Urology</option>
              </select>
            </div>

            <div class="form-group label-floating">
              <label class="control-label">Your ID Card</label>
              <input
                class="form-control"
                placeholder=""
                type="text"
                v-model="form.card_id"
              />
            </div>
            <div class="form-group label-floating">
              <label class="control-label">Your email</label>
              <input
                class="form-control"
                placeholder=""
                type="email"
                v-model="form.email"
              />
            </div>

            <div class="form-group label-floating">
              <label class="control-label">Password</label>
              <input
                class="form-control"
                placeholder=""
                type="password"
                v-model="form.password"
              />
            </div>
            <div class="form-group label-floating">
              <label class="control-label">Confirm your password</label>
              <input
                class="form-control"
                placeholder=""
                type="password"
                v-model="form.re_password"
              />
            </div>

            <div class="remember">
              <div class="checkbox">
                <label>
                  <input
                    name="optionsCheckboxes"
                    type="checkbox"
                    v-model="form.is_agreements"
                  />
                  I accept the
                  <nuxt-link to="/">Terms and Conditions</nuxt-link> of the
                  website
                </label>
              </div>
            </div>

            <input
              type="submit"
              class="btn btn-md btn-primary full-width"
              value="Complete sign up !"
            />

            <p>
              you have an account? <nuxt-link to="/auth/login"> Sing in !</nuxt-link>
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
        email: "amilest0001@gmail.com",
        first_name: "prueba01",
        re_password: "TT00001*",
        password: "TT00001*",
        area: "P",
        card_id: "12220",
        is_agreements: true,
      },
    };
  },
  methods: {
    async onSubmit() {
      
      let payload = {
        email: this.form.email,
        first_name: this.form.first_name,
        password: this.form.password,
        re_password: this.form.re_password,
        area: this.form.area,
        card_id: this.form.card_id,
        is_agreements: this.form.is_agreements,
      };

      await this.$axios.post("/auth/users/", payload);

      this.$toast.success(
        "Your account was successfully created. Please check your inbox email, We sent a link to activate your account."
      );

      this.$router.push('/auth/login')

    },
  },
};
</script>

<style>
</style>
