<template>
  <div id="add-patient">
    <div class="row margin-tb-90px margin-lr-10px sm-mrl-0px">
      <!-- Page Title -->
      <div
        id="page-title"
        class="padding-30px background-white full-width box-shadow"
      >
        <div class="container">
          <ol class="breadcrumb opacity-5">
            <li><nuxt-link to="/dashboard">Home</nuxt-link></li>
            <li><nuxt-link to="/patients">patients</nuxt-link></li>
            <li class="active">Evaluate Patient</li>
          </ol>
          <h1 class="font-weight-300">Evaluate New Patient</h1>
          <br />
          <div class="col-lg-8"></div>
        </div>
      </div>
    </div>

    <!-- // Page Title -->
    <div class="">
      <form id="regForm">
        <!-- One "tab" for each step in the form: -->
        <div class="tab">
          Name:
          <p>
            <input
              placeholder="First name..."
              oninput="this.className = ''"
              name="fname"
            />
          </p>
          <p>
            <input
              placeholder="Last name..."
              oninput="this.className = ''"
              name="lname"
            />
          </p>
        </div>
        <div class="tab">
          Date of Birth:
          <p><input id="date" type="date" /></p>
        </div>
        <div class="tab">
          Upload patient's MRI image:
          <p><input type="file" id="myFile" name="filename" /></p>
        </div>
        <div style="overflow: auto">
          <div style="float: right">
            <button type="button" id="prevBtn" onclick="nextPrev(-1)">
              Previous
            </button>
            <button type="button" id="nextBtn" onclick="nextPrev(1)">
              Next
            </button>
          </div>
        </div>
        <!-- Circles which indicates the steps of the form: -->
        <div style="text-align: center; margin-top: 40px">
          <span class="step"></span>
          <span class="step"></span>
          <span class="step"></span>
          <span class="step"></span>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  layout: "private",
  transitions: "page",
  methods: {
    initialize() {
      var currentTab = 0; // Current tab is set to be the first tab (0)
      showTab(currentTab); // Display the current tab

      function showTab(n) {
        // This function will display the specified tab of the form...
        var x = document.getElementsByClassName("tab");
        let btn = document.getElementById("prevBtn");
        let btnNext = document.getElementById("nextBtn");

        if (x[n]) {
          x[n].style.display = "block";
        }

        if (btn) {
          if (n == 0) {
            document.getElementById("prevBtn").style.display = "none";
          } else {
            document.getElementById("prevBtn").style.display = "inline";
          }
        }

        if (btnNext) {
          if (n == x.length - 1) {
            document.getElementById("nextBtn").innerHTML = "Submit";
          } else {
            document.getElementById("nextBtn").innerHTML = "Next";
          }
        }

        //... and run a function that will display the correct step indicator:
        fixStepIndicator(n);
      }

      function nextPrev(n) {
        // This function will figure out which tab to display
        var x = document.getElementsByClassName("tab");
        // Exit the function if any field in the current tab is invalid:
        if (n == 1 && !validateForm()) return false;
        // Hide the current tab:
        x[currentTab].style.display = "none";
        // Increase or decrease the current tab by 1:
        currentTab = currentTab + n;
        // if you have reached the end of the form...
        if (currentTab >= x.length) {
          // ... the form gets submitted:
          document.getElementById("regForm").submit();
          return false;
        }
        // Otherwise, display the correct tab:
        showTab(currentTab);
      }

      function validateForm() {
        // This function deals with validation of the form fields
        var x,
          y,
          i,
          valid = true;
        x = document.getElementsByClassName("tab");
        y = x[currentTab].getElementsByTagName("input");
        // A loop that checks every input field in the current tab:
        for (i = 0; i < y.length; i++) {
          // If a field is empty...
          if (y[i].value == "") {
            // add an "invalid" class to the field:
            y[i].className += " invalid";
            // and set the current valid status to false
            valid = false;
          }
        }
        // If the valid status is true, mark the step as finished and valid:
        if (valid) {
          document.getElementsByClassName("step")[currentTab].className +=
            " finish";
        }
        return valid; // return the valid status
      }

      function fixStepIndicator(n) {
        // This function removes the "active" class of all steps...
        var i,
          x = document.getElementsByClassName("step");

        for (i = 0; i < x.length; i++) {
          if(x[i]){
            x[i].className = x[i].className.replace(" active", "");
          }
        }
        //... and adds the "active" class on the current step:
        if(x[n]){
          x[n].className += " active";
        }
      }
    },
  },
  head() {
    return {
      title: `${this.title} | Medical Health Services`,
    };
  },
  data() {
    return {
      title: "Dashboard",
    };
  },
  created() {
    this.initialize();
  },
};
</script>

<style lang="scss" scoped>
#add-patient {
  * {
    box-sizing: border-box;
  }

  body {
    background-color: #f1f1f1;
  }

  #regForm {
    background-color: #ffffff;
    margin: 100px auto;
    font-family: Raleway;
    padding: 40px;
    width: 70%;
    min-width: 300px;
  }

  h1 {
    text-align: center;
  }

  input {
    padding: 10px;
    width: 100%;
    font-size: 17px;
    font-family: Raleway;
    border: 1px solid #aaaaaa;
  }

  /* Mark input boxes that gets an error on validation: */
  input.invalid {
    background-color: #ffdddd;
  }

  /* Hide all steps by default: */
  .tab {
    display: none;
  }

  button {
    background-color: #2097e6;
    color: #ffffff;
    border: none;
    padding: 10px 20px;
    font-size: 17px;
    font-family: Raleway;
    cursor: pointer;
  }

  button:hover {
    opacity: 0.8;
  }

  #prevBtn {
    background-color: #bbbbbb;
  }

  /* Make circles that indicate the steps of the form: */
  .step {
    height: 15px;
    width: 15px;
    margin: 0 2px;
    background-color: #bbbbbb;
    border: none;
    border-radius: 50%;
    display: inline-block;
    opacity: 0.5;
  }

  .step.active {
    opacity: 1;
  }

  /* Mark the steps that are finished and valid: */
  .step.finish {
    background-color: #4caf50;
  }
}
</style>
