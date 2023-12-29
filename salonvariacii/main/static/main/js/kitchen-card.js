
$(document).ready(function () {
    slideCount = $('#kitchen-card-slider .kitchen-card-slide').length;
    if ($('#kitchen-card-slider .kitchen-card-slide').length > 8) {
        $('#kitchen-card-slider').addClass("dotsFalse");
    }

    var header = document.querySelector("header");
    header.classList.add("catalogCard");
        $('#kitchen-card-slider .kitchen-card-slider').slick({
        slidesToShow: 1.5, // Количество отображаемых слайдов
        slidesToScroll: 1,
        prevArrow: $('.nav-kitchen-card-slider .custom-prev-arrow'),
        nextArrow: $('.nav-kitchen-card-slider .custom-next-arrow'),
        infinite: true,
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        centerMode: false,
                        infinite: false,
                        slidesToShow: 1.8,
                        prevArrow: $('#kitchen-card-slider .nav-kitchen-card-slider-mobile .col-4 .custom-prev-arrow'),
                        nextArrow: $('#kitchen-card-slider .nav-kitchen-card-slider-mobile .col-4 .custom-next-arrow'),
                    }
                }
            ]
        });
    


    if(slideCount  >= 10){
        $('#kitchen-card-slider .nav-kitchen-card-slider .sliderCount').html('&nbsp/ ' + slideCount);
        $('#kitchen-card-slider .nav-kitchen-card-slider-mobile .sliderCount').html('&nbsp/ ' + slideCount);
    }
    else{
        $('#kitchen-card-slider .nav-kitchen-card-slider .sliderCount').html('&nbsp/ 0' + slideCount);
        $('#kitchen-card-slider .nav-kitchen-card-slider-mobile .sliderCount').html('&nbsp/ 0' + slideCount);
    }
    
    $('#kitchen-card-slider .nav-kitchen-card-slider .currentSlide').html('01');
    $('#kitchen-card-slider .nav-kitchen-card-slider-mobile .currentSlide').html('01');

    $("#kitchen-card-slider .kitchen-card-slider").on("afterChange", function (event, slick, currentSlide, nextSlide) {
        let currentSlider = $('#kitchen-card-slider .kitchen-card-slider').slick('slickCurrentSlide') + 1;
        if (currentSlider >= 10) {
            $('#kitchen-card-slider .nav-kitchen-card-slider .currentSlide').html(currentSlider + ' ');
            $('#kitchen-card-slider .nav-kitchen-card-slider-mobile .currentSlide').html(currentSlider + ' ');
        } else {
            $('#kitchen-card-slider .nav-kitchen-card-slider .currentSlide').html('0' + currentSlider + ' ');
            $('#kitchen-card-slider .nav-kitchen-card-slider-mobile .currentSlide').html('0' + currentSlider + ' ');
        }
    });

    setTimeout(function () {
        var iframe = document.getElementsByTagName("iframe")[0].contentWindow;
        iframe.postMessage('{"event":"command","func":"playVideo","args":""}', "*");
    }, 500);



});