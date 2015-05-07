$(document).ready(function() {
    // hide everything that is not main.
    $(".container").not("#main").not("#nav").hide();

    // when a nav link/button is clicked, show the corresponding
    // container and hide the others.
    $('.navlink').click(function(){
        var target = "#" + $(this).data("target");
        $(".container").not(target).not("#nav").hide();
        $(target).show();
    });

    // when a top level nav menu link is clicked, update the 'active'
    // class to highlight the nav link for the current page.
    $('ul.nav li a').click(function(e) {
        var $this = $(this);
        $this.parent().siblings().removeClass('active').end().addClass('active');
        e.preventDefault();
    });
});
