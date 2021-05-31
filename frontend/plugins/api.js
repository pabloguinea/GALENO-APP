export default function ({ $axios }, inject) {
    // Create a custom axios instance
    const api = $axios.create({
        headers: {
            common: {
                /*Add here authroization key from cookie */
            }
        }
    })

    // Set baseURL to something different
    //api.setBaseURL('https://my_api.com')

    // Inject to context as $api
    inject('api', api)

    // aslso is possible inject the authorization header directly:
    // https://axios.nuxtjs.org/helpers
    //this.$axios.setHeader('Authorization', '123')
    // this.$axios.setToken('123', 'Bearer')
}