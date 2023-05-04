
let btn = document.getElementsByClassName('btn');
let slide = document.getElementById('slide')

btn[0].onclick = function() {
    slide.style.transform = 'translateX(38%)';
    for (let i = 0; i < 4; i++) {
        btn[i].classList.remove('btn-active');
    }
    this.classList.add('btn-active');
}

btn[1].onclick = function() {
    slide.style.transform = 'translateX(13%)';
    for (let i = 0; i < 4; i++) {
        btn[i].classList.remove('btn-active');
    }
    this.classList.add('btn-active');
}

btn[2].onclick = function() {
    slide.style.transform = 'translateX(-12%)';
    for (let i = 0; i < 4; i++) {
        btn[i].classList.remove('btn-active');
    }
    this.classList.add('btn-active');
}

btn[3].onclick = function() {
    slide.style.transform = 'translateX(-37%)';
    for (let i = 0; i < 4; i++) {
        btn[i].classList.remove('btn-active');
    }
    this.classList.add('btn-active');
}


document.querySelector('#article-01').addEventListener('click', () => {
    document.querySelector('.popup-page').classList.add('active');
});

document.querySelector('.popup-page .close-btn').addEventListener('click', () => {
    document.querySelector('.popup-page').classList.remove('active');
});