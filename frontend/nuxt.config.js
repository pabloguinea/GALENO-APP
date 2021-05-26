export default {
  server: {
    host: 'localhost' // 0: localhost - 1: anywhere
  },

  // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
  ssr: false,

  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'Galeno App',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Health Care & Medical Services' },
    ],
    link: [
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Open+Sans:400,600,800%7CPoppins:300i,300,400,700,400i,500%7CDancing+Script:700%7CDancing+Script:700' },
      { rel: 'icon', type: 'image/x-icon', href: '/assets/img/favicon.ico' },
    ],
    script: [
      {
        src: "https://use.fontawesome.com/releases/v5.0.6/js/all.js",
        body: true,
        async: true,
      },
      {
        src: "//code.jquery.com/jquery-3.2.1.min.js"
      },
      {
        type: 'text/javascript',
        src: "/assets/js/sticky-sidebar.js",
        body: true,
      },
      {
        type: 'text/javascript',
        src: "/assets/js/YouTubePopUp.jquery.js",
        body: true,
        async: true,
      },
      {
        type: 'text/javascript',
        src: "/assets/js/owl.carousel.min.js",
        body: true,
      },
      {
        type: 'text/javascript',
        src: "/assets/js/imagesloaded.min.js",
        body: true,
      },
      {
        type: 'text/javascript',
        src: "/assets/js/wow.min.js",
        body: true,
      },
      {
        type: 'text/javascript',
        src: "/assets/js/popper.min.js",
        body: true,
      },
      {
        type: 'text/javascript',
        src: "/assets/js/bootstrap.min.js",
        body: true,
      },
      {
        type: 'text/javascript',
        src: "/assets/js/custom.js",
        body: true,
      },
    ],
  },


  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@/assets/css/animate.css',
    '@/assets/css/owl.carousel.css',
    '@/assets/css/owl.theme.css',
    /*'@/assets/css/bootstrap.min.css',*/
    '@/assets/css/hover-min.css',
    '@/assets/css/flag-icon.min.css',
    /*"@/assets/css/style.css",*/
    /*'@/assets/css/colors/main',*/
    '@/assets/css/elegant_icon.css',
    '@/assets/sass/style.scss',
    '@/assets/sass/custom.scss',
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
   /* '@nuxtjs/eslint-module',*/
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {},

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en',
    },
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    extractCSS: true,
  }
}
