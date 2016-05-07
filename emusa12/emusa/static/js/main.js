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

$(document).ready(function() {
    $('.holas').hide();
});


$(document).ready(function() {
  $('#chocolate').click(function(){
    $('#textochocolate').show();
    $('#imagenchocolate').show();
    $('#textogalleta').hide();
    $('#textosnacks').hide();
    $('#textogolosinas').hide();
    $('#textocereales').hide();
    $('#textopastas').hide();
    $('#textoaceite').hide();
    $('#textosalsas').hide();
    $('#textogranos').hide();
    $('#textopolvos').hide();
    $('#textodetergente').hide();
    $('#textoaseo').hide();
    $('#textocongelados').hide();
    $('#textomicroondables').hide();
    $('#textorefrigerados').hide();
    $('#imagengalleta').hide();
    $('#imagensnacks').hide();
    $('#imagengolosinas').hide();
    $('#imagencereales').hide();
    $('#imagenpastas').hide();
    $('#imagenaceite').hide();
    $('#imagensalsas').hide();
    $('#imagengranos').hide();
    $('#imagenpolvos').hide();
    $('#imagendetergente').hide();
    $('#imagenaseo').hide();
    $('#imagencongelados').hide();
    $('#imagenmicroondables').hide();
    $('#imagenrefrigerados').hide();
  })
});

$(document).ready(function() {
  $('#galleta').click(function(){
    $('#textogalleta').show();
    $('#imagengalleta').show();
    $('#textochocolate').hide();
    $('#textosnacks').hide();
    $('#textogolosinas').hide();
    $('#textocereales').hide();
    $('#textopastas').hide();
    $('#textoaceite').hide();
    $('#textosalsas').hide();
    $('#textogranos').hide();
    $('#textopolvos').hide();
    $('#textodetergente').hide();
    $('#textoaseo').hide();
    $('#textocongelados').hide();
    $('#textomicroondables').hide();
    $('#textorefrigerados').hide();
    $('#imagenchocolate').hide();
    $('#imagensnacks').hide();
    $('#imagengolosinas').hide();
    $('#imagencereales').hide();
    $('#imagenpastas').hide();
    $('#imagenaceite').hide();
    $('#imagensalsas').hide();
    $('#imagengranos').hide();
    $('#imagenpolvos').hide();
    $('#imagendetergente').hide();
    $('#imagenaseo').hide();
    $('#imagencongelados').hide();
    $('#imagenmicroondables').hide();
    $('#imagenrefrigerados').hide();
  })
});

$(document).ready(function() {
  $('#snacks').click(function(){
    $('#textosnacks').show();
    $('#imagensnacks').show();
    $('#textogalleta').hide();
    $('#textochocolate').hide();
    $('#textogolosinas').hide();
    $('#textocereales').hide();
    $('#textopastas').hide();
    $('#textoaceite').hide();
    $('#textosalsas').hide();
    $('#textogranos').hide();
    $('#textopolvos').hide();
    $('#textodetergente').hide();
    $('#textoaseo').hide();
    $('#textocongelados').hide();
    $('#textomicroondables').hide();
    $('#textorefrigerados').hide();
    $('#imagengalleta').hide();
    $('#imagenchocolate').hide();
    $('#imagengolosinas').hide();
    $('#imagencereales').hide();
    $('#imagenpastas').hide();
    $('#imagenaceite').hide();
    $('#imagensalsas').hide();
    $('#imagengranos').hide();
    $('#imagenpolvos').hide();
    $('#imagendetergente').hide();
    $('#imagenaseo').hide();
    $('#imagencongelados').hide();
    $('#imagenmicroondables').hide();
    $('#imagenrefrigerados').hide();
  })
});

$(document).ready(function() {
  $('#aceite').click(function(){
    $('#textoaceite').show();
    $('#imagenaceite').show();
    $('#textogalleta').hide();
    $('#textochocolate').hide();
    $('#textogolosinas').hide();
    $('#textocereales').hide();
    $('#textopastas').hide();
    $('#textosnacks').hide();
    $('#textosalsas').hide();
    $('#textogranos').hide();
    $('#textopolvos').hide();
    $('#textodetergente').hide();
    $('#textoaseo').hide();
    $('#textocongelados').hide();
    $('#textomicroondables').hide();
    $('#textorefrigerados').hide();
    $('#imagengalleta').hide();
    $('#imagenchocolate').hide();
    $('#imagengolosinas').hide();
    $('#imagencereales').hide();
    $('#imagenpastas').hide();
    $('#imagensnacks').hide();
    $('#imagensalsas').hide();
    $('#imagengranos').hide();
    $('#imagenpolvos').hide();
    $('#imagendetergente').hide();
    $('#imagenaseo').hide();
    $('#imagencongelados').hide();
    $('#imagenmicroondables').hide();
    $('#imagenrefrigerados').hide();
  })
});

$(document).ready(function() {
  $('#salsas').click(function(){
    $('#textosalsas').show();
    $('#imagensalsas').show();
    $('#textogalleta').hide();
    $('#textochocolate').hide();
    $('#textogolosinas').hide();
    $('#textocereales').hide();
    $('#textopastas').hide();
    $('#textosnacks').hide();
    $('#textoaceite').hide();
    $('#textogranos').hide();
    $('#textopolvos').hide();
    $('#textodetergente').hide();
    $('#textoaseo').hide();
    $('#textocongelados').hide();
    $('#textomicroondables').hide();
    $('#textorefrigerados').hide();
    $('#imagengalleta').hide();
    $('#imagenchocolate').hide();
    $('#imagengolosinas').hide();
    $('#imagencereales').hide();
    $('#imagenpastas').hide();
    $('#imagensnacks').hide();
    $('#imagenaceite').hide();
    $('#imagengranos').hide();
    $('#imagenpolvos').hide();
    $('#imagendetergente').hide();
    $('#imagenaseo').hide();
    $('#imagencongelados').hide();
    $('#imagenmicroondables').hide();
    $('#imagenrefrigerados').hide();
  })
});

$(document).ready(function() {
  $('#golosinas').click(function(){
    $('#textogolosinas').show();
    $('#imagengolosinas').show();
    $('#textogalleta').hide();
    $('#textochocolate').hide();
    $('#textosalsas').hide();
    $('#textocereales').hide();
    $('#textopastas').hide();
    $('#textosnacks').hide();
    $('#textoaceite').hide();
    $('#textogranos').hide();
    $('#textopolvos').hide();
    $('#textodetergente').hide();
    $('#textoaseo').hide();
    $('#textocongelados').hide();
    $('#textomicroondables').hide();
    $('#textorefrigerados').hide();
    $('#imagengalleta').hide();
    $('#imagenchocolate').hide();
    $('#imagensalsas').hide();
    $('#imagencereales').hide();
    $('#imagenpastas').hide();
    $('#imagensnacks').hide();
    $('#imagenaceite').hide();
    $('#imagengranos').hide();
    $('#imagenpolvos').hide();
    $('#imagendetergente').hide();
    $('#imagenaseo').hide();
    $('#imagencongelados').hide();
    $('#imagenmicroondables').hide();
    $('#imagenrefrigerados').hide();
  })
});

$(document).ready(function() {
  $('#cereales').click(function(){
    $('#textocereales').show();
    $('#imagencereales').show();
    $('#textogalleta').hide();
    $('#textochocolate').hide();
    $('#textogolosinas').hide();
    $('#textosalsas').hide();
    $('#textopastas').hide();
    $('#textosnacks').hide();
    $('#textoaceite').hide();
    $('#textogranos').hide();
    $('#textopolvos').hide();
    $('#textodetergente').hide();
    $('#textoaseo').hide();
    $('#textocongelados').hide();
    $('#textomicroondables').hide();
    $('#textorefrigerados').hide();
    $('#imagengalleta').hide();
    $('#imagenchocolate').hide();
    $('#imagengolosinas').hide();
    $('#imagensalsas').hide();
    $('#imagenpastas').hide();
    $('#imagensnacks').hide();
    $('#imagenaceite').hide();
    $('#imagengranos').hide();
    $('#imagenpolvos').hide();
    $('#imagendetergente').hide();
    $('#imagenaseo').hide();
    $('#imagencongelados').hide();
    $('#imagenmicroondables').hide();
    $('#imagenrefrigerados').hide();
  })
});

$(document).ready(function() {
  $('#pastas').click(function(){
    $('#textopastas').show();
    $('#imagenpastas').show();
    $('#textogalleta').hide();
    $('#textochocolate').hide();
    $('#textogolosinas').hide();
    $('#textosalsas').hide();
    $('#textocereales').hide();
    $('#textosnacks').hide();
    $('#textoaceite').hide();
    $('#textogranos').hide();
    $('#textopolvos').hide();
    $('#textodetergente').hide();
    $('#textoaseo').hide();
    $('#textocongelados').hide();
    $('#textomicroondables').hide();
    $('#textorefrigerados').hide();
    $('#imagengalleta').hide();
    $('#imagenchocolate').hide();
    $('#imagengolosinas').hide();
    $('#imagensalsas').hide();
    $('#imagencereales').hide();
    $('#imagensnacks').hide();
    $('#imagenaceite').hide();
    $('#imagengranos').hide();
    $('#imagenpolvos').hide();
    $('#imagendetergente').hide();
    $('#imagenaseo').hide();
    $('#imagencongelados').hide();
    $('#imagenmicroondables').hide();
    $('#imagenrefrigerados').hide();
  })
});

$(document).ready(function() {
  $('#granos').click(function(){
    $('#textogranos').show();
    $('#imagengranos').show();
    $('#textogalleta').hide();
    $('#textochocolate').hide();
    $('#textogolosinas').hide();
    $('#textosalsas').hide();
    $('#textopastas').hide();
    $('#textosnacks').hide();
    $('#textoaceite').hide();
    $('#textocereales').hide();
    $('#textopolvos').hide();
    $('#textodetergente').hide();
    $('#textoaseo').hide();
    $('#textocongelados').hide();
    $('#textomicroondables').hide();
    $('#textorefrigerados').hide();
    $('#imagengalleta').hide();
    $('#imagenchocolate').hide();
    $('#imagengolosinas').hide();
    $('#imagensalsas').hide();
    $('#imagenpastas').hide();
    $('#imagensnacks').hide();
    $('#imagenaceite').hide();
    $('#imagencereales').hide();
    $('#imagenpolvos').hide();
    $('#imagendetergente').hide();
    $('#imagenaseo').hide();
    $('#imagencongelados').hide();
    $('#imagenmicroondables').hide();
    $('#imagenrefrigerados').hide();
  })
});

$(document).ready(function() {
  $('#polvos').click(function(){
    $('#textopolvos').show();
    $('#imagenpolvos').show();
    $('#textogalleta').hide();
    $('#textochocolate').hide();
    $('#textogolosinas').hide();
    $('#textosalsas').hide();
    $('#textopastas').hide();
    $('#textosnacks').hide();
    $('#textoaceite').hide();
    $('#textocereales').hide();
    $('#textogranos').hide();
    $('#textodetergente').hide();
    $('#textoaseo').hide();
    $('#textocongelados').hide();
    $('#textomicroondables').hide();
    $('#textorefrigerados').hide();
    $('#imagengalleta').hide();
    $('#imagenchocolate').hide();
    $('#imagengolosinas').hide();
    $('#imagensalsas').hide();
    $('#imagenpastas').hide();
    $('#imagensnacks').hide();
    $('#imagenaceite').hide();
    $('#imagencereales').hide();
    $('#imagengranos').hide();
    $('#imagendetergente').hide();
    $('#imagenaseo').hide();
    $('#imagencongelados').hide();
    $('#imagenmicroondables').hide();
    $('#imagenrefrigerados').hide();
  })
});

$(document).ready(function() {
  $('#detergente').click(function(){
    $('#textodetergente').show();
    $('#imagendetergente').show();
    $('#textogalleta').hide();
    $('#textochocolate').hide();
    $('#textogolosinas').hide();
    $('#textosalsas').hide();
    $('#textopastas').hide();
    $('#textosnacks').hide();
    $('#textoaceite').hide();
    $('#textocereales').hide();
    $('#textogranos').hide();
    $('#textopolvos').hide();
    $('#textoaseo').hide();
    $('#textocongelados').hide();
    $('#textomicroondables').hide();
    $('#textorefrigerados').hide();
    $('#imagengalleta').hide();
    $('#imagenchocolate').hide();
    $('#imagengolosinas').hide();
    $('#imagensalsas').hide();
    $('#imagenpastas').hide();
    $('#imagensnacks').hide();
    $('#imagenaceite').hide();
    $('#imagencereales').hide();
    $('#imagengranos').hide();
    $('#imagenpolvos').hide();
    $('#imagenaseo').hide();
    $('#imagencongelados').hide();
    $('#imagenmicroondables').hide();
    $('#imagenrefrigerados').hide();
  })
});

$(document).ready(function() {
  $('#aseo').click(function(){
    $('#textoaseo').show();
    $('#imagenaseo').show();
    $('#textogalleta').hide();
    $('#textochocolate').hide();
    $('#textogolosinas').hide();
    $('#textosalsas').hide();
    $('#textopastas').hide();
    $('#textosnacks').hide();
    $('#textoaceite').hide();
    $('#textocereales').hide();
    $('#textogranos').hide();
    $('#textodetergente').hide();
    $('#textopolvos').hide();
    $('#textocongelados').hide();
    $('#textomicroondables').hide();
    $('#textorefrigerados').hide();
    $('#imagengalleta').hide();
    $('#imagenchocolate').hide();
    $('#imagengolosinas').hide();
    $('#imagensalsas').hide();
    $('#imagenpastas').hide();
    $('#imagensnacks').hide();
    $('#imagenaceite').hide();
    $('#imagencereales').hide();
    $('#imagengranos').hide();
    $('#imagendetergente').hide();
    $('#imagenpolvos').hide();
    $('#imagencongelados').hide();
    $('#imagenmicroondables').hide();
    $('#imagenrefrigerados').hide();
  })
});

$(document).ready(function() {
  $('#congelados').click(function(){
    $('#textocongelados').show();
    $('#imagencongelados').show();
    $('#textogalleta').hide();
    $('#textochocolate').hide();
    $('#textogolosinas').hide();
    $('#textosalsas').hide();
    $('#textopastas').hide();
    $('#textosnacks').hide();
    $('#textoaceite').hide();
    $('#textocereales').hide();
    $('#textogranos').hide();
    $('#textodetergente').hide();
    $('#textopolvos').hide();
    $('#textoaseo').hide();
    $('#textomicroondables').hide();
    $('#textorefrigerados').hide();
    $('#imagengalleta').hide();
    $('#imagenchocolate').hide();
    $('#imagengolosinas').hide();
    $('#imagensalsas').hide();
    $('#imagenpastas').hide();
    $('#imagensnacks').hide();
    $('#imagenaceite').hide();
    $('#imagencereales').hide();
    $('#imagengranos').hide();
    $('#imagendetergente').hide();
    $('#imagenpolvos').hide();
    $('#imagenaseo').hide();
    $('#imagenmicroondables').hide();
    $('#imagenrefrigerados').hide();
  })
});

$(document).ready(function() {
  $('#microondables').click(function(){
    $('#textomicroondables').show();
    $('#imagenmicroondables').show();
    $('#textogalleta').hide();
    $('#textochocolate').hide();
    $('#textogolosinas').hide();
    $('#textosalsas').hide();
    $('#textopastas').hide();
    $('#textosnacks').hide();
    $('#textoaceite').hide();
    $('#textocereales').hide();
    $('#textogranos').hide();
    $('#textodetergente').hide();
    $('#textopolvos').hide();
    $('#textocongelados').hide();
    $('#textoaseo').hide();
    $('#textorefrigerados').hide();
    $('#imagengalleta').hide();
    $('#imagenchocolate').hide();
    $('#imagengolosinas').hide();
    $('#imagensalsas').hide();
    $('#imagenpastas').hide();
    $('#imagensnacks').hide();
    $('#imagenaceite').hide();
    $('#imagencereales').hide();
    $('#imagengranos').hide();
    $('#imagendetergente').hide();
    $('#imagenpolvos').hide();
    $('#imagencongelados').hide();
    $('#imagenaseo').hide();
    $('#imagenrefrigerados').hide();
  })
});

$(document).ready(function() {
  $('#refrigerados').click(function(){
    $('#textorefrigerados').show();
    $('#imagenrefrigerados').show();
    $('#textogalleta').hide();
    $('#textochocolate').hide();
    $('#textogolosinas').hide();
    $('#textosalsas').hide();
    $('#textopastas').hide();
    $('#textosnacks').hide();
    $('#textoaceite').hide();
    $('#textocereales').hide();
    $('#textogranos').hide();
    $('#textodetergente').hide();
    $('#textopolvos').hide();
    $('#textocongelados').hide();
    $('#textomicroondables').hide();
    $('#textoaseo').hide();
    $('#imagengalleta').hide();
    $('#imagenchocolate').hide();
    $('#imagengolosinas').hide();
    $('#imagensalsas').hide();
    $('#imagenpastas').hide();
    $('#imagensnacks').hide();
    $('#imagenaceite').hide();
    $('#imagencereales').hide();
    $('#imagengranos').hide();
    $('#imagendetergente').hide();
    $('#imagenpolvos').hide();
    $('#imagencongelados').hide();
    $('#imagenmicroondables').hide();
    $('#imagenaseo').hide();
  })
});

$(document).ready(function(){
    $('.slider').slider({full_width: true});
});

$(document).ready(function() {
    $('#brasil').hide();
    $('#guatemala').hide();
});

$(document).ready(function() {
  $('#textoperu').click(function(){
    $('#peru').show();
    $('#brasil').hide();
    $('#guatemala').hide();
  })
});

$(document).ready(function() {
  $('#textobrasil').click(function(){
    $('#brasil').show();
    $('#peru').hide();
    $('#guatemala').hide();
  })
});
$(document).ready(function() {
  $('#textoguatemala').click(function(){
    $('#guatemala').show();
    $('#peru').hide();
    $('#brasil').hide();
  })
});
