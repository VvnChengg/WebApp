var detailButtons = document.querySelectorAll('.item-details-button');
var detailContainer = document.querySelector('.item-details-container');
var closeButtons = document.querySelectorAll('.close-button');
var wrapper = document.querySelector('#item-details-wrapper');

detailButtons.forEach(function(button) {
  button.addEventListener('click', function() {
    detailContainer.style.display = 'block';
    wrapper.style.display = 'block';
  });
});

closeButtons.forEach(function(button) {
  button.addEventListener('click', function() {
    detailContainer.style.display = 'none';
    wrapper.style.display = 'none';
  });
});
