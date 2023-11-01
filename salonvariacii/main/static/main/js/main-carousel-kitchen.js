$(document).ready(function(){
  var $slider = $('.main-kitchen-carousel')
  var $proggress = $('.main-kitchen-carousel .progress-fill')
  var $numbers = $('.main-kitchen-carousel .num')
  const interval = 5000;
  
  $('.main-kitchen-carousel').on('init', function(event, slick){
    $numbers.first().addClass('num-active'); 
    $proggress.first().animate({width: '100%'}, interval, 'linear');
  });

  $slider.slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    variableWidth: true,
    prevArrow: $('.nav-main-kitchen-carousel-buttton .custom-prev-arrow'),
    nextArrow: $('.nav-main-kitchen-carousel-buttton .custom-next-arrow'),
    autoplay: true,
    autoplaySpeed: interval,
    infinite: false, 
    edgeFriction: 0.2,
  });

  $slider.on('beforeChange', function(event, slick, currentSlide, nextSlide){
    $numbers.removeClass('num-active');
    $numbers.eq(nextSlide).addClass('num-active'); 

    var lineToAnimate = $proggress.eq(nextSlide);
    $proggress.eq(currentSlide).css('width', '0');

    // Анимируем линию (увеличиваем ее ширину до 100%)
    lineToAnimate.animate({ width: '100%'}, interval, 'linear');;
  });
});
