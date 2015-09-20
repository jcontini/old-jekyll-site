/* Make external links open in a new window */
$(document.links).filter(function() {
    return this.hostname != window.location.hostname;
}).attr('target', '_blank');

/* Start the bigfoots */
$.bigfoot();

/* Scroll to Top feature */
jQuery(document).ready(function() {
    var offset = 250;
    var duration = 300;
    jQuery(window).scroll(function() {
        if (jQuery(this).scrollTop() > offset) {
            jQuery('.back-to-top').fadeIn(duration);
        } else {
            jQuery('.back-to-top').fadeOut(duration);
        }
    });

    jQuery('.back-to-top').click(function(event) {
        event.preventDefault();
        jQuery('html, body').animate({scrollTop: 0}, duration);
        return false;
    })
});

/* Random Quote Selector */
$(document).ready(function () {
    var url = "https://rawgit.com/jcontini/jcontini.github.io/master/_data/quotes.json";
    $.getJSON(url,
    function (json) {
        var i = Math.floor(Math.random() * json.length);
        $('#random #quote').html('<div>"' + json[i].quote + '"</div>');
        $('#random #author').html('<div><i class="fa fa-pencil-square-o"></i>  ' + json[i].author + '</div>');
    });
});