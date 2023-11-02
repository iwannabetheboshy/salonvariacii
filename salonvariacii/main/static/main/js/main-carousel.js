$(document).ready(function(){
  $('.slider-catalog-container .slide img').first().addClass('large-image');
  $('.slider-catalog-container .slide .content').first().addClass('active');
    $('.slide').click(function() {
        $('.slide img').removeClass('large-image');
      // Добавляем класс large-image только к изображению, на которое кликнули
      $('.slide .content').removeClass('active');
      $(this).find('img').addClass('large-image');
      $(this).find('.content').addClass('active');
    });


    var $slider_kitchen = $('.main-kitchen-carousel')
    var $proggress_kitchen = $('.nav-main-kitchen-carousel .progress-fill')
    var $numbers_kitchen = $('.nav-main-kitchen-carousel .num')
    const interval = 5000;
    
    $slider_kitchen.on('init', function(event, slick){
      $numbers_kitchen.first().addClass('num-active'); 
      $proggress_kitchen.first().animate({width: '100%'}, interval, 'linear');
    });
  
    $slider_kitchen.slick({
      slidesToShow: 1.4,
      slidesToScroll: 1,
      prevArrow: $('.nav-main-kitchen-carousel-buttton .custom-prev-arrow'),
      nextArrow: $('.nav-main-kitchen-carousel-buttton .custom-next-arrow'),
      autoplay: true,
      autoplaySpeed: interval,
      infinite: false, 
      edgeFriction: 0.2,
    });
  
    $slider_kitchen.on('beforeChange', function(event, slick, currentSlide, nextSlide){
      $numbers_kitchen.removeClass('num-active');
      $numbers_kitchen.eq(nextSlide).addClass('num-active'); 
  
      var lineToAnimate_kitchen = $proggress_kitchen.eq(nextSlide);
      $proggress_kitchen.eq(currentSlide).css('width', '0');
  
      lineToAnimate_kitchen.animate({ width: '100%'}, interval, 'linear');;
    });



    var $slider_review = $('#project-and-reviews .project-and-reviews-slider')
    var $proggress_review = $('#project-and-reviews .project-and-reviews-nav .progress-fill')
    var $numbers_review = $('#project-and-reviews .project-and-reviews-nav .num')


    
    $slider_review.on('init', function(event, slick){
      $numbers_review.first().addClass('num-active'); 
      $proggress_review.first().animate({width: '100%'}, interval, 'linear');
    });
  
    $slider_review.slick({
      slidesToShow: 1.05,
      slidesToScroll: 1,
      prevArrow: $('.project-and-reviews-slider .custom-prev-arrow'),
      nextArrow: $('.project-and-reviews-slider .custom-next-arrow'),
      autoplay: true,
      autoplaySpeed: interval,
      infinite: false, 
      edgeFriction: 0.2,
    });
  
    $slider_review.on('beforeChange', function(event, slick, currentSlide, nextSlide){
      $numbers_review.removeClass('num-active');
      $numbers_review.eq(nextSlide).addClass('num-active'); 
  
      var lineToAnimate = $proggress_review.eq(nextSlide);
      $proggress_review.eq(currentSlide).css('width', '0');
  
      // Анимируем линию (увеличиваем ее ширину до 100%)
      lineToAnimate.animate({ width: '100%'}, interval, 'linear');;
    });

  });