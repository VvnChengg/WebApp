var detailButtons = document.querySelectorAll('.item-details-button');
var closeButtons = document.querySelectorAll('.close-button');

detailButtons.forEach(function(button) {
  button.addEventListener('click', function() {
    var newItem = this.closest('.newItem');
    var itemDetailsContainer = newItem.querySelector('.item-details-container');
    itemDetailsContainer.style.display = 'block';

    const itemId = button.dataset.itemId;
    const url = '/posts/item/' + itemId;  
    window.location.href = url;
  });
});

closeButtons.forEach(function(button) {
  button.addEventListener('click', function() {
    var newItem = this.closest('.newItem');
    var itemDetailsContainer = newItem.querySelector('.item-details-container');
    itemDetailsContainer.style.display = 'none';

    // Remove item_id parameter from URL
    var url = new URL(window.location.href);
    url.searchParams.delete('item_id');
    window.history.pushState({}, '', url);
  });
});