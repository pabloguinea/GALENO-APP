<template>
  <div class="">
    <section
      class="banner padding-tb-150px sm-ptb-80px background-overlay"
      :style="{'background-image': 'url('+require('~/assets/img/bg.jpg')+')'}"

    >
      <div class="container z-index-2 position-relative">
        <div class="title">
          <br /><br />
          <h1
            class="text-title-large text-main-color font-weight-300 margin-bottom-15px"
          >
            Decision Support System
          </h1>
          <br /><br />
          <h4 class="font-weight-300 text-main-color text-up-small">
            Suitable for healthcare professionals only.
          </h4>
        </div>
        <br /><br /><br /><br /><br />
        <div class="row">
          <div class="col-lg-7">
            <div class="row">
              <div class="col-md-3 col-6 sm-mb-30px wow fadeInUp">
                <a href="#" class="d-block border-radius-15 hvr-float hvr-sh2">
                  <div
                    class="background-main-color text-white border-radius-15 padding-20px text-center opacity-hover-7"
                  >
                    <div class="icon margin-bottom-15px opacity-7">
                      <img :src="require('~/assets/img/icon/categorie-1.png')" alt="" />
                    </div>
                    Doctors
                  </div>
                </a>
              </div>
              <div
                class="col-md-3 col-6 sm-mb-30px wow fadeInUp"
                data-wow-delay="0.2s"
              >
                <a href="#" class="d-block border-radius-15 hvr-float hvr-sh2">
                  <div
                    class="background-main-color text-white border-radius-15 padding-20px text-center opacity-hover-7"
                  >
                    <div class="icon margin-bottom-15px opacity-7">
                      <img :src="require('~/assets/img/icon/categorie-2.png')" alt="" />
                    </div>
                    Clinics
                  </div>
                </a>
              </div>
              <div class="col-md-3 col-6 wow fadeInUp" data-wow-delay="0.4s">
                <a href="#" class="d-block border-radius-15 hvr-float hvr-sh2">
                  <div
                    class="background-main-color text-white border-radius-15 padding-20px text-center opacity-hover-7"
                  >
                    <div class="icon margin-bottom-15px">
                      <img :src="require('~/assets/img/icon/categorie-3.png')" alt="" />
                    </div>
                    Labs
                  </div>
                </a>
              </div>
              <div class="col-md-3 col-6 wow fadeInUp" data-wow-delay="0.6s">
                <a href="#" class="d-block border-radius-15 hvr-float hvr-sh2">
                  <div
                    class="background-main-color text-white border-radius-15 padding-20px text-center opacity-hover-7"
                  >
                    <div class="icon margin-bottom-15px opacity-7">
                      <img :src="require('~/assets/img/icon/categorie-4.png')" alt="" />
                    </div>
                    Pharmacies
                  </div>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="padding-tb-100px">
      <div class="container">
        <div class="row">
          <div class="col-lg-3 col-md-6 sm-mb-30px wow fadeInUp">
            <div class="service text-center opacity-hover-7 hvr-bob">
              <div class="icon margin-bottom-10px">
                <img :src="require('~/assets/img/icon/service-1.png')" alt="" />
              </div>
              <h3 class="text-second-color">Reliable Data</h3>
              <p class="text-grey-2">
                Our models are trained with real patient data and are
                continuously learning from new patient data verified by
                healthcare specialists.
              </p>
            </div>
          </div>

          <div
            class="col-lg-3 col-md-6 sm-mb-30px wow fadeInUp"
            data-wow-delay="0.2s"
          >
            <div class="service text-center opacity-hover-7 hvr-bob">
              <div class="icon margin-bottom-10px">
                <img :src="require('~/assets/img/icon/service-2.png')" alt="" />
              </div>
              <h3 class="text-second-color">High Scalability</h3>
              <p class="text-grey-2">
                Galeno is ready to scale with the inclusion of models for new
                pathologies and new patient data based on clinical evidence.
              </p>
            </div>
          </div>

          <div
            class="col-lg-3 col-md-6 sm-mb-30px wow fadeInUp"
            data-wow-delay="0.4s"
          >
            <div class="service text-center opacity-hover-7 hvr-bob">
              <div class="icon margin-bottom-10px">
                <img :src="require('~/assets/img/icon/service-3.png')" alt="" />
              </div>
              <h3 class="text-second-color">Quick results</h3>
              <p class="text-grey-2">
                The results and reports are automatically generated by Galeno
                after the correct upload of the necessary data.
              </p>
            </div>
          </div>

          <div
            class="col-lg-3 col-md-6 sm-mb-30px wow fadeInUp"
            data-wow-delay="0.6s"
          >
            <div class="service text-center opacity-hover-7 hvr-bob">
              <div class="icon margin-bottom-10px">
                <img :src="require('~/assets/img/icon/service-4.png')" alt="" />
              </div>
              <h3 class="text-second-color">Know better</h3>
              <p class="text-grey-2">
                Although the diagnosis provided by Galen is not conclusive, it
                provides an expert point of view to be considered by the
                healthcare specialist.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {};
</script>

<style>

</style>
