$(document).ready(function () {
  slideCount = $('.main-kitchen-carousel-slide').length;

  $('.main-kitchen-carousel').slick({
    slidesToShow: 1,
    prevArrow: $('.nav-main-kitchen-carousel-buttton .custom-prev-arrow'),
    nextArrow: $('.nav-main-kitchen-carousel-buttton .custom-next-arrow'),
    autoplaySpeed: 5000,
    autoplay: true,
    infinite: true,
    dots: false,

    responsive: [
      {
        breakpoint: 552,
        settings: {
          dots: true
        }
      },
    ]
  });

  $('.main-kitchen-carousel-sliderCount .sliderCount').html(slideCount);
  $('.main-kitchen-carousel-sliderCount .currentSlide').html('01');

  $(".main-kitchen-carousel").on("afterChange", function (event, slick, currentSlide, nextSlide) {
    let currentSlider = $('.main-kitchen-carousel').slick('slickCurrentSlide') + 1;
    if (currentSlider >= 10) {
      $('.main-kitchen-carousel-sliderCount .currentSlide').html(currentSlider);
    } else {
      $('.main-kitchen-carousel-sliderCount .currentSlide').html('0' + currentSlider);
    }
  });
  $('#project-and-reviews .project-and-reviews-slider').slick({
    slidesToShow: 1.05,
    slidesToScroll: 1,
    prevArrow: $('.nav-project-and-reviews .custom-prev-arrow'),
    nextArrow: $('.nav-project-and-reviews .custom-next-arrow'),
    autoplaySpeed: 2500,
    autoplay: true,
    infinite: false,
    dots: true,

    customPaging: function (slider, i) {
      return '<span> 0' + (i + 1) + '</span>';
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
          slidesToShow: 1.2
        }
      },
      {
        breakpoint: 800,
        settings: {
          slidesToShow: 1.1
        }
      },
    ]
  });
  $('.slider-catalog-container .slide').first().addClass('large-image');
  $('.slider-catalog-container .slide .content').first().addClass('active');
  $('.slider-catalog-container .slide').click(function () {
    $('.slider-catalog-container .slide').removeClass('large-image');
    $('.slider-catalog-container .slide .content').removeClass('active');
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

  slideCountMore = $('.more-slide').length;


  $('.more-slider').slick({
    slidesToShow: 1,
    prevArrow: $('.nav-more-slider-desc .custom-prev-arrow'),
    nextArrow: $('.nav-more-slider-desc .custom-next-arrow'),
    autoplaySpeed: 5000,
    //autoplay: true,
    infinite: false,
    dots: false,

    responsive: [
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 1.2,
          prevArrow: $('.nav-more-slider-mobile .col-4 .custom-prev-arrow'),
          nextArrow: $('.nav-more-slider-mobile .col-4 .custom-next-arrow'),
        }
      },
      {
        breakpoint: 1000,
        settings: {
          slidesToShow: 1.2,
          prevArrow: $('.nav-more-slider-mobile .col-4 .custom-prev-arrow'),
          nextArrow: $('.nav-more-slider-mobile .col-4 .custom-next-arrow'),
        }
      },
      {
        breakpoint: 984,
        settings: {
          slidesToShow: 1,
          prevArrow: $('.nav-more-slider-mobile .col-4 .custom-prev-arrow'),
          nextArrow: $('.nav-more-slider-mobile .col-4 .custom-next-arrow'),
        }
      },
    ]
  });

  $('.more-header .sliderCount').html('&nbsp/ ' + slideCountMore);
  $('.more-header .currentSlide').html('01');

  $('.nav-more-slider-mobile .sliderCount').html('&nbsp/ ' + slideCountMore);
  $('.nav-more-slider-mobile .currentSlide').html('01');

  $(".more-slider").on("afterChange", function (event, slick, currentSlide, nextSlide) {
    let currentSlider = $('.more-slider').slick('slickCurrentSlide') + 1;
    if (currentSlider >= 10) {
      $('.more-header .currentSlide').html(currentSlider + ' ');
      $('.nav-more-slider-mobile .currentSlide').html(currentSlider + ' ');
    } else {
      $('.more-header .currentSlide').html('0' + currentSlider + ' ');
      $('.nav-more-slider-mobile .currentSlide').html('0' + currentSlider + ' ');
    }
  });

var catalogSlider = null;


function catalogSliderInit () {
	if (!catalogSlider) {
		catalogSlider = new Swiper('#fullscreen-image .mySwiper', {
      loop: false,
      slidesPerView: 1,
    });
	}
}

function catalogSliderDestroy () {
	if (catalogSlider) {
		catalogSlider.destroy();
		catalogSlider = null;
	}
}

  //инициализация слайдера больше возможностей при загрузке
	windowWidth = $(this).innerWidth();

	if (windowWidth <= 1200) {
		catalogSliderInit()
	} else {
		catalogSliderDestroy()
  }


  
  
  $('.more-slider .more-slide img').click(function (event) {
    if (!$(event.target).hasClass('slick-next') && !$(event.target).hasClass('slick-prev')) {
      var src = $(this).attr('src');
      var index = findSliderItemIndexByImageSrc(src);
     
      if(windowWidth <= 1200){
        catalogSlider.slideTo(index, 0, false);
      }
      else{
        showSlides(index)
      }
      
      

      $('#fullscreen-image').show();
    };
  });

  $('.fullscreen-image-nav .close ').click(function (event) {
    $('#fullscreen-image').hide();

  });


});




var currentSlideIndex = 0;
var slides = document.querySelectorAll("#fullscreen-image .swiper-slide");

function showSlides(slideIndex) {

  if (slideIndex - 1 < 0) {
    document.querySelectorAll("#fullscreen-image .fullscreen-image-nav .custom-prev-arrow")[0].classList.add("slick-disabled");
  } else if (slideIndex + 1 >= slides.length) {
    document.querySelectorAll("#fullscreen-image .fullscreen-image-nav .custom-next-arrow")[0].classList.add("slick-disabled");
  } else {
    document.querySelectorAll("#fullscreen-image .fullscreen-image-nav .custom-prev-arrow")[0].classList.remove("slick-disabled");
    document.querySelectorAll("#fullscreen-image .fullscreen-image-nav .custom-next-arrow")[0].classList.remove("slick-disabled");
  }

  currentSlideIndex = slideIndex;
  for (var i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  slides[slideIndex].style.display = "block";
}

function prevSlide() {
  currentSlideIndex--;
  if (currentSlideIndex < 0) {
    currentSlideIndex = 0;
  }
  showSlides(currentSlideIndex);

}

function nextSlide() {
  currentSlideIndex++;
  if (currentSlideIndex >= slides.length) {
    currentSlideIndex = slides.length - 1;
  }
  showSlides(currentSlideIndex);

}

function findSliderItemIndexByImageSrc(srcToFind) {
  var $sliderItems = $("#fullscreen-image .modal-content .swiper-slide");

  var foundIndex = $sliderItems.filter(function (index, sliderItem) {
    var $img = $(sliderItem).find('img');
    return $img.length > 0 && $img.attr('src') === srcToFind;
  }).index();

  return foundIndex;
}



function readMore(e) {
  ful_text_review = e.parentNode.parentNode.querySelector(".project-and-reviews-text");
  console.log(ful_text_review);
  if (e.innerHTML == "Читать далее...") {
    e.innerHTML = "Свернуть";
    ful_text_review.style.height = `${ful_text_review.scrollHeight}px`;
  }
  else {
    e.innerHTML = "Читать далее...";
    ful_text_review.style.height = "120px";
  }
}




Dribbble = window.Dribbble || {};
Dribbble.JsConfig = Dribbble.JsConfig || {};
Dribbble.isHistorySupported = () => (window.history && 'pushState' in window.history);
DEVICE_WIDTH_BREAKPOINT = '800px';
HIDPI_BREAKPOINT = '(-webkit-min-device-pixel-ratio: 1.5),(min--moz-device-pixel-ratio: 1.5),(-o-min-device-pixel-ratio: 3/2),(min-device-pixel-ratio: 1.5),(min-resolution: 1.5dppx)';
User = {
  loggedIn: function () {
    return !!document.querySelector('body.logged-in')
  },
  loggedOut: function () {
    return !this.loggedIn()
  },
};


var config = Dribbble.JsConfig || {}
Dribbble.JsConfig = Object.assign(config, {
  user: { "isLoggedIn": false, "reCaptchaSiteKey": "6LdmBTIUAAAAAM4NIokaWu8p3BBuYEw3CxuDdyg_", "canPurchasePro": true, "isHiringTrialEligible": false },
  hiringProfile: {},
  features: { "braintreeHiring": false, "proDiscountToasty": false, "collaborators": false, "hiringBundleDiscount": true, "purchaseFreelance": true, "learnRedesign": false, "proTrial": false, "jobBoardTrial": true, "klTags": true, "hideCohortSelection": true, "shotFeedUpdates": false },
  isRobot: null,
  remoteIp: "101.127.248.174",
  isProduction: true,
  permissions: { "userPermissions": ["canBuyBoostWithBraintree", "canSeeThirdPartyPaymentMethods"] },
  screenshot_boost: { "buttonText": [{ "label": "Buy Now", "value": "buy-now" }, { "label": "Download", "value": "download" }, { "label": "Learn More", "value": "learn-more" }, { "label": "Shop Now", "value": "shop-now" }, { "label": "Apply Now", "value": "apply-now" }, { "label": "Try Now", "value": "try-now" }, { "label": "Get Offer", "value": "get-offer" }, { "label": "Contact Us", "value": "contact-us" }], "tiers": { "lowTier": { "daysToServe": 7, "range": { "lowerLimit": 0, "upperLimit": 10000 } }, "midTier": { "daysToServe": 14, "range": { "lowerLimit": 10001, "upperLimit": 100000 } }, "highTier": { "daysToServe": 28, "range": { "lowerLimit": 100001, "upperLimit": null } } }, "pricePerImpression": "0.01", "purchase": { "stripePublicKey": "pk_live_9EfFSEE6iTCgHghKqBqnixxR", "savedCreditCardInformation": null }, "discount": null, "minimumImpressions": 2000, "targetPlacements": { "following": "Following Feed", "popular": "Popular Feed", "search": "Search Feed", "goods": "Goods Feed", "recent": "New \u0026 Noteworthy Feed", "shot_modal": "Shot Modal", "similar_work": "Similar Work", "tags": "Tag Feed", "popular_first": "Popular Feed First" }, "priorities": ["self_serve", "sales", "remnant", "sales_priority"] },
})

window.CanvasRenderer = class {
  setProjectInterface() { }
}
const data = 'https://assets1.lottiefiles.com/datafiles/d9bc9kYC2VttaKb/data.json';
let isActive = false;
let isTouch = false;
const ttest = document.querySelectorAll('.hero-marquee-item__tags');
for (i = 0; i < ttest.length; i++) {
  ttest[i].addEventListener('click', function (e) {
    if (isActive == true) {
      return;
    }
    isTouch = true;
    likes_count = this.querySelectorAll('.likes-count')[0]
    likes_count.innerHTML = parseInt(likes_count.innerHTML) + 1
    lottie_div = this.parentNode.querySelectorAll('.lottie')[0]
    lottie_div.style.opacity = 1;
    var animation = bodymovin.loadAnimation({
      container: lottie_div,
      path: data,
      renderer: 'svg',
      loop: false,
      autoplay: false,

    });
    animation.play();
    isActive = true;
    animation.addEventListener('complete', e => {
      animation.destroy();
      isActive = false;
      isTouch = false;
    })
  });
};
media_div = document.querySelectorAll(".hero-marquee-item");
for (i = 0; i < media_div.length; i++) {
  media_div[i].addEventListener('click', function (e) {
    if (isTouch == false) {
      str = '<div class="shorts-youtube-container">'
      str += '<iframe src="https://www.youtube.com/embed/'
      str += this.querySelector("video").getAttribute("data-url")
      str += '?autoplay=1&mute=1&loop=1&color=white&controls=1&modestbranding=1&playsinline=1&rel=0&enablejsapi=1" title="Infinity restyle 2022" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
      str += '</div>'
      document.getElementById('player').innerHTML = str
      setTimeout(function () {
        $('#videoModal').modal('show');
        var iframe = document.getElementById('player').getElementsByTagName("iframe")[0].contentWindow;
        iframe.postMessage('{"event":"command","func":"playVideo","args":""}', "*");
      }, 300);


    }
  });
}
watchVideoBlocks = document.querySelectorAll(".watch-video")
watchVideoBlocks.forEach(function (block, index) {
  block.onclick = function () {
    str = '<div class="main-youtube-container">'
    str += '<iframe src="https://www.youtube.com/embed/'
    str += this.getAttribute("data-url");
    str += '?autoplay=1&mute=1&loop=1&color=white&controls=1&modestbranding=1&playsinline=1&rel=0&enablejsapi=1" title="Infinity restyle 2022" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    str += '</div>'
    document.getElementById('player').innerHTML = str
    setTimeout(function () {
      $('#videoModal').modal('show');
      var iframe = document.getElementById('player').getElementsByTagName("iframe")[0].contentWindow;
      iframe.postMessage('{"event":"command","func":"playVideo","args":""}', "*");
    }, 300);

  };
});


$('#videoModal').on('hide.bs.modal', function (e) {
  try {
    document.getElementById("player-video").src = "";
  } catch (err) { }
})

$(document).ready(function () {
  text = $(".about-us-text").eq(0);
  size = $("#about-us-block").data("fontsize");
  text.css("font-size", size);
});

$(document).ready(function () {
  if (window.innerWidth < 984) {
    var elements = document.querySelectorAll('.more-slide');
    var elementsArray = Array.from(elements);

    elementsArray.forEach(function (element) {
      var height = element.querySelector('.more-slide-text').offsetHeight;

      if (height > 270) {
        element.getElementsByClassName('mobileFull')[0].style.display = 'block';
        element.querySelector('.more-slide-text').style.maxHeight = "250px";
        element.querySelector('.more-slide-text').style.overflow = 'hidden';
      }
    });
  }
});


function showFull(id) {
  if (document.getElementById('more-slide-' + id).innerText == 'развернуть ') {
    document.getElementById('more-slide-text-' + id).style.maxHeight = "1000px";
    console.log(document.getElementById('more-slide-text-' + id));
    document.getElementById('more-slide-' + id).innerHTML = 'свернуть <svg width="14" height="8" viewBox="0 0 14 8" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.64601 0.646039C6.69245 0.599476 6.74763 0.562533 6.80837 0.537326C6.86912 0.51212 6.93424 0.499146 7.00001 0.499146C7.06577 0.499146 7.13089 0.51212 7.19164 0.537326C7.25238 0.562533 7.30756 0.599476 7.35401 0.646039L13.354 6.64604C13.4479 6.73993 13.5006 6.86726 13.5006 7.00004C13.5006 7.13281 13.4479 7.26015 13.354 7.35404C13.2601 7.44793 13.1328 7.50067 13 7.50067C12.8672 7.50067 12.7399 7.44793 12.646 7.35404L7.00001 1.70704L1.35401 7.35404C1.26012 7.44793 1.13278 7.50067 1.00001 7.50067C0.86723 7.50067 0.739893 7.44793 0.646006 7.35404C0.552119 7.26015 0.499374 7.13281 0.499374 7.00004C0.499374 6.86726 0.552119 6.73993 0.646006 6.64604L6.64601 0.646039Z" fill="#212529"/></svg> ';
  } else {
    document.getElementById('more-slide-text-' + id).style.maxHeight = "270px";
    document.getElementById('more-slide-' + id).innerHTML = 'развернуть <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.64601 4.64604C1.69245 4.59948 1.74763 4.56253 1.80838 4.53733C1.86912 4.51212 1.93424 4.49915 2.00001 4.49915C2.06578 4.49915 2.1309 4.51212 2.19164 4.53733C2.25239 4.56253 2.30756 4.59948 2.35401 4.64604L8.00001 10.293L13.646 4.64604C13.6925 4.59955 13.7477 4.56267 13.8084 4.53752C13.8692 4.51236 13.9343 4.49941 14 4.49941C14.0658 4.49941 14.1309 4.51236 14.1916 4.53752C14.2523 4.56267 14.3075 4.59955 14.354 4.64604C14.4005 4.69253 14.4374 4.74772 14.4625 4.80846C14.4877 4.86919 14.5006 4.9343 14.5006 5.00004C14.5006 5.06578 14.4877 5.13088 14.4625 5.19162C14.4374 5.25236 14.4005 5.30755 14.354 5.35404L8.35401 11.354C8.30756 11.4006 8.25239 11.4375 8.19164 11.4628C8.1309 11.488 8.06578 11.5009 8.00001 11.5009C7.93424 11.5009 7.86912 11.488 7.80838 11.4628C7.74763 11.4375 7.69245 11.4006 7.64601 11.354L1.64601 5.35404C1.59945 5.30759 1.5625 5.25242 1.5373 5.19167C1.51209 5.13093 1.49911 5.06581 1.49911 5.00004C1.49911 4.93427 1.51209 4.86915 1.5373 4.80841C1.5625 4.74766 1.59945 4.69248 1.64601 4.64604Z" fill="#212529"/></svg>';

  }
}
