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

    $('.kitchen-annotation-right').click(function () {
        console.log($(this).find("video")[0].paused);
        if ($(this).find("video")[0].paused) {
            $(this).find("svg").hide();
            $(this).find("video").trigger('play');
        } else {
            $(this).find("video").trigger('pause');
            $(this).find("svg").show();
        }
    });
});