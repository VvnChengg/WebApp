// var detailButtons = document.querySelectorAll('.item-details-button');
// var detailContainer = document.querySelectorAll('.item-details-container');
// var closeButtons = document.querySelectorAll('.close-button');
// var wrapper = document.querySelectorAll('.item-details-wrapper');

// detailButtons.forEach(function(button, index) {
//   button.addEventListener('click', function() {
//     detailContainer[index].style.display = 'block';
//     wrapper[index].style.display = 'block';
//   });
// });

// closeButtons.forEach(function(button, index) {
//   button.addEventListener('click', function() {
//     detailContainer[index].style.display = 'none';
//     wrapper[index].style.display = 'none';
//   });
// });

var detailButtons = document.querySelectorAll('.item-details-button');
var closeButtons = document.querySelectorAll('.close-button');

detailButtons.forEach(function(button) {
  button.addEventListener('click', function() {
    var newItem = this.closest('.newItem');
    var itemDetailsContainer = newItem.querySelector('.item-details-container');
    itemDetailsContainer.style.display = 'block';
  });
});

closeButtons.forEach(function(button) {
  button.addEventListener('click', function() {
    var newItem = this.closest('.newItem');
    var itemDetailsContainer = newItem.querySelector('.item-details-container');
    itemDetailsContainer.style.display = 'none';
  });
});