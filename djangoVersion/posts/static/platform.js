// 當點擊類別時，設置類別為 active，取消其他類別的 active 狀態
const categoryLinks = document.querySelectorAll('.categories ul li a');
for (let i = 0; i < categoryLinks.length; i++) {
  categoryLinks[i].addEventListener('click', function(e) {
    e.preventDefault();
    const activeLink = document.querySelector('.categories ul li.active a');
    activeLink.classList.remove('active');
    this.classList.add('active');
  });
}
