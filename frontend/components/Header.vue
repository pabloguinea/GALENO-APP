<template>
  <div>
    <header>
      <div id="fixed-header-dark" class="header-output fixed-header">
        <div class="container header-in">
          <div class="row">
            <div class="col-lg-2 col-md-12">
              <a
                id="logo"
                :to="{ path: '/'}" nuxt
                class="d-inline-block margin-tb-15px"
                ><img  :src="require('~/assets/img/logo-1.png')" width="50%" alt=""
              /></a>
              <a
                class="mobile-toggle padding-13px background-main-color"
                href="#"
                ><i class="fas fa-bars"></i
              ></a>
            </div>
            <div class="col-lg-7 col-md-12 position-inherit">
              <ul
                id="menu-main"
                class="nav-menu float-lg-right link-padding-tb-20px"
              >
                <br />
                <li class="has-dropdown">
                  <a href="#">Patologies</a>
                  <ul class="sub-menu">
                    <li>
                      <a :to="{ path: '/'}" nuxt>Renal Insufficiency</a>
                    </li>
                    <li>
                      <a :to="{ path: '/'}" nuxt>Respiratory Diseases</a>
                    </li>
                    <li><a :to="{ path: '/'}" nuxt>Alzheimer</a></li>
                    <li><a :to="{ path: '/'}" nuxt>Parkinson</a></li>
                  </ul>
                </li>
                <li class="has-dropdown">
                  <a href="#">Technology</a>
                  <ul class="sub-menu">
                    <li><a :to="{ path: '/'}" nuxt>SW Architecture</a></li>
                    <li>
                      <a :to="{ path: '/'}" nuxt>Artificial Intelligence</a>
                    </li>
                    <li><a :to="{ path: '/'}" nuxt>Data Base</a></li>
                  </ul>
                </li>
                <li class="has-dropdown">
                  <a href="#">Features</a>
                  <ul class="sub-menu">
                    <li><a :to="{ path: '/'}" nuxt>Scalability</a></li>
                    <li><a :to="{ path: '/'}" nuxt>Usability</a></li>
                    <li>
                      <a :to="{ path: '/'}" nuxt>Performance</a>
                    </li>
                    <li><a :to="{ path: '/'}" nuxt>Accuracy</a></li>
                  </ul>
                </li>
                <li class="has-dropdown">
                  <a :to="{ path: '/'}" nuxt>References</a>
                </li>

                <li><a :to="{ path: '/'}" nuxt>Conact Us</a></li>
              </ul>
            </div>
            <div class="col-lg-3 col-md-12">
              <br />
              <hr class="margin-bottom-0px d-block d-sm-none" />
              <a
                :to="{ path: '/'}" nuxt
                class="btn btn-sm border-radius-30 margin-tb-15px text-white background-second-color box-shadow float-right padding-lr-20px margin-left-30px"
              >
                <i class="fas fa-user"></i> Login
              </a>
            </div>
          </div>
        </div>
      </div>
    </header>
  </div>
</template>

<style>
.NuxtLogo {
  animation: 1s appear;
  margin: auto;
}

@keyframes appear {
  0% {
    opacity: 0;
  }
}
</style>
