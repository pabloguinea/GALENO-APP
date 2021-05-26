<template>
  <div>
    <header>
      <div id="fixed-header-dark" class="header-output fixed-header">
        <div class="container header-in">
          <div class="row">
            <div class="col-lg-2 col-md-12">
              <nuxt-link to="/"
                id="logo"
                class="d-inline-block margin-tb-15px"
                ><img  :src="require('~/assets/img/logo-1.png')" width="50%" alt=""
              /></nuxt-link>
              <nuxt-link to="/"
                class="mobile-toggle padding-13px background-main-color"
                ><i class="fas fa-bars"></i
              ></nuxt-link>
            </div>
            <div class="col-lg-7 col-md-12 position-inherit">
              <ul
                id="menu-main"
                class="nav-menu float-lg-right link-padding-tb-20px"
              >
                <br />
                <li class="has-dropdown">
                  <nuxt-link to="/">Patologies</nuxt-link>
                  <ul class="sub-menu">
                    <li>
                      <nuxt-link to="/">Renal Insufficiency</nuxt-link>
                    </li>
                    <li>
                      <nuxt-link to="/">Respiratory Diseases</nuxt-link>
                    </li>
                    <li><nuxt-link to="/">Alzheimer</nuxt-link></li>
                    <li><nuxt-link to="/">Parkinson</nuxt-link></li>
                  </ul>
                </li>
                <li class="has-dropdown">
                  <nuxt-link to="/">Technology</nuxt-link>
                  <ul class="sub-menu">
                    <li><nuxt-link to="/">SW Architecture</nuxt-link></li>
                    <li>
                      <nuxt-link to="/">Artificial Intelligence</nuxt-link>
                    </li>
                    <li><nuxt-link to="/">Data Base</nuxt-link></li>
                  </ul>
                </li>
                <li class="has-dropdown">
                  <nuxt-link to="/">Features</nuxt-link>
                  <ul class="sub-menu">
                    <li><nuxt-link to="/">Scalability</nuxt-link></li>
                    <li><nuxt-link to="/">Usability</nuxt-link></li>
                    <li>
                      <nuxt-link to="/">Performance</nuxt-link>
                    </li>
                    <li><nuxt-link to="/" >Accuracy</nuxt-link> </li>
                  </ul>
                </li>
                <li class="has-dropdown">
                  <nuxt-link to="/" >References</nuxt-link>
                  <!--<nuxt-link to="/">References</nuxt-link>-->
                </li>

                <li><nuxt-link to="/">Conact Us</nuxt-link></li>
              </ul>
            </div>
            <div class="col-lg-3 col-md-12">
              <br />
              <hr class="margin-bottom-0px d-block d-sm-none" />
              <nuxt-link to="/"
                class="btn btn-sm border-radius-30 margin-tb-15px text-white background-second-color box-shadow float-right padding-lr-20px margin-left-30px"
              >
                <i class="fas fa-user"></i> Login
              </nuxt-link>
            </div>
          </div>
        </div>
      </div>
    </header>
  </div>
</template>

<style>

</style>
