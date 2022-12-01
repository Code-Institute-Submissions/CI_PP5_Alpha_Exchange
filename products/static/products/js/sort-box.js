// sorts the products on the page by the current selection
$('#sort-box').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    // get the selected value and check against the default
    var selectedVal = selector.val();
    if(selectedVal != "default"){
        // Split the sort type and direction
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];

        // build and replace the current url
        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        // if default selected delete sort url 
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
});
