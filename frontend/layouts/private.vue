
<template>
  <div class="private-view">
    <header-private :show-login="false" />

    <left-sidebar />
    <div class="content-wrapper">
      <div class="container-fluid overflow-hidden">
        <Nuxt />
      </div>
    </div>
    
    <footer-private />

    <!-- Scroll to Top Button-->
    <nuxt-link to="/"  class="scroll-to-top rounded" href="#page-top">
        <i class="fa fa-angle-up"></i>
    </nuxt-link>
    
    <!-- Modal Logout -->
     <logout-modal />


  </div>
</template>

<script>
import HeaderPrivate from "~/components/HeaderPrivate.vue";
import LeftSidebar from "~/components/LeftSidebar.vue";
import LogoutModal from '~/components/LogoutModal.vue';
//import { mapState } from 'vuex'
//import EventBus from '../helpers/utils/EventBus'

/**
 * Vertical layout
 */
export default {
  components: { LeftSidebar, HeaderPrivate, LogoutModal },
  name: "private",

  created() {},
  methods: {},
  data() {
    return {};
  },
  mounted() {
    //this.toggleMenu();
  } /*,
  computed: mapState(['layout']),*/,
};
</script>

<style>
</style>
