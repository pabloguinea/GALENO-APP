// reusable aliases for mutations
export const AUTH_MUTATIONS = {
  SET_USER: 'SET_USER',
  SET_PAYLOAD: 'SET_PAYLOAD',
  LOGOUT: 'LOGOUT',
}

export const state = () => ({
  access_token: null, // JWT access token
  refresh_token: null, // JWT refresh token
  id: null, // user id
  user: null, // user email address
  authenticated: false,
})

export const mutations = {
  // store the logged in user in the state
  [AUTH_MUTATIONS.SET_USER](state, payload) {
    state.id = payload.id
    state.user = payload
    state.authenticated = true
  },

  // store new or updated token fields in the state
  [AUTH_MUTATIONS.SET_PAYLOAD](state, payload) {

    state.access_token = payload.access

    // refresh token is optional, only set it if present
    if (payload.refresh) {
      state.refresh_token = payload.refresh
    }
  },

  // clear our the state, essentially logging out the user
  [AUTH_MUTATIONS.LOGOUT](state) {
    state.id = null
    state.user = null
    state.access_token = null
    state.refresh_token = null
    state.authenticated = false
  },
}

export const actions = {
  async login({ commit, dispatch }, credentials) {

    // make an API call to login the user with an email address and password
    const { data: { data } } = await this.$axios.post(
      '/auth/jwt/create',
      credentials
    )

    // commit the tokens to the state
    commit(AUTH_MUTATIONS.SET_PAYLOAD, data)

    // Get the user authenticated
    await dispatch('get_user')

  },

  async get_user({ commit, dispatch }) {

    // make an API call to login the user with an email address and password
    const { data: { data } } = await this.$axios.get(
      '/auth/users/me/'
    )

    // commit the user 
    commit(AUTH_MUTATIONS.SET_USER, data)
  },

  async register({ commit }, payload) {
    // make an API call to register the user
    await this.$axios.post(
      '/auth/users/',
      payload
    )

    this.$toast.success('Your account was successfully created. To activate your account please check by the confirmation email.')

  },

  // given the current refresh token, refresh the user's access token to prevent expiry
  async refresh({ commit, state }) {
    const { refresh_token } = state

    // make an API call using the refresh token to generate a new access token
    const { data: { data: { payload } } } = await this.$axios.post(
      '/auth/jwt/refresh',
      { refresh_token }
    )

    commit(AUTH_MUTATIONS.SET_PAYLOAD, payload)
  },

  // logout the user
  logout({ commit, state }) {
    commit(AUTH_MUTATIONS.LOGOUT)
  },
}

export const getters = {
  // determine if the user is authenticated based on the presence of the access token
  isAuthenticated: (state) => {
    return state.access_token && state.access_token !== ''
  },
}