// Limits the range of the buttons to 1-99
function disableOption(itemId, size) {
    if (size) {
        // if item has size
        var quantity = parseInt($(`.size_${itemId}_${size}`).val());
    } else {
        // if item does not have size
        var quantity = parseInt($(`.id_qty_${itemId}`).val());
    }

    // Number range offset by 1 gives (1-99)
    var minusDisabled = quantity < 2;
    var plusDisabled = quantity > 98;

    if (size) {
        // if item has size set buttons to adjust by ID and size
        $(`.decrement-size_${itemId}_${size}`).prop('disabled', minusDisabled);
        $(`.increment-size_${itemId}_${size}`).prop('disabled', plusDisabled);
    } else {
        // if item has no size set buttons to adjust by ID only
        $(`.decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`.increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }
}

// disables buttons correctly on page load
var allQtyInputs = $('.select_input');
for(var i = 0; i < allQtyInputs.length; i++){
    var itemId = $(allQtyInputs[i]).data('item_id');
    var size = $(allQtyInputs[i]).data('size');
    disableOption(itemId, size);
    
}

// checks to disable function on each click
$('.select_input').change(function() {
    var itemId = $(this).data('item_id');
    var size = $(this).data('size');
    disableOption(itemId, size);
});

// Increment product quantity
$('.increment-qty').click(function(e) {
   e.preventDefault();
   var itemId = $(this).data('item_id');
   var size = $(this).data('size');
   // get the parent input group then search for select input class
   var parent = $(this).closest('.input-group').find('.form-control')[0];
   if (size) {
        var allQuantityInputs = $(`.input-group-${itemId} input[data-size='${size}']`);
    } else {
        var allQuantityInputs = $(`.input-group-${itemId} input[name='quantity']`);
    }
   var quantity = parseInt($(parent).val());
   // set new quantity box value
   $(allQuantityInputs).val(quantity + 1);
   disableOption(itemId, size);
});

// Decrement product quantity
$('.decrement-qty').click(function(e) {
   e.preventDefault();
   var itemId = $(this).data('item_id');
   var size = $(this).data('size');
   // get the parent input group then search for select input class
   var parent = $(this).closest('.input-group').find('.form-control')[0];
   if (size) {
        var allQuantityInputs = $(`.input-group-${itemId} input[data-size='${size}']`);
    } else {
        var allQuantityInputs = $(`.input-group-${itemId} input[name='quantity']`);
    }
   var quantity = parseInt($(parent).val());
   // set new quantity box value
   $(allQuantityInputs).val(quantity - 1);
   disableOption(itemId, size);
});
