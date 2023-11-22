$(document).ready(function() {
    var navbarToggler = document.querySelector('.navbar-toggler');
    var navbar = document.querySelector('.navbar');

    navbarToggler.addEventListener('click', function() {
        if (navbar.classList.contains('navbar-opened')) {
            navbar.classList.remove('navbar-opened');
            document.getElementById("header").style.background = "rgba(255, 255, 255, .9)"
            /*document.getElementById("header").style.height = "auto"*/
            в
        }
        else {
            navbar.classList.add('navbar-opened');
            document.getElementById("header").style.background = "rgba(255, 255, 255, 1)"
            /*document.getElementById("header").style.height = "100%"*/
        }
    });

    $("#navbarNav").on('show.bs.collapse', function() {
    $('a.nav-link').click(function() {
        $("#navbarNav").collapse('hide');
    });
});
});