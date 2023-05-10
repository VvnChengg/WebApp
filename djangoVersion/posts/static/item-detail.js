const pathName = window.location.pathname; // "/posts/item/1/"
const itemId = pathName.match(/(\d+)\/$/)[1]; // "1"

const itemDetailsContainer = document.querySelector(`.item-details-container[data-item-id="${itemId}"]`);
itemDetailsContainer.style.display = 'block';

var closeButton = document.querySelector(`.close-button[data-item-id="${itemId}"]`);


closeButton.addEventListener('click', function() {
  itemDetailsContainer.style.display = 'none';
  var url = new URL(window.location.href);
  url.searchParams.delete('item_id');
  window.history.pushState({}, '', url);
  window.location.href = 'http://127.0.0.1:8000/posts/';
})