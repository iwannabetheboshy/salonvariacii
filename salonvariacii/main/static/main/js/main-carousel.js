$(document).ready(function () {
  $('.main-kitchen-carousel').slick({
    slidesToShow: 1.1,
    prevArrow: $('.nav-main-kitchen-carousel-buttton .custom-prev-arrow'),
    nextArrow: $('.nav-main-kitchen-carousel-buttton .custom-next-arrow'),
    autoplaySpeed: 1000,
    //autoplay:true,
    infinite: false,
    dots: true,

    customPaging: function (slider, i) {
      return '<a> 0' +( i + 1 ) + '</a>';
    },

    responsive: [
    {
      breakpoint: 1200,
      settings: {
        slidesToShow: 2.05
      }
    },
    {
      breakpoint: 1000,
      settings: {
        slidesToShow: 1.8
      }
    },
    {
      breakpoint: 900,
      settings: {
        slidesToShow: 1.6
      }
    },
    {
      breakpoint: 800,
      settings: {
        slidesToShow: 1.4
      }
    },
    {
      breakpoint: 700,
      settings: {
        slidesToShow: 1.15
      }
    },
    ]

  });

  $('.slider-catalog-container .slide').first().addClass('large-image');
  $('.slider-catalog-container .slide .content').first().addClass('active');
  $('.slide').click(function () {
    $('.slide').removeClass('large-image');
    $('.slide .content').removeClass('active');
    $(this).addClass('large-image');
    $(this).find('.content').addClass('active');
  });


    $('.slider-catalog-container-mobile .slide-line-mobile').slick({
      slidesToShow: 1.3,
      slidesToScroll: 1,
      arrows: false,
      infinite: false,

      responsive: [
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 1.1
          }
        },
        {
          breakpoint: 900,
          settings: {
            slidesToShow: 1.2
          }
        },
      ]
    });

  $('#project-and-reviews .project-and-reviews-slider').slick({
    slidesToShow: 1.05,
    slidesToScroll: 1,
    prevArrow: $('.nav-project-and-reviews .custom-prev-arrow'),
    nextArrow: $('.nav-project-and-reviews .custom-next-arrow'),
    autoplaySpeed: 1000,
    infinite: false,
    dots: true,

    customPaging: function (slider, i) {
      return '<a> 0' +( i + 1 ) + '</a>';
    },

    responsive: [
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 1.2
        }
      },
      {
        breakpoint: 1000,
        settings: {
          slidesToShow: 1.4
        }
      },
    ]

  });
});



