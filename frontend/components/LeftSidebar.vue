<template>
  <div>
    <nav
      class="navbar navbar-expand-lg navbar-dark z-index-9 fixed-top"
      id="mainNav"
    >
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul
          class="navbar-nav navbar-sidenav background-main-color admin-nav"
          id="admin-nav"
        >
          <li class="nav-item">
            <span class="nav-title-text">Main</span>
          </li>
          <li
            class="nav-item"
            data-toggle="tooltip"
            data-placement="right"
            title="Dashboard"
          >
            <nuxt-link to="/dashboard" class="nav-link " :class="{'active': $nuxt.$route.path === '/dashboard'}">
              <i class="fas fa-fw fa-home"></i
              ><span class="nav-link-text">Dashboard</span>
            </nuxt-link>
          </li>
          <li
            class="nav-item"
            data-toggle="tooltip"
            data-placement="right"
            title="My items"
          >
            <nuxt-link to="/patients" class="nav-link" :class="{'active': $nuxt.$route.path === '/patients'}">
              <i class="fa fa-fw fa-table"></i>
              <span class="nav-link-text">My Patients</span>
            </nuxt-link>
          </li>

          <li class="nav-item">
            <span class="nav-title-text">AI System</span>
          </li>

          <li
            class="nav-item"
            data-toggle="tooltip"
            data-placement="right"
            title="Add Listing"
          >
            <nuxt-link to="/patients/evaluate" class="nav-link" :class="{'active': $nuxt.$route.path === '/patients/evaluate'}">
              <i class="fa fa-fw fa-plus-circle"></i>
              <span class="nav-link-text">Evaluate Patient</span>
            </nuxt-link>
          </li>
          <li
            class="nav-item"
            data-toggle="tooltip"
            data-placement="right"
            title="Packages"
          >
            <nuxt-link to="/packages" class="nav-link" :class="{'active': $nuxt.$route.path === '/packages'}">
              <i class="far fa-fw fa-list-alt"></i>
              <span class="nav-link-text">Packages</span>
            </nuxt-link>
          </li>

          <li class="nav-item">
            <span class="nav-title-text">User Area</span>
          </li>
          <li
            class="nav-item"
            data-toggle="tooltip"
            data-placement="right"
            title="My Profile"
          >
            <nuxt-link to="/account" class="nav-link" :class="{'active': $nuxt.$route.path === '/account'}">
              <i class="fa fa-fw fa-user-circle"></i>
              <span class="nav-link-text">My Profile</span>
            </nuxt-link>
          </li>
          <li
            class="nav-item"
            data-toggle="tooltip"
            data-placement="right"
            title="Sing Out"
          >
            <nuxt-link
              to="/login"
              class="nav-link"
              data-toggle="modal"
              data-target="#exampleModal"
            >
              <i class="fa fa-fw fa-sign-out-alt"></i>
              <span class="nav-link-text">Sing Out</span>
            </nuxt-link>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>
<script>
export default {
  name: "left-sidebar",
  data() {
    return {};
  },
  props: {
    showLogin: {
      type: Boolean,
      required: false,
    },
  },
};
</script>
<style>
</style>
