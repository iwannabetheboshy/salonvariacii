$(document).ready(function(){
    var $slider = $('.project-and-reviews-slider')
    var $proggress = $('.project-and-reviews-slider .progress-fill')
    var $numbers = $('.project-and-reviews-slider .num')
    const interval = 5000;
    
    $('.main-kitchen-carousel').on('init', function(event, slick){
      $numbers.first().addClass('num-active'); 
      $proggress.first().animate({width: '100%'}, interval, 'linear');
    });
  
    $slider.slick({
      slidesToShow: 2,
      slidesToScroll: 1,
      variableWidth: true,
      prevArrow: $('.project-and-reviews-slider .custom-prev-arrow'),
      nextArrow: $('.project-and-reviews-slider .custom-next-arrow'),
      
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