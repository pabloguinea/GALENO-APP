<template>
  <div class="">
    <div id="page-title" class="padding-tb-30px gradient-white">
        <div class="container text-center">
            <ol class="breadcrumb opacity-5">
                <li><nuxt-link to="/">Home</nuxt-link></li>
                <li class="active" >Login</li>
            </ol>
            <h1 class="font-weight-300">Login</h1>
        </div>
    </div>

    <div class="container margin-bottom-100px">
        <!--======= log_in_page =======-->
        <div id="log-in" class="site-form log-in-form box-shadow border-radius-10">

            <div class="form-output">
                <form>
                    <div class="form-group label-floating">
                        <label class="control-label">Username</label>
                        <input class="form-control" placeholder="" type="email">
                    </div>
                    <div class="form-group label-floating">
                        <label class="control-label">Password</label>
                        <input class="form-control" placeholder="" type="password">
                    </div>

                    <div class="remember">
                        <div class="checkbox">
                            <label>
							<input name="optionsCheckboxes" type="checkbox">
								Remember Me
						</label>
                        </div>
                        <nuxt-link to="/" class="forgot">Forgot my Password</nuxt-link>
                    </div>

                    <nuxt-link to="/" class="btn btn-md btn-primary full-width">Login</nuxt-link>

                    <div class="or"></div>



                    <p>Don't you have an account? <nuxt-link to="/register">Register Now!</nuxt-link> </p>
                </form>
            </div>
        </div>
        <!--======= // log_in_page =======-->

    </div>
  </div>
</template>

<script>
export default {
    layout: "public",
     
    head() {
        return {
            title: `${this.title} | Medical Health Services`
        };
    },
    data() {
        return {
            title: "Log in"
        };
    }
};
</script>

<style>

</style>
