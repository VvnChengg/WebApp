// search bar
let search_flg = false;
let search_btn = document.querySelector('.top-search');
let search_bar = document.querySelector('.show-search');

search_btn.onclick = function () {
    if (search_flg === false) {
        search_bar.classList.add('search-active');
        search_flg = true;
        document.querySelector('#top-search-btn').src = '/static/images/cancel.png';
    }
    else {
        search_bar.classList.remove('search-active');
        search_flg = false;
        document.querySelector('#top-search-btn').src = '/static/images/search.png';
    }
    console.log(search_flg)
}

const searchForm = document.getElementById('searchform');
    searchForm.addEventListener('submit', function (event) {
    event.preventDefault(); // 阻止預設的表單提交行為

    const keyword = document.getElementById('s').value; // 獲取搜尋關鍵字的值
    const url = `/posts/search?keyword=${keyword}`; // 構建搜尋的 URL，將關鍵字作為參數
    window.location.href = url; // 跳轉到後端處理搜尋的 URL
});