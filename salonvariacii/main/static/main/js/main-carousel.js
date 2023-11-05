$(document).ready(function () {
  $('.main-kitchen-carousel').slick({
    slidesToShow: 1.35,
    prevArrow: $('.nav-main-kitchen-carousel-buttton .custom-prev-arrow'),
    nextArrow: $('.nav-main-kitchen-carousel-buttton .custom-next-arrow'),
    autoplaySpeed: 1000,
    //autoplay:true,
    infinite: false,
    dots: true,

    customPaging: function (slider, i) {
      return '<a> 0' +( i + 1 ) + '</a>';
    },
  });

  $('.slider-catalog-container .slide').first().addClass('large-image');
  $('.slider-catalog-container .slide .content').first().addClass('active');
  $('.slide').click(function () {
    $('.slide').removeClass('large-image');
    $('.slide .content').removeClass('active');
    $(this).addClass('large-image');
    $(this).find('.content').addClass('active');
  });

    if ($(window).width()<=1200) {

    $('.slider-catalog-container-mobile .slide-line-mobile').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: false,
    });
  }

  $('#project-and-reviews .project-and-reviews-slider').slick({
    slidesToShow: 1.05,
    slidesToScroll: 1,
    prevArrow: $('.nav-project-and-reviews .custom-prev-arrow'),
    nextArrow: $('.nav-project-and-reviews .custom-next-arrow'),
    autoplaySpeed: 1000,
    infinite: false,
    dots: true,
     //autoplay:true,
    customPaging: function (slider, i) {
      return '<a> 0' +( i + 1 ) + '</a>';
    },
  });
});