<template>
  <div id="patients">
    <div class="row margin-tb-90px margin-lr-10px sm-mrl-0px">
      <!-- Page Title -->
      <div
        id="page-title"
        class="padding-30px background-white full-width box-shadow"
      >
        <div class="container">
          <ol class="breadcrumb opacity-5">
            <li><nuxt-link to="/dashboard">Home</nuxt-link></li>
            <li class="active">My Patients</li>
          </ol>
          <h1 class="font-weight-300">My Patients</h1>
          <br />
          <div class="col-lg-8"></div>
        </div>
      </div>
    </div>

    <!-- // Page Title -->
    <div class="margin-tb-45px">
      <!-- clinic -->
      <div
        class="background-white thum-hover box-shadow hvr-float full-width margin-bottom-45px"
      >
        <div
          class="float-lg-left margin-right-30px sm-mr-0px text-center sm-mt-35px"
        ></div>
        <div class="padding-lr-25px padding-tb-45px">
          <h2>
            <nuxt-link
              to="/dashboard"
              class="d-inline-block text-dark text-capitalize text-medium margin-tb-15px"
              >Pedro García Colmenero<br />
              Birth Date: 24/06/1956 <br />
              Mild Demented</nuxt-link
            >
            >
            <nuxt-link
              to="/dashboard"
              class="d-inline-block margin-lr-10px text-grey-2 text-up-small"
              ><i class="far fa-window-close"></i> Delete</nuxt-link
            >
            >
          </h2>
          <div class="row no-gutters">
            <div class="col-lg-6 row">
              <div class="col-4 text-center">
                <nuxt-link to="/dashboard" class="text-lime"
                  ><i class="far fa-thumbs-up"></i> Correct diagnosis</nuxt-link>
              </div>
              <div class="col-4 text-center">
                <nuxt-link to="/dashboard" class="text-red"
                  ><i class="far fa-thumbs-down"></i> Diagnostic
                  error</nuxt-link>
              </div>
              <div class="col-4 text-center">
                <nuxt-link to="/dashboard" class="text-blue"
                  ><i class="fa fa-eye"></i> See diagnostic</nuxt-link>
              </div>
            </div>
          </div>
        </div>
        <div class="clearfix"></div>
      </div>
      <!-- // clinic -->

      <!-- pagination -->
      <ul class="pagination pagination-md">
        <li class="page-item disabled">
          <nuxt-link to="/dashboard" class="page-link rounded-0" tabindex="-1"
            >Previous</nuxt-link
          >
        </li>
        <li class="page-item">
          <nuxt-link to="/dashboard" class="page-link">1</nuxt-link>
        </li>
        <li class="page-item">
          <nuxt-link to="/dashboard" class="page-link">2</nuxt-link>
        </li>
        <li class="page-item">
          <nuxt-link to="/dashboard" class="page-link">3</nuxt-link>
        </li>
        <li class="page-item">
          <nuxt-link to="/dashboard" class="page-link rounded-0"
            >Next</nuxt-link
          >
        </li>
        <br /><br /><br /><br /><br /><br />
      </ul>
      <!-- //pagination -->
    </div>
  </div>
</template>

<script>
export default {
  layout: "private",
  transitions: "page",
  methods: {
    initialize() {
     
    },
  },
  head() {
    return {
      title: `${this.title} | Medical Health Services`,
    };
  },
  data() {
    return {
      title: "Dashboard",
    };
  },
  created() {
    this.initialize();
  },
};
</script>

<style>
</style>
