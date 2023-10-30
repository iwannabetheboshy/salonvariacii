$(document).ready(function() {

    $('.slide').click(function() {
        $('.slide img').removeClass('large-image');
      // Добавляем класс large-image только к изображению, на которое кликнули
      $('.slide .content').removeClass('active');
      $(this).find('img').addClass('large-image');
      $(this).find('.content').addClass('active');
    });
  });
