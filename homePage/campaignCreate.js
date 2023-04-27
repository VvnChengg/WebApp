const createBtn = document.querySelector('.campaign-create');
const closeBtn = document.querySelector('.close-form');
const formContainer = document.querySelector('.campaign-form-container');

createBtn.addEventListener('click', () => {
formContainer.style.display = 'block';
});

closeBtn.addEventListener('click', () => {
formContainer.style.display = 'none';
});

const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
event.preventDefault();

const eventName = document.querySelector('#campaign-name').value;
const eventDate = document.querySelector('#campaign-date').value;
const eventTime = document.querySelector('#campaign-time').value;
const eventLocation = document.querySelector('#campaign-location').value;

// 將表單資料傳到後端進行處理
// ...

form.reset();
formContainer.style.display = 'none';
});