<template>
  <div>
    <header class="background-white box-shadow fixed-top z-index-99">
      <nav class="container-fluid header-in">
        <div class="row">
          <div class="col-xl-2 col-lg-2 d-flex " style="max-height:80px;align-items:center;">
            <nuxt-link to="/dashboard" class="d-inline-block margin-tb-15px" 
              ><img class="img-fluid"
                :src="require('~/assets/img/logo-1.png')"
                style="max-height:80px;"
                alt=""
            /></nuxt-link>
            <nuxt-link
              to="/"
              class="mobile-toggle padding-13px background-main-color"
              ><i class="fas fa-bars"></i
            ></nuxt-link>
          </div>
          <div class="col-xl-6 col-lg-8 position-inherit">
            <ul
              id="menu-main"
              class="nav-menu float-lg-right link-padding-tb-20px"
            >
              <br />
              <li class="has-dropdown">
                <nuxt-link to="/" target="_blank">Patologies</nuxt-link>
                <ul class="sub-menu">
                  <li><nuxt-link to="/" target="_blank">Renal Insufficiency</nuxt-link></li>
                  <li><nuxt-link to="/" target="_blank">Respiratory Diseases</nuxt-link></li>
                  <li><nuxt-link to="/" target="_blank">Alzheimer</nuxt-link></li>
                  <li><nuxt-link to="/" target="_blank">Parkinson</nuxt-link></li>
                </ul>
              </li>
              <li class="has-dropdown">
                <nuxt-link to="/" target="_blank">Technology</nuxt-link>
                <ul class="sub-menu">
                  <li><nuxt-link to="/" target="_blank">SW Architecture</nuxt-link></li>
                  <li><nuxt-link to="/" target="_blank">Artificial Intelligence</nuxt-link></li>
                  <li><nuxt-link to="/" target="_blank">Data Base</nuxt-link></li>
                </ul>
              </li>
              <li class="has-dropdown">
                <nuxt-link to="/">Features</nuxt-link>
                <ul class="sub-menu">
                  <li><nuxt-link to="/" target="_blank">Scalability</nuxt-link></li>
                  <li><nuxt-link to="/" target="_blank">Usability</nuxt-link></li>
                  <li><nuxt-link to="/" target="_blank">Performance</nuxt-link></li>
                  <li><nuxt-link to="/" target="_blank">Accuracy</nuxt-link></li>
                </ul>
              </li>
              <li class="has-dropdown">
                <nuxt-link to="/" target="_blank">References</nuxt-link>
              </li>

              <li><nuxt-link to="/" target="_blank">Conact Us</nuxt-link></li>
            </ul>
          </div>
          <div class="col-xl-4 d-none d-xl-block">
            <hr class="margin-bottom-0px d-block d-sm-none" />
            <br />
            <nuxt-link
              to="/login"
              class="btn btn-sm border-radius-30 margin-tb-15px text-white background-second-color box-shadow float-right padding-lr-25px margin-left-30px"
              ><i class="fa fa-fw fa-sign-out-alt margin-right-7px"></i>
              Logout</nuxt-link
            >

            <div class="nav-item dropdown float-left">
              <nuxt-link
                to="/account"
                class="margin-top-15px d-inline-block text-grey-3 margin-right-15px"
                ><img
                  :src="require('~/assets/img/avatar.png')"
                  class="height-30px border-radius-30"
                  alt=""
                />
                Pablo Guinea</nuxt-link
              >
            </div>
          </div>
        </div>
      </nav>
    </header>
  </div>
</template>
<script>
export default {
  name: "header-private",
  data() {
    return {};
  },
  props: {
    showLogin: {
      type: Boolean,
      required: false,
    },
  },
};
</script>
<style>
</style>
