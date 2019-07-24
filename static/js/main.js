$(document).ready(function() {
    $(".dropdown-trigger").dropdown();
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $( "#progress" ).slideToggle('slow');
    $('.fixed-action-btn').floatingActionButton();
 });
 $('body').on('touchstart', function() {});
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
// USED IN PERSONAL_INTERVIEW.HTML
//
////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////
//
// USED FOR ALL PAGE HEADINGS
//
////////////////////////////////////////////////////////////
;(function($, win) {
    $.fn.inViewport = function(cb) {
      return this.each(function(i,el) {
        function visPx(){
          var elH = $(el).outerHeight(),
              H = $(win).height(),
              r = el.getBoundingClientRect(), t=r.top, b=r.bottom;
          return cb.call(el, Math.max(0, t>0? Math.min(elH, H-t) : (b<H?b:H)));  
        }
        visPx();
        $(win).on("resize scroll", visPx);
      });
    };
  }(jQuery, window));
  
  $("h3 span").inViewport(function(px){
    $(this).toggleClass("animateLine", !!px);
  });

