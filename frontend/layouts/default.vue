
<template>
  <div id="layout-wrapper">
    <!-- ============================================================== -->
    <!-- Start right Content here -->
    <!-- ============================================================== -->
    <div class="main-content">
      <div class="page-content">
        <div class="container-fluid">
          <Header />
          <Nuxt />
        </div>
      </div>
      <!-- End Page-content -->
      <!--<Footer />-->
    </div>
  </div>
</template>

<script>
//import { mapState } from 'vuex'
//import EventBus from '../helpers/utils/EventBus'

/**
 * Vertical layout
 */
export default {
  name: 'default',
  created() {},
  methods: {},
  data() {
    return {}
  },
  mounted() {
    //this.toggleMenu();
  }/*,
  computed: mapState(['layout']),*/
}
</script>

<style>

</style>
