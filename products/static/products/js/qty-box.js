// Limits the range of the buttons to 1-99
function disableOption(itemId) {
    var quantity = parseInt($(`#id_qty_${itemId}`).val());
    var minusDisabled = quantity < 2;
    var plusDisabled = quantity > 98;
    $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
}

// disables buttons correctly on page load
var allQtyInputs = $('.select_input');
for(var i = 0; i < allQtyInputs.length; i++){
    var itemId = $(allQtyInputs[i]).data('item_id');
    disableOption(itemId);
}

// checks to disable function on each click
$('.select_input').change(function() {
    var itemId = $(this).data('item_id');
    disableOption(itemId);
});

// Increment product quantity
$('.increment-qty').click(function(e) {
   e.preventDefault();
   // get the parent input group then search for select input class
   var parent = $(this).closest('.input-group').find('.form-control')[0];
   var quantity = parseInt($(parent).val());
   // set new quantity box value
   $(parent).val(quantity + 1);
   var itemId = $(this).data('item_id');
   disableOption(itemId);
});

// Decrement product quantity
$('.decrement-qty').click(function(e) {
   e.preventDefault();
   // get the parent input group then search for select input class
   var parent = $(this).closest('.input-group').find('.form-control')[0];
   var quantity = parseInt($(parent).val());
   // set new quantity box value
   $(parent).val(quantity - 1);
   var itemId = $(this).data('item_id');
   disableOption(itemId);
});