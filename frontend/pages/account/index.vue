<template>
  <div class="row margin-tb-90px margin-lr-10px sm-mrl-0px">
    <!-- Page Title -->
    <div id="page-title" class="padding-30px background-white full-width">
      <div class="container">
        <ol class="breadcrumb opacity-5">
          <li><nuxt-link to="/dashboard">Home</nuxt-link></li>
          <li class="active">My Profile</li>
        </ol>
        <h1 class="font-weight-300">My Profile</h1>
      </div>
    </div>
    <!-- // Page Title -->

    <div class="row margin-tb-45px full-width">
      <div class="col-md-4">
        <div class="padding-15px background-white">
          <a href="#" class="d-block margin-bottom-10px"
            ><img :src='require("~/assets/img/profile.jpg")' alt=""
          /></a>
          <a
            href="#"
            class="btn btn-sm text-white background-main-color btn-block"
            >Upload Image</a
          >
        </div>
      </div>
      <div class="col-md-8">
        <div class="row">
          <div class="col-md-6 margin-bottom-20px">
            <label><i class="far fa-user margin-right-10px"></i>Name</label>
            <input
              type="text"
              class="form-control form-control-sm"
              placeholder="Pablo Guinea Benito"
            />
          </div>
          <div class="col-md-6 margin-bottom-20px">
            <label
              ><i class="fas fa-lock margin-right-10px"></i> Username</label
            >
            <input
              type="text"
              class="form-control form-control-sm"
              placeholder="PG1HM"
            />
          </div>
          <div class="col-md-6 margin-bottom-20px">
            <label
              ><i class="fas fa-lock margin-right-10px"></i>Your Card ID</label
            >
            <input
              type="text"
              class="form-control form-control-sm"
              placeholder="87234832"
            />
          </div>
          <div class="col-md-6 margin-bottom-20px">
            <label
              ><i class="far fa-envelope-open margin-right-10px"></i
              >Email</label
            >
            <input
              type="text"
              class="form-control form-control-sm"
              placeholder="pablo.guinea@hmhospitales.es"
            />
          </div>
          <div class="col-md-6">
            <label
              ><i class="fas fa-link margin-right-10px"></i> Speciality</label
            >
            <input
              type="text"
              class="form-control form-control-sm"
              placeholder="Neurologist"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  layout: "private",
  transitions: "page",
  middleware: 'authenticated',
  methods: {
    initialize() {},
  },
  head() {
    return {
      title: `${this.title} | Medical Health Services`,
    };
  },
  data() {
    return {
      title: "My Profile",
    };
  },
  created() {
    this.initialize();
  },
};
</script>

<style>
</style>
