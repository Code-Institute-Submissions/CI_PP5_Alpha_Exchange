/**
 * This module controls the update and remove buttons for the basket items
 * the get cookie function gets the current csrfToken from the form for 
 * use during post.
 */

// getCookie function to get the current csrfToken
function getCookie(name) {
    function escape(s) { return s.replace(/([.*+?\^$(){}|\[\]\/\\])/g, '\\$1'); }
    var match = document.cookie.match(RegExp('(?:^|;\\s*)' + escape(name) + '=([^;]*)'));
    return match ? match[1] : null;
}

// Update quantity on click
$('.update-link').click(function(e) {
    var form = $(this).parent().prev('.update-form');
    form.submit();
});

// Remove item and reload on click
$('.remove-item').click(function(e) {
    var csrfToken = getCookie("csrftoken");
    var itemId = $(this).attr('class').split('remove_')[1];
    var size = $(this).data('product_size');
    var url = `/basket/remove/${itemId}/`;
    var data = {'csrfmiddlewaretoken': csrfToken, 'product_size': size};

    $.post(url, data)
     .done(function() {
         location.reload();
     });
});