<template>
  <div class="row margin-tb-90px margin-lr-10px sm-mrl-0px">
    <!-- Page Title -->
    <div id="page-title" class="padding-30px background-white full-width">
      <div class="container">
        <ol class="breadcrumb opacity-5">
          <li><nuxt-link to="/dashboard">Home</nuxt-link></li>
          <li class="active">Packages</li>
        </ol>
        <h1 class="font-weight-300">Packages</h1>
      </div>
    </div>
    <!-- // Page Title -->

    <div class="margin-tb-45px full-width">
      <div class="row">
        <!-- Pricing -->
        <div
          class="col-lg-4 col-md-4 col-sm-6 sm-mb-40px wow fadeInUp"
          data-wow-delay="0.2s"
          style="
            visibility: visible;
            animation-delay: 0.2s;
            animation-name: fadeInUp;
          "
        >
          <div class="pricing hover-effect">
            <div class="pricing-head text-center">
              <h3
                class="font-weight-700 padding-40px background-main-color margin-0px text-white"
              >
                <span class="z-index-2 position-relative d-block">
                  BASIC<span class="d-block text-small font-weight-300"></span>
                </span>
              </h3>
              <h2 class="background-grey-1 margin-0px padding-15px">
                <i class="text-up-small">$</i>5<span class="text-up-small"
                  >.49</span
                >
                <span class="d-block text-small">Per Month</span>
              </h2>
            </div>
            <ul
              class="pricing-content text-center list-unstyled background-white"
            >
              <li><strong>50</strong> Patients/month</li>
              <li><strong>2</strong> Pathologies</li>
            </ul>
            <div class="pricing-footer">
              <a
                href="#"
                class="btn btn-block background-grey-1 text-dark rounded-0"
                >Select Plan</a
              >
            </div>
          </div>
        </div>
        <!-- // Pricing -->

        <!-- Pricing -->
        <div
          class="col-lg-4 col-md-4 col-sm-6 sm-mb-40px wow fadeInUp"
          data-wow-delay="0.4s"
          style="
            visibility: visible;
            animation-delay: 0.4s;
            animation-name: fadeInUp;
          "
        >
          <div class="pricing hover-effect">
            <div class="pricing-head text-center">
              <h3
                class="font-weight-700 padding-40px background-second-color margin-0px text-white"
              >
                <span class="z-index-2 position-relative d-block">
                  POWER<span class="d-block text-small font-weight-300"></span>
                </span>
              </h3>
              <h2 class="background-grey-1 margin-0px padding-15px">
                <span class="text-up-small">$</span>9<span class="text-up-small"
                  >.49</span
                >
                <span class="d-block text-small">Per Month </span>
              </h2>
            </div>
            <ul
              class="pricing-content text-center list-unstyled background-white"
            >
              <li><strong>100</strong> Patients/month</li>
              <li><strong>4</strong> Pathologies</li>
            </ul>
            <div class="pricing-footer">
              <a
                href="#"
                class="btn btn-block background-grey-1 text-dark rounded-0"
                >Subscribed</a
              >
            </div>
          </div>
        </div>
        <!-- // Pricing -->

        <!-- Pricing -->
        <div
          class="col-lg-4 col-md-4 col-sm-6 sm-mb-40px wow fadeInUp"
          data-wow-delay="0.6s"
          style="
            visibility: visible;
            animation-delay: 0.6s;
            animation-name: fadeInUp;
          "
        >
          <div class="pricing hover-effect">
            <div class="pricing-head text-center">
              <h3
                class="font-weight-700 padding-40px background-main-color margin-0px text-white"
              >
                <span class="z-index-2 position-relative d-block">
                  ULTIMATE<span
                    class="d-block text-small font-weight-300"
                  ></span>
                </span>
              </h3>
              <h2 class="background-grey-1 margin-0px padding-15px">
                <span class="text-up-small">$</span>19<span
                  class="text-up-small"
                  >.49</span
                >
                <span class="d-block text-small">Per Month </span>
              </h2>
            </div>
            <ul
              class="pricing-content text-center list-unstyled background-white"
            >
              <li><strong>Unlimited</strong> Patients/month</li>
              <li><strong>10</strong> Pathologies</li>
              <li><strong></strong> Tips & Recommendations</li>
            </ul>
            <div class="pricing-footer">
              <a
                href="#"
                class="btn btn-block background-grey-1 text-dark rounded-0"
                >Cooming Soon
              </a>
            </div>
          </div>
        </div>
        <!-- // Pricing -->
      </div>
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
      title: "Packages",
    };
  },
  created() {
    this.initialize();
  },
};
</script>

<style>
</style>
