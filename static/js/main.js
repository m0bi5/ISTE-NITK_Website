$(document).ready(function() {
    $(".dropdown-trigger").dropdown();
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
    $('select').formSelect();
 });

 ////////////////////////////////////////////////////////////
//
// USED IN LOGIN.HTML
//
////////////////////////////////////////////////////////////

 $('#alert_close').click(function(){
    $( "#alert_box" ).fadeOut( "slow", function() {});
});


////////////////////////////////////////////////////////////
//
// USED IN APPLICANT_DEETS.HTML
//
////////////////////////////////////////////////////////////

$('#id_sig_choices').on('change', function() {
    console.log($('.selected').length)
   if($('.selected').length == 3) {
       console.log($('.selected')[0])
        $($('.selected')[0]).removeClass('selected');
   }
});