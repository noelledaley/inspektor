
$(document).ready(function () {
  $('.element').on('click', function() {
    // Add an event listener to each element tag in Summary table

    var elementTag = 'my-' + this.innerHTML;
    $('.' + elementTag).toggleClass('highlight');

    // Toggle entire table rows 
    $(this).toggleClass('highlight');
    $(this).next().toggleClass('highlight');

  });

});
