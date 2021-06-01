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
          <file-pond
            v-if="!profileAvatar || profileAvatar === ''"
            maxFileSize="5MB"
            :imageEditAllowEdit="true"
            :required="true"
            name="file"
            ref="pond"
            label-idle="Drop your photo here..."
            v-bind:allow-multiple="false"
            accepted-file-types="image/jpeg, image/png"
            :server="uploaderSettings.server"
            v-bind:files="uploadedFiles"
            :onremovefile="handleOnRemoveFile"
            :onprocessfile="handleOnProcesFile"
            :error="handleUploadError"
          />

          <a
            v-else
            href=""
            @click.prevent=""
            class="d-flex justify-content-center d-block margin-bottom-10px"
            ><img
              :src="profileAvatar"
              class="img-fluid"
              style="max-width: 500px"
              alt=""
          /></a>

          <a
            v-if="profileAvatar && profileAvatar !== ''"
            href=""
            @click.prevent="profileAvatar = null"
            class="btn btn-sm text-white background-main-color btn-block"
            >Change Image</a
          >
        </div>
      </div>
      <div class="col-md-8">
        <div class="row">
          <div class="col-md-6 margin-bottom-20px">
            <label
              ><i class="far fa-user margin-right-10px"></i> First Name</label
            >
            <input
              type="text"
              class="form-control form-control-sm"
              placeholder=""
              v-model="form.firstName"
            />
          </div>
          <div class="col-md-6 margin-bottom-20px">
            <label
              ><i class="fas fa-lock margin-right-10px"></i> Last Name</label
            >
            <input
              type="text"
              v-model="form.lastName"
              class="form-control form-control-sm"
            />
          </div>
          <div class="col-md-6 margin-bottom-20px">
            <label
              ><i class="far fa-envelope-open margin-right-10px"></i>
              Email</label
            >
            <input
              type="text"
              class="form-control form-control-sm"
              v-model="form.email"
              placeholder=""
            />
          </div>
          <div class="col-md-6 margin-bottom-20px">
            <label
              ><i class="fas fa-mobile-alt margin-right-10px"></i>
              Speciality</label
            >
            <select class="selectpicker form-control" v-model="form.area">
              <option value="P">Pneumology</option>
              <option value="N">Neurology</option>
              <option value="U">Urology</option>
            </select>
          </div>
          <div class="col-md-6">
            <label><i class="fas fa-link margin-right-10px"></i> Card ID</label>
            <input
              type="text"
              class="form-control form-control-sm"
              v-model="form.cardId"
              placeholder=""
            />
          </div>
          <div class="col-md-6">
            <label><i class="fas fa-info margin-right-10px"></i> Role</label>
            <input
              type="text"
              class="form-control form-control-sm"
              v-model="form.role"
              readonly
              placeholder=""
            />
          </div>
        </div>

        <a
          href=""
          @click.prevent="updateProfile()"
          class="btn btn-md margin-tb-40px padding-lr-25px text-white background-main-color btn-inline-block"
          >Update Profile</a
        >
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
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
  middleware: "authenticated",
  components: {
    FilePond,
  },
  computed: {
    ...mapState({
      user: (state) => state.auth.user,
      access_token: (state) => state.auth.access_token,
    }),
    uploaderSettings() {
      if (!this.accessToken) {
        this.accessToken = this.access_token;
      }
      return {
        server: {
          url: "https://api.galenoapp.teamcloud.com.co/v1/auth/users/me/",
          process: {
            onload: (response) => this.onUpload(response),
            method: "patch",
            headers: {
              Authorization: 'Bearer '+this.accessToken,
            },
          },
        },
      };
    },
  },

  head() {
    return {
      title: `${this.title} | Medical Health Services`,
    };
  },
  data() {
    return {
      title: "My Profile",
      profileAvatar: "",
      uploadedFiles: [],
      accessToken: null,
      form: {
        email: "",
        firstName: "",
        lastName: "",
        cardId: "",
        role: "",
      },
    };
  },
  methods: {
    initialize() {
      if (this.user) {
        this.form.email = this.user.attributes.email;
        this.form.firstName = this.user.attributes.first_name;
        this.form.lastName = this.user.attributes.last_name;
        this.form.cardId = this.user.attributes.card_id;
        this.form.area = this.user.attributes.area;
        this.form.role = this.user.attributes.role;
        this.profileAvatar = this.user.attributes.avatar;
      }
    },
    onUpload(response) {
      console.log(response);
    },
    handleOnRemoveFile(error, file) {},
    handleUploadError(error, file, status) {
      this.$toast.success("Error uploading the photo.");
    },
    handleOnProcesFile(error, file) {},
    async updateProfile() {
      await this.$axios.patch("auth/users/me/", this.form);
      this.$toast.success("Your profile was updated correctly.");
    },
  },

  mounted() {
    this.initialize();
  },

  watch: {
    access_token(data) {
      this.accessToken = data;
    },
  },
};
</script>

<style>
</style>
