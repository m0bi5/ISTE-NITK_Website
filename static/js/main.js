$(document).ready(function() {
    $(".dropdown-trigger").dropdown();
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $( "#progress" ).slideToggle('slow');
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
$("#show_about").click(function(){
    $( "#details_form" ).slideToggle('slow');
    $( "#about_sigs" ).slideToggle('slow');
})

$("#show_form").click(function(){
    $( "#details_form" ).slideToggle('slow');
    $( "#about_sigs" ).slideToggle('slow');
})

////////////////////////////////////////////////////////////
//
// USED IN APPLICANT_PROGRESS.HTML
//
////////////////////////////////////////////////////////////
