$(document).ready(function(){

  $("#exchange_rate_form").submit(function(func){
    func.preventDefault();

    $.ajax({
      url: $(this).attr('action'),
      type: $(this).attr('method'),
      data: $(this).serialize(),

      success: function(json){
        $("head").append(json.er_script);
        $('#exchange_rates_plot').append(json.er_div);
        //alert(json.er_div);
      }

    })
  });
});
