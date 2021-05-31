<template>
  <div id="dashboard" class="row margin-tb-90px margin-lr-10px sm-mrl-0px">
    <div class="col-xl-3 col-md-6 margin-bottom-30px">
      <a
        class="d-block padding-30px background-main-color box-shadow border-radius-10 hvr-float"
      >
        <h6 class="text-white margin-0px font-weight-400">
          <i
            class="far fa-user text-icon-large margin-bottom-10px opacity-5 d-block"
          ></i>

          <span class="font-2 text-extra-large">17</span>
          <span class="margin-left-10px">Patients</span>
          <p></p>
        </h6>
      </a>
    </div>

    <div class="col-xl-3 col-md-6 margin-bottom-30px">
      <a
        class="d-block padding-30px background-lime box-shadow border-radius-10 hvr-float"
      >
        <h6 class="text-white margin-0px font-weight-400">
          <i
            class="far fa-user text-icon-large margin-bottom-10px opacity-5 d-block"
          ></i>
          <span class="font-2 text-extra-large">9</span>
          <span class="margin-left-10px">Patients with pathologies</span>
        </h6>
      </a>
    </div>

    <div class="col-xl-3 col-md-6 margin-bottom-30px">
      <a
        class="d-block padding-30px background-amber box-shadow border-radius-10 hvr-float"
      >
        <h6 class="text-white margin-0px font-weight-400">
          <i
            class="far fa-map text-icon-large margin-bottom-10px opacity-5 d-block"
          ></i>
          <span class="font-2 text-extra-large">6</span>
          <span class="margin-left-10px">Diagnosis pending</span>
          <p></p>
        </h6>
      </a>
    </div>

    <div class="col-xl-3 col-md-6 margin-bottom-30px">
      <a
        class="d-block padding-30px background-red box-shadow border-radius-10 hvr-float"
      >
        <h6 class="text-white margin-0px font-weight-400">
          <i
            class="fas fa-chart-line text-icon-large margin-bottom-10px opacity-5 d-block"
          ></i>
          <span class="font-2 text-extra-large">90%</span>
          <span class="margin-left-10px">Accuracy</span>
          <p></p>
        </h6>
      </a>
    </div>

    <div class="col-12">
      <div
        class="alert alert-info margin-bottom-35px border-radius-10 padding-30px"
      >
        Welcome <strong>Pablo!</strong>
        <hr />
      </div>

      <div class="row">
        <div class="col-12 d-flex justify-content-center">
          <div class="margin-bottom-30px">
            <div
              class="padding-30px background-white border-radius-20 box-shadow"
            >
              <h3>
                <i
                  class="far fa-chart-bar margin-right-10px text-main-color"
                ></i>
                Patients Report
              </h3>
              <hr />
              <div
                id="piechart_3d_"
                style="min-width: 600px; min-height: 250px; display: flex"
              >
                <GChart
                  type="PieChart"
                  version="current"
                  :is3D="true"
                  :data="chartSettings.chartData"
                  :options="chartSettings.chartOptions"
                />
              </div>
              <!--
              <a
                href="#"
                class="btn btn-md border-0 border-radius-10 background-main-color padding-lr-10px text-white margin-tb-5px"
                >View More</a
              >-->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { GChart } from "vue-google-charts";

export default {
  middleware: 'authenticated',
  scrollToTop: true,
  layout: "private",
  transitions: "page",
  components: {
    GChart,
  },
  methods: {
    initialize() {},
  },
  head() {
    return {
      title: `${this.title} | Medical Health Services`,
    };
  },
  data() {
    return {
      title: "Dashboard",
      chartSettings: {
        type: "pieChart",
        chartData: [
          ["Healthy", "Hours per Day"],
          ["Mild Demented", 5],
          ["Moderate Demented", 2],
          ["Very Mild Demented", 2],
          ["Non Demented", 2],
        ],
        settings: {
          packages: ["corechart", "table", "piechart"],
        },
        chartOptions: {
          is3D: true,
          height: 300,
          width: 600,
          chart: {
            title: "Patients Report",
            subtitle: "Healthy - Hours per Day",
          },
        },
      },
    };
  },
  created() {
    //this.initialize();
  },
};
</script>

<style>
</style>
