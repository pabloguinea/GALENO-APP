<template>
  <div id="add-patient">
    <div class="row my-5 py-5 margin-lr-10px sm-mrl-0px">
      <!-- Page Title -->
      <div
        id="page-title"
        class="padding-30px background-white full-width box-shadow"
      >
        <div class="container">
          <ol class="breadcrumb opacity-5">
            <li><nuxt-link to="/dashboard">Home</nuxt-link></li>
            <li><nuxt-link to="/patients">patients</nuxt-link></li>
            <li class="active">Evaluate Patient</li>
          </ol>
          <h1 class="font-weight-300">Evaluate New Patient</h1>
          <br />
          <div class="col-lg-8"></div>
        </div>

        <!-- // Page Title -->
        <div id="regForm" class="">
          <form-wizard
            ref="wizard"
            @on-complete="onCompleteWizard"
            title=""
            :startIndex="startTab"
            subtitle="Please fill the below form. You will see the evaluation results of this patient in the patients list."
            shape="circle"
            color="#0864b2"
            errorColor="#df1c1c"
            back-button-text="Previous"
            next-button-text="Next"
            finish-button-text="Save"
          >
            <tab-content
              title="Names"
              icon="fa fa-user"
              :before-change="() => validateStep()"
            >
              <div class="form-group mb-3">
                <label for="validationCustom01">First name</label>
                <input
                  v-model="form.firstName"
                  required
                  @input="$v.form.firstName.$touch()"
                  type="text"
                  class="form-control"
                  placeholder="First name"
                  value="Mark"
                  :class="{
                    'is-invalid': submitted && $v.form.firstName.$error,
                  }"
                />
                <div
                  v-if="submitted && $v.form.firstName.$error"
                  class="invalid-feedback"
                >
                  <span v-if="!$v.form.firstName.required"
                    >This value is required.</span
                  >
                </div>
              </div>

              <div class="form-group mb-3">
                <label for="validationCustom01">Last name</label>
                <input
                  v-model="form.lastName"
                  required
                  @input="$v.form.lastName.$touch()"
                  type="text"
                  class="form-control"
                  placeholder="Last name"
                  value="Mark"
                  :class="{
                    'is-invalid': submitted && $v.form.lastName.$error,
                  }"
                />
                <div
                  v-if="submitted && $v.form.lastName.$error"
                  class="invalid-feedback"
                >
                  <span v-if="!$v.form.lastName.required"
                    >This value is required.</span
                  >
                </div>
              </div>

              <div class="form-group mb-3">
                <label for="validationCustom01">Email</label>
                <input
                  v-model="form.email"
                  required
                  @input="$v.form.email.$touch()"
                  type="email"
                  class="form-control"
                  placeholder="Email"
                  value="Mark"
                  :class="{
                    'is-invalid': submitted && $v.form.email.$error,
                  }"
                />
                <div
                  v-if="submitted && $v.form.email.$error"
                  class="invalid-feedback"
                >
                  <span v-if="!$v.form.email.required"
                    >This value is required.</span
                  >
                  <span v-if="!$v.form.email.email"
                    >This value must be a valid email.</span
                  >
                </div>
              </div>
            </tab-content>
            <tab-content
              title="Age"
              icon="fa fa-calendar"
              :before-change="() => validateStep()"
            >
              <div class="form-group mb-3">
                <label>Birth Date</label>
                <br />
                <date-picker
                  v-model="form.birthDate"
                  lang="en"
                  :class="{
                    'is-invalid': submitted && $v.form.birthDate.$error,
                  }"
                ></date-picker>
                <br />
                <div
                  v-if="submitted && $v.form.birthDate.$error"
                  class="invalid-feedback"
                >
                  <span v-if="$v.form.birthDate.$error"
                    >This birth date is required.</span
                  >
                </div>
              </div>
            </tab-content>
            <tab-content
              title="MRI Images"
              icon="fa fa-image"
              :before-change="() => validateStep()"
            >
              <file-pond
                maxFileSize="5MB"
                :imageEditAllowEdit="true"
                :required="true"
                name="file"
                ref="pond"
                label-idle="Drop your image here..."
                v-bind:allow-multiple="false"
                accepted-file-types="image/jpeg, image/png"
                :server="uploaderSettings.server"
                v-bind:files="uploadedFiles"
                :onremovefile="handleOnRemoveFile"
                :onprocessfile="handleOnProcesFile"
                :error="handleUploadError"
              />

              <div
                v-if="
                  !currentPatient &&
                  submitted &&
                  (!form.results || !form.results.success)
                "
                class="invalid-feedback d-flex"
              >
                <span>The MRI image is required.</span>
              </div>

              <!---  Current image -->
              <div
                class="d-flex justify-content-center margin-20px"
                v-if="
                  currentPatient &&
                  currentPatient.attributes.picture &&
                  currentPatient.attributes.picture !== ''
                "
              >
                <div
                  style="height: 200px; width: 200px; cursor: pointer"
                  class="image img-fluid"
                  @click="getImageIndex(currentPatient)"
                  :style="{
                    backgroundImage:
                      'url(' + currentPatient.attributes.picture + ')',
                  }"
                ></div>
              </div>

              <b-alert
                v-if="form.results && form.results.most_probable_category"
                show
                :variant="
                  form.results.most_probable_category === '' ||
                  form.results.most_probable_category === 'NonDemented'
                    ? 'dark'
                    : form.results.most_probable_category === 'VeryMildDemented'
                    ? 'info'
                    : form.results.most_probable_category === 'MildDemented'
                    ? 'warning'
                    : 'danger'
                "
              >
                <div>
                  <span class="text-dark card-title"
                    >Classification level:</span
                  >
                  <span class="text-bold">
                    {{ form.results.most_probable_category }}</span
                  >
                </div>
              </b-alert>
            </tab-content>
          </form-wizard>
        </div>
      </div>
    </div>

    <b-toast
      id="validator-toast"
      title="There are errors on the form"
      static
      no-auto-hide
    >
      Please check all the fields of form
    </b-toast>

    <CoolLightBox
      v-if="this.currentPatient"
      :items="imagesSelected"
      :index="indexImage"
      :useZoomBar="true"
      :effect="'fade'"
      :fullScreen="true"
      @close="indexImage = null"
    ></CoolLightBox>
  </div>
</template>

<script>
import moment from "moment";

import CoolLightBox from "vue-cool-lightbox";
import "vue-cool-lightbox/dist/vue-cool-lightbox.min.css";

import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";

import { FormWizard, TabContent } from "vue-form-wizard";
import "vue-form-wizard/dist/vue-form-wizard.min.css";

import { required, minLength, email } from "vuelidate/lib/validators";

import vueFilePond from "vue-filepond";
import "filepond/dist/filepond.min.css";

import FilePondPluginImagePreview from "filepond-plugin-image-preview";
import "filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css";

import FilePondPluginImageEdit from "filepond-plugin-image-edit";
import "filepond-plugin-image-edit/dist/filepond-plugin-image-edit.css";

import FilePondPluginImageCrop from "filepond-plugin-image-crop";
import FilePondPluginFileValidateSize from "filepond-plugin-file-validate-size";
import FilePondPluginFileValidateType from "filepond-plugin-file-validate-type";
import FilePondPluginImageExifOrientation from "filepond-plugin-image-exif-orientation";

// Create component
const FilePond = vueFilePond(
  FilePondPluginFileValidateType,
  FilePondPluginImagePreview,
  FilePondPluginImageEdit,
  /*FilePondPluginImageCrop,*/
  FilePondPluginFileValidateSize,
  FilePondPluginImageExifOrientation
);

export default {
  layout: "private",
  transitions: "page",
  components: {
    FormWizard,
    TabContent,
    DatePicker,
    FilePond,
    CoolLightBox,
  },
  validations: {
    form: {
      firstName: {
        required,
        minLength: minLength(3),
      },
      lastName: {
        required,
      },
      email: {
        required,
        email,
      },
      birthDate: {
        required,
      },
      results: {
        required,
      },
    },
  },
  methods: {
    getImageIndex(patient) {
      this.indexImage = this.imagesSelected.indexOf(patient.attributes.picture);
    },
    onUpload(response) {
      this.form.results = JSON.parse(response);
      if (this.form.results.success) {
        this.$bvToast.toast(
          `Your image has been processed successfully. Now you can to complete the saving of form`,
          {
            title: "Information",
            autoHideDelay: 10000,
            variant: "primary",
            appendToast: false,
          }
        );
      } else {
        this.$bvToast.toast(
          `Your image was not processed correctly, please check your image and upload again.`,
          {
            title: "Error",
            autoHideDelay: 10000,
            variant: "danger",
            appendToast: false,
          }
        );
      }
    },
    handleOnRemoveFile(error, file) {
      this.form.results = null;
    },
    handleUploadError(error, file, status) {
      this.form.results = null;
    },
    handleOnProcesFile(error, file) {
      this.processedFiles.push(file.file);
    },
    validateStep(step) {
      this.submitted = true;
      let isValid = true;
      this.$v.form.$touch();
      console.log(this.$refs.wizard);

      // parcially check the vality of form for each tab
      switch (this.$refs.wizard.activeTabIndex) {
        case 0:
          isValid =
            !this.$v.form.firstName.$invalid &&
            !this.$v.form.lastName.$invalid &&
            !this.$v.form.email.$invalid;

          break;
        case 1:
          isValid = !this.$v.form.birthDate.$invalid;

          break;
        case 2:
          isValid =
            !this.$v.form.firstName.$invalid &&
            !this.$v.form.lastName.$invalid &&
            !this.$v.form.email.$invalid &&
            !this.$v.form.birthDate.$invalid;

          if (!isValid) {
            this.$bvToast.toast(`Please check all the form tabs.`, {
              title: "There are errors on the form",
              autoHideDelay: 10000,
              variant: "danger",
              appendToast: false,
            });
          }

          if (
            !this.currentPatient &&
            isValid &&
            (!this.form.results || !this.form.results.success)
          ) {
            isValid = false;

            this.$bvToast.toast(`Please upload an image MRI before to save.`, {
              title: "Error",
              autoHideDelay: 10000,
              variant: "danger",
              appendToast: false,
            });
          }

          break;
        default:
          break;
      }

      if (!isValid) {
        this.$emit("on-validate", this.$data, isValid);
      }

      return isValid;
    },
    formSubmit(e) {
      this.submitted = true;
      // stop here if form is invalid
      this.$v.$touch();
    },
    async onCompleteWizard() {
      
      let payload = {
        first_name: this.form.firstName,
        last_name: this.form.lastName,
        email: this.form.email,
        birth_date: this.form.birthDate
          ? moment(this.form.birthDate).format("YYYY-MM-DD")
          : null,
        data: this.form.results,
        classification: this.form.results
          ? this.form.results.most_probable_category
          : null,
      };

      console.log("Payload ", payload);
      if (!this.currentPatient) {
        // is creating
        this.currentPatient = await this.$axios
          .post("patients", payload)
          .then((res) => {
            return res.data.data;
          });
      } else {
        // is updating
        await this.$axios.patch("patients/" + this.currentPatient.id, payload);
      }

      console.log(this.processedFiles, this.currentPatient);
      if (this.processedFiles.length > 0 && this.currentPatient.id) {
        
        let file = this.processedFiles[0];

        payload = new FormData();
        payload.append('picture', file, file.name);

        await this.$axios.patch(
          "patients/" + this.currentPatient.id,
          payload,
          {
            headers: {
              "Content-Type": `multipart/form-data; boundary=${payload._boundary}`,
            },
          }
        );
      }

      // upload image to server
      this.$toast.success("The patient was saved correctly.");

      this.$router.push("/patients");

    },
    initialize() {},
  },
  head() {
    return {
      title: `${this.title} | Medical Health Services`,
    };
  },
  async fetch() {
    if (this.$route.query.id) {
      this.currentPatient = await this.$axios
        .get("patients/" + this.$route.query.id)
        .then((res) => {
          return res.data.data;
        });
      console.log("currentPatient ", this.currentPatient);

      if (this.currentPatient) {
        this.form.firstName = this.currentPatient.attributes.first_name;
        this.form.lastName = this.currentPatient.attributes.last_name;
        this.form.email = this.currentPatient.attributes.email;
        this.form.birthDate = new Date(
          this.currentPatient.attributes.birth_date
        );
        this.form.results = this.currentPatient.attributes.data;
        this.form.classification = this.currentPatient.attributes.classification;
        this.form.is_dm_confirmed = this.currentPatient.attributes.is_dm_confirmed;

        if (this.currentPatient.attributes.picture) {
          this.imagesSelected.push(this.currentPatient.attributes.picture);
        }
      }
    }
  },
  data() {
    return {
      startTab: 0,
      errors: [],
      imagesSelected: [],
      indexImage: null,
      currentPatient: null,
      uploaderSettings: {
        server: {
          url: `${process.env.modelApiUrl}/clasify`, 
          process: {
            onload: (response) => this.onUpload(response),
          },
        },
      },
      title: "Dashboard",
      form: {
        firstName: "",
        lastName: "",
        email: "",
        birthDate: "",
        results: "",
      },
      submitted: false,
      submitform: false,
      submit: false,
      uploadedFiles: [],
      processedFiles: [],
    };
  },
  created() {
    this.initialize();
  },
};
</script>

<style lang="scss" >
span.stepTitle.active {
  font-weight: 500;
}
.vue-form-wizard .wizard-nav-pills > li.active > a .wizard-icon,
.vue-form-wizard .wizard-nav-pills > li.active > a:focus .wizard-icon,
.vue-form-wizard .wizard-nav-pills > li.active > a:hover .wizard-icon {
  color: #ffffff;
}
.vue-form-wizard .wizard-icon-circle .wizard-icon {
  display: flex;
  justify-content: center;
  text-align: center;
  align-self: center;
}

#add-patient {
  #regForm {
    display: flex;
    justify-content: center;

    input:not(.is-invalid) {
      padding: 10px;
      width: 100%;
      border: 1px solid #aaaaaa;
    }

    input.is-invalid {
      background-color: #ffdddd;
    }
  }
}
</style>
