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
      return '<span> 0' +( i + 1 ) + '</span>';
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
        slidesToShow: 1.25
      }
    },
    {
      breakpoint: 700,
      settings: {
        slidesToShow: 1.15
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 1.1
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
      return '<span> 0' +( i + 1 ) + '</span>';
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
});

function readMore (e) {
  ful_text_review = e.parentNode.parentNode.querySelector(".project-and-reviews-text");
  console.log(ful_text_review);
  if (e.innerHTML == "Читать далее...") {
    e.innerHTML = "Свернуть";
    ful_text_review.style.height = `${ ful_text_review.scrollHeight }px`;
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
      loggedIn: function() {
        return !!document.querySelector('body.logged-in')
      },
      loggedOut: function() {
        return !this.loggedIn()
      },
    };


    var config = Dribbble.JsConfig || {}
    Dribbble.JsConfig = Object.assign(config, {
        user: {"isLoggedIn":false,"reCaptchaSiteKey":"6LdmBTIUAAAAAM4NIokaWu8p3BBuYEw3CxuDdyg_","canPurchasePro":true,"isHiringTrialEligible":false},
        hiringProfile: {},
        features: {"braintreeHiring":false,"proDiscountToasty":false,"collaborators":false,"hiringBundleDiscount":true,"purchaseFreelance":true,"learnRedesign":false,"proTrial":false,"jobBoardTrial":true,"klTags":true,"hideCohortSelection":true,"shotFeedUpdates":false},
        isRobot: null,
        remoteIp: "101.127.248.174",
        isProduction: true,
        permissions: {"userPermissions":["canBuyBoostWithBraintree","canSeeThirdPartyPaymentMethods"]},
        screenshot_boost: {"buttonText":[{"label":"Buy Now","value":"buy-now"},{"label":"Download","value":"download"},{"label":"Learn More","value":"learn-more"},{"label":"Shop Now","value":"shop-now"},{"label":"Apply Now","value":"apply-now"},{"label":"Try Now","value":"try-now"},{"label":"Get Offer","value":"get-offer"},{"label":"Contact Us","value":"contact-us"}],"tiers":{"lowTier":{"daysToServe":7,"range":{"lowerLimit":0,"upperLimit":10000}},"midTier":{"daysToServe":14,"range":{"lowerLimit":10001,"upperLimit":100000}},"highTier":{"daysToServe":28,"range":{"lowerLimit":100001,"upperLimit":null}}},"pricePerImpression":"0.01","purchase":{"stripePublicKey":"pk_live_9EfFSEE6iTCgHghKqBqnixxR","savedCreditCardInformation":null},"discount":null,"minimumImpressions":2000,"targetPlacements":{"following":"Following Feed","popular":"Popular Feed","search":"Search Feed","goods":"Goods Feed","recent":"New \u0026 Noteworthy Feed","shot_modal":"Shot Modal","similar_work":"Similar Work","tags":"Tag Feed","popular_first":"Popular Feed First"},"priorities":["self_serve","sales","remnant","sales_priority"]},
    })

    window.CanvasRenderer = class {
      setProjectInterface() {}
  }
  const data = 'https://assets1.lottiefiles.com/datafiles/d9bc9kYC2VttaKb/data.json';
  let isActive = false;
  let isTouch = false;
  const ttest = document.querySelectorAll('.hero-marquee-item__tags');
  for (i = 0; i < ttest.length; i++) {
      ttest[i].addEventListener('click', function(e) {
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
                autoplay: false
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
      media_div[i].addEventListener('click', function(e) {
         if (isTouch == false) {
          str = '<div class="shorts-youtube-container">'
          str += '<iframe src="https://www.youtube.com/embed/'
          str += this.querySelector("video").getAttribute("data-url")
          str += '?autoplay=1&mute=1&loop=1&color=white&controls=1&modestbranding=1&playsinline=1&rel=0" title="Infinity restyle 2022" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
          str += '</div>'
          document.getElementById('player').innerHTML = str
          $('#videoModal').modal('show');
         }
      });
  }
  watchVideoBlocks = document.querySelectorAll(".watch-video")
  watchVideoBlocks.forEach(function(block, index) {
      block.onclick = function() {
          str = '<div class="main-youtube-container">'
          str += '<iframe src="https://www.youtube.com/embed/z8xoGi5pK70?autoplay=1&mute=1&loop=1&color=white&controls=1&modestbranding=1&playsinline=1&rel=0" title="Infinity restyle 2022" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
          str += '</div>'
          document.getElementById('player').innerHTML = str
          $('#videoModal').modal('show');
      };
  });


  $('#videoModal').on('hide.bs.modal', function (e) {
    try {
      document.getElementById("player-video").src = "";
    } catch (err)
    {}
  })
