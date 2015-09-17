
$(document).ready(function () {
  $('.element').on('click', function() {

    var elementTag = 'my-' + this.innerHTML;
    $('.' + elementTag).toggleClass('highlight');
    $(this).toggleClass('highlight');
    console.log('toggling class');
  });

});
