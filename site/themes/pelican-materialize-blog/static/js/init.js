(function($){
  $(function(){
    $('.button-collapse').sideNav();
    $('.dropdown-button').dropdown();
    $('.dropdown-taglist').dropdown({
      hover: true,
      constrain_width: false
    });
    $('.materialboxed').materialbox();
  });
})(jQuery);
