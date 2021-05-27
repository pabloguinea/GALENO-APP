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
          <form>
            <div class="form-group label-floating">
              <label class="control-label">Your Name</label>
              <input class="form-control" placeholder="" type="email" />
            </div>

            <div class="form-group label-floating is-select">
              <label class="control-label">Your Speciality</label>
              <select class="selectpicker form-control">
                <option value="P">Pneumology</option>
                <option value="N">Neurology</option>
                <option value="U">Urology</option>
              </select>
            </div>

            <div class="form-group label-floating">
              <label class="control-label">Your ID Card</label>
              <input class="form-control" placeholder="" type="text" />
            </div>
            <div class="form-group label-floating">
              <label class="control-label">Your email</label>
              <input class="form-control" placeholder="" type="email" />
            </div>

            <div class="form-group label-floating">
              <label class="control-label">Password</label>
              <input class="form-control" placeholder="" type="password" />
            </div>
            <div class="form-group label-floating">
              <label class="control-label">Confirm your password</label>
              <input class="form-control" placeholder="" type="password" />
            </div>

            <div class="remember">
              <div class="checkbox">
                <label>
                  <input name="optionsCheckboxes" type="checkbox" />
                  I accept the
                  <nuxt-link to="/">Terms and Conditions</nuxt-link> of the
                  website
                </label>
              </div>
            </div>

            <nuxt-link to="/" class="btn btn-md btn-primary full-width"
              >Complete sign up !</nuxt-link
            >

            <p>
              you have an account? <nuxt-link to="/login"> Sing in !</nuxt-link>
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
    };
  },
};
</script>

<style>
</style>
