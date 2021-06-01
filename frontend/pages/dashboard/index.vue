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

          <span class="font-2 text-extra-large">{{ indicators.total }}</span>
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
          <span class="font-2 text-extra-large">{{
            indicators.pathologies
          }}</span>
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
          <span class="font-2 text-extra-large">{{ indicators.pendding }}</span>
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
          <span class="font-2 text-extra-large"
            >{{ indicators.accuracy }}%</span
          >
          <span class="margin-left-10px">Accuracy</span>
          <p></p>
        </h6>
      </a>
    </div>

    <div class="col-12">
      <div
        class="alert alert-info margin-bottom-35px border-radius-10 padding-30px"
      >
        Welcome
        <strong
          >{{ this.user.attributes.first_name }}
          {{ this.user.attributes.last_name }}!</strong
        >
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
                  v-if="this.reports.length"
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
import { mapState } from "vuex";
import { GChart } from "vue-google-charts";

export default {
  middleware: "authenticated",
  scrollToTop: true,
  layout: "private",
  transitions: "page",
  components: {
    GChart,
  },
  computed: {
    ...mapState({
      user: (state) => state.auth.user,
    }),
  },
  methods: {
    init() {
      console.log(this.user);
    },
    initialize() {},
  },
  async fetch() {
    this.reports = await this.$axios.get("patients/report").then((res) => {
      return res.data.data;
    });

    if (this.reports.length > 0) {
      this.reports.forEach((report) => {
        switch (report.attributes.indicator) {
          case "total":
            this.indicators.total = report.attributes.count;
            break;

          case "pendding":
            this.indicators.pendding = report.attributes.count;
            break;

          case "t":
            this.indicators.pathologies = report.attributes.count;
            break;

          default:
            let index = this.listTypes.indexOf(report.attributes.indicator);
            if (index > -1) {
              this.chartSettings.chartData[index + 1][1] = report.attributes.count;
            }
            break;
        }
      });

      console.log("reports:", this.reports);
      console.log("chartData: ", this.chartSettings.chartData);
    }
  },
  head() {
    return {
      title: `${this.title} | Medical Health Services`,
    };
  },
  data() {
    return {
      title: "Dashboard",
      reports: [],
      listTypes: [
        "NonDemented",
        "MildDemented",
        "ModerateDemented",
        "VeryMildDemented",
      ],
      indicators: {
        total: 0,
        pathologies: 0,
        pendding: 0,
        accuracy: 90,
      },
      chartSettings: {
        type: "pieChart",
        chartData: [
          ["Healthy", "Hours per Day"],
          ["Non Demented", 0],
          ["Mild Demented", 0],
          ["Moderate Demented", 0],
          ["Very Mild Demented", 0],
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
  mounted() {
    this.init();
  },
  watch: {
    user(data) {
      console.log("user: ", data);
    },
  },
};
</script>

<style>
</style>
