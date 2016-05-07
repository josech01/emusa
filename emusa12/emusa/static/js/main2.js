$(document).ready(function() {
  //change the integers below to match the height of your upper dive, which I called
  //banner.  Just add a 1 to the last number.  console.log($(window).scrollTop())
  //to figure out what the scroll position is when exactly you want to fix the nav
  //bar or div or whatever.  I stuck in the console.log for you.  Just remove when
  //you know the position.
  $(".button-collapse").sideNav();

  $(document).ready(function(){
      $('.parallax').parallax();
    });

  $('a[href^="#"]').click(function() {
    
    var target = $(this).attr( "href");
    console.log(target);
    if( target.length ) {
      event.preventDefault();
      if ($(window).width() < 600) {
        $('html, body').animate({
              scrollTop: $(target).offset().top - 60
          }, 1000);
      }
      else {
        $('html, body').animate({
              scrollTop: $(target).offset().top - 215
          }, 1000);
      }
    }
  });
  
});