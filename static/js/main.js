$(function() {
    $(document).ready(function() {
        $(document).scroll(function(e) {
            e.preventDefault();

            var movement = $(document).scrollTop() * 0.2;
            $(".parallax").css("background-position-y", movement + "px");
        });
    });


    $(document).ready(function() {
        $("body").smoothWheel(0);
    });
});
