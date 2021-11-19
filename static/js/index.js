$("#process_input").click(function(){
    var text = $("#editor").val();
    $.ajax({
      url: "/suggestions",
      type: "get",
      data: {jsdata: text},
      success: function(response) {
        $("#place_for_suggestions").html(response);
      },
      error: function(xhr) {
        //Do Something to handle error
      }
    });
});

$("#process_input_1").click(function(){
    var text = $("#editor").val();
    $.ajax({
      url: "/suggestions_1",
      type: "get",
      data: {jsdata: text},
      success: function(response) {
        $("#place_for_suggestions_1").html(response);
      },
      error: function(xhr) {
        //Do Something to handle error
      }
    });
});
