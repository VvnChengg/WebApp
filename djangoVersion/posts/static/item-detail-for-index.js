var detailButtons = document.querySelectorAll('.item-details-button');
var closeButtons = document.querySelectorAll('.close-button');

detailButtons.forEach(function(button) {
  button.addEventListener('click', function() {
    const itemId = button.dataset.itemId;
    const url = '/posts/item/' + itemId;
    window.location.href = url;
  });
});