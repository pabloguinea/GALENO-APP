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
      <CoolLightBox
        :items="imagesSelected"
        :index="indexImage"
        :useZoomBar="true"
        :effect="'fade'"
        :fullScreen="true"
        @close="indexImage = null"
      ></CoolLightBox>

      <!-- clinic -->
      <div
        class="background-white thum-hover box-shadow hvr-float full-width margin-bottom-45px"
        v-for="patient of this.patients"
        :key="patient.id"
      >
        <div
          class="float-lg-left margin-right-30px sm-mr-0px text-center sm-mt-35px"
        >
          <div
            style="height: 200px; width: 200px; cursor:pointer;"
            v-if="
              patient.attributes.picture && patient.attributes.picture !== ''
            "
            class="image img-fluid"
            @click="getImageIndex(patient)"
            :style="{
              backgroundImage: 'url(' + patient.attributes.picture + ')',
            }"
          ></div>

          <img v-else src="http://placehold.it/200x200" alt="" />
        </div>
        <div class="padding-lr-25px padding-tb-25px">
          <h2>
            <span
              class="d-inline-block text-dark text-capitalize text-medium margin-tb-5px"
              >{{ patient.attributes.first_name }}
              {{ patient.attributes.last_name }}</span
            >
            <nuxt-link :to="`/patients/evaluate?id=${patient.id}`"
              class="d-inline-block margin-lr-10px text-grey-2 text-up-small"
              ><i class="far fa-file-alt"></i> Edit</nuxt-link>
            <a
              href=""
              @click.prevent="deletePatient(patient)"
              class="d-inline-block margin-lr-10px text-grey-2 text-up-small"
              ><i class="far fa-window-close"></i> Delete</a
            >
          </h2>
          <div class="d-flex justify-content-start">
            <span class="text-grey-2 mr-5"
              ><i class="far fa-user"></i> Email: {{ patient.attributes.email }}
            </span>
            <span class="text-grey-2"
              ><i class="far fa-calendar"></i> Birth Date:
              {{ patient.attributes.birth_date }}
            </span>
          </div>
          <div class="d-flex justify-content-start">
            <span class="text-grey-2 mr-5" v-if="patient.attributes.data"
              ><i class="far fa-user"></i> Diagnosis:
              <span
                class=""
                :class="{
                  'text-primary': patient.attributes.is_dm_confirmed,
                  'text-danger': false === patient.attributes.is_dm_confirmed,
                }"
                >{{ patient.attributes.data.most_probable_category }}
                <span
                  class="text-warning"
                  v-if="null === patient.attributes.is_dm_confirmed"
                  >(Non validated)</span
                >
              </span>
            </span>
          </div>
          <div class="row no-gutters padding-top-30px">
            <div class="col-lg-6 row">
              <div class="col-6">
                <a
                  href=""
                  @click.prevent="confirmDiagnostic(true, patient.id)"
                  class="text-lime"
                  ><i class="far fa-thumbs-up"></i> Correct diagnosis</a
                >
              </div>
              <div class="col-6 text-center">
                <a
                  href=""
                  @click.prevent="confirmDiagnostic(false, patient.id)"
                  class="text-red"
                  ><i class="far fa-thumbs-down"></i> Diagnostic error</a
                >
              </div>
            </div>
          </div>
        </div>
        <div class="clearfix"></div>
      </div>

      <!-- pagination -->
      <!--
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
      -->
      <!-- //pagination -->
    </div>
  </div>
</template>

<script>
import CoolLightBox from "vue-cool-lightbox";
import "vue-cool-lightbox/dist/vue-cool-lightbox.min.css";
export default {
  layout: "private",
  transitions: "page",
  components: {
    CoolLightBox,
  },
  methods: {
    async confirmDiagnostic(value, patientId) {
      await this.$axios.patch("patients/" + patientId, {
        is_dm_confirmed: value,
      });

      this.$toast.success("Patient updated correctly.");

      // reload list
      this.$fetch();
    },

    getImageIndex(patient) {
      this.indexImage = this.imagesSelected.indexOf(patient.attributes.picture);
    },

    deletePatient(patient) {
      this.$confirm({
        message: `Are you sure of delete ${patient.attributes.first_name} ${patient.attributes.last_name} ?`,
        button: {
          no: "No",
          yes: "Yes, Delete",
        },
        /**
         * Callback Function
         * @param {Boolean} confirm
         */
        callback: async (confirm) => {
          if (confirm) {
            await this.$axios.delete("patients/" + patient.id);
            this.$toast.success("Patient deleted correctly.");

            // reload list
            this.$fetch();
          }
        },
      });
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
      imagesSelected: [],
      patientsSelected: [],
      indexImage: null,
      patients: [],
    };
  },
  async fetch() {
    this.patients = await this.$axios.get("patients").then((res) => {
      return res.data.data;
    });
    this.patients.forEach((patient) => {
      if (patient.attributes.picture) {
        this.imagesSelected.push(patient.attributes.picture);
      }
    });
    console.log("Patients: ", this.patients);
    console.log("Patients: ", this.imagesSelected);
  },
  created() {},
};
</script>

<style>
</style>
