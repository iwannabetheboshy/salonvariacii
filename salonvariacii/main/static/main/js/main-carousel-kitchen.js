$(document).ready(function(){
    const progressFill = $('.progress-fill');
    let progressWidth = 0; // Начальная ширина заполняющейся линии
    const interval = 5000; // Интервал смены слайдов (5 секунд)

    function updateProgressBar() {
        progressWidth = 0; 
        progressFill.css('width', '0%');

        progressFill.animate({
            width: '100%'
        }, interval, 'linear');
    }

    // Инициализация Slick Slider
    $('.main-kitchen-carousel').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        variableWidth: true,
        prevArrow: $('.custom-prev-arrow'),
        nextArrow: $('.custom-next-arrow'),
        //autoplay: true,
        //autoplaySpeed: interval,
        //onAfterChange: updateProgressBar, 
        infinite: false, // Отключает бесконечную прокрутку
        edgeFriction: 0.2, // Добавляет сопротивление на краях слайдера
        responsive: [
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            }
            
          ]
    });

    //updateProgressBar();
});
