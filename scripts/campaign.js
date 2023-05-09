

document.querySelector('.campaign-add').addEventListener('click', () => {
    document.querySelector('.campaign-form-container').classList.add('form-active');
    document.querySelector('.campaign-form-overlay').classList.add('overlay-active');
})

document.querySelector('.campaign-form-close').addEventListener('click', () => {
    document.querySelector('.campaign-form-container').classList.remove('form-active');
    document.querySelector('.campaign-form-overlay').classList.remove('overlay-active');
})

// adding campaign 
