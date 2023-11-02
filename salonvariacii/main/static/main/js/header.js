$(document).ready(function() {
    var burger = document.getElementsByClassName('burger')[0];
    var close = document.getElementsByClassName('burger-close')[0];
    var burger_nav = document.getElementsByClassName('burger-menu')[0];

      burger.onclick = function() {
        close.style.display = 'block';
        burger.style.display = 'none';
        burger_nav.style.display = 'block';
    };

    close.onclick =function() {
        close.style.display = 'none';
        burger.style.display = 'block';
        burger_nav.style.display = 'none';
    };
  });