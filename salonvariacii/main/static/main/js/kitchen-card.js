$(document).ready(function () {
    $('#kitchen-card-slider .kitchen-card-slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
        centerMode: true,
        prevArrow: $('.nav-kitchen-card-slider .custom-prev-arrow'),
        nextArrow: $('.nav-kitchen-card-slider .custom-next-arrow'),
        infinite: true,
        variableWidth: true,
        responsive: [
            {
                breakpoint: 1200,
                settings: {
                    centerMode: false,
                    infinite: false,
                    slidesToShow: 1.8,
                }
            }
        ]
    });


    setTimeout(function() {
        var iframe = document.getElementsByTagName("iframe")[0].contentWindow;
        iframe.postMessage('{"event":"command","func":"playVideo","args":""}', "*");
    }, 500);
        


});