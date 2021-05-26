
<template>
  <div class="pulbic-view">
    <HeaderPublic :show-login="false" />
    
      <Nuxt />
    
    <Footer />
  </div>
</template>

<script>
//import { mapState } from 'vuex'
//import EventBus from '../helpers/utils/EventBus'

/**
 * Vertical layout
 */
export default {
  name: "public",
   
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
