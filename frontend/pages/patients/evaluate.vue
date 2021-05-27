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
            :startIndex="2"
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
                :acceptedFileTypes="['image/png', 'image/jpeg']"
                :imageEditAllowEdit="true"
                name="test"
                ref="pond"
                label-idle="Drop your image here..."
                v-bind:allow-multiple="false"
                accepted-file-types="image/jpeg, image/png"
                :server="apiUrl"
                v-bind:files="uploadedFiles"
                v-on:onremovefile="handleOnRemoveFile"
                v-on:onprocessfile="handleOnProcesFile"
                v-on:error="handleUploadError"
              />

              <div
                v-if="submitted && $v.form.image.$error"
                class="invalid-feedback d-flex"
              >
                <span v-if="$v.form.image.$error"
                  >The MRI image is required.</span
                >
              </div>
            </tab-content>
          </form-wizard>
        </div>
      </div>
    </div>

    <b-toast id="validator-toast" title="There are errors on the form" static no-auto-hide>
      Please check all the fields of form
    </b-toast>

  </div>
</template>

<script>
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
import FilePondPluginFileValidateSize from 'filepond-plugin-file-validate-size';
import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type';
import FilePondPluginImageExifOrientation from 'filepond-plugin-image-exif-orientation';


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
      image: {
        required,
      },
    },
  },
  methods: {
    handleOnRemoveFile(error, file){
      debugger;
    },
    handleUploadError(error, file, status){
      debugger;
    },
    handleOnProcesFile(error, file){
      debugger;
    },
    handleFilePondInit: function () {
      console.log("FilePond has initialized");

      // FilePond instance methods are available on `this.$refs.pond`
    },
    validateStep(step) {
      this.submitted = true;
      let isValid = false;
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
          isValid = !this.$v.form.firstName.$invalid &&
            !this.$v.form.lastName.$invalid &&
            !this.$v.form.email.$invalid  &&
            !this.$v.form.birthDate.$invalid &&
            !this.$v.form.image.$invalid;
          if(!isValid){
            this.$bvToast.toast(`Please check all the form tabs.`, {
              title: 'There are errors on the form',
              autoHideDelay: 5000,
              variant:'danger',
              appendToast: false
            });
          } 
          break;
        default:
          break;
      }

      if(!isValid){
        this.$emit("on-validate", this.$data, isValid);
      }else{
        debugger
      }
      
      return isValid;
    },
    formSubmit(e) {
      this.submitted = true;
      // stop here if form is invalid
      this.$v.$touch();
    },
    onCompleteWizard() {
      let isLatest = false;
      if (this.$refs.wizard) {
        isLatest = this.$refs.wizard.isLastStep;
      }
    },
    initialize() {},
  },
  head() {
    return {
      title: `${this.title} | Medical Health Services`,
    };
  },
  data() {
    return {
      errors: [],
      apiUrl: "https://galenoapp.teamcloud.com.co/api",
      title: "Dashboard",
      form: {
        firstName: "",
        lastName: "",
        email: "",
        birthDate: "",
        image: "",
      },
      submitted: false,
      submitform: false,
      submit: false,
      uploadedFiles: [],
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
