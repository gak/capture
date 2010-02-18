$(document).ready(function() {

  $.plot($("#placeholder"), workdata, {

      xaxis: {
        mode: "time",
        timeformat: "%d-%m-%y",
      },

  });
});
