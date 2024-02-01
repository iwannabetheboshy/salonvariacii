$(document).ready( function () {
    const swiper = new Swiper('.mySwiper', {
        spaceBetween: 16,
        loop: true,
        loopAdditionalSlides: 1,
        LoopedSlides: 1,
        initialSlide: 3,
        navigation: {
            nextEl: '.nav-kitchen-card-slider .custom-next-arrow',
            prevEl: '.nav-kitchen-card-slider .custom-prev-arrow',
            enabled: true,
        },
        pagination: {
            el: '.swiper-pagination',
            type: 'fraction',
            formatFractionCurrent: function (number) {
                return number < 10 ? '0' + number : number;
            },
        },
        breakpoints: {
            // when window width is >= 320px
            1200: {
                centeredSlides: true,
                slidesPerView: 1.8,
            },
            // when window width is >= 480px
            360: {
                centeredSlides: false,
                slidesPerView: 'auto',
             
            },
            
          }
        
    });
    
    

    setTimeout(function () {
        swiper.slideToLoop(0, 0, true)

    }, 500);
    var header = document.querySelector("header");
    header.classList.add("catalogCard");

    
    



    setTimeout(function () {
        var iframe = document.getElementsByTagName("iframe")[0].contentWindow;
        iframe.postMessage('{"event":"command","func":"playVideo","args":""}', "*");
    }, 500);


});

