$(document).ready(function() {

  settings = {
    xaxis: {
      mode: "time",
      timeformat: "%d-%m-%y",
    }
  }

  $.plot($("#work"), workdata, settings);
  $.plot($("#commute"), commutedata, settings);

});
