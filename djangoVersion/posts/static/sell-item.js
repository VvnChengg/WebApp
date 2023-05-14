const sellForm = document.querySelector('#sell-form');
const submitBtn = document.querySelector('#sell-submit-button');
const cancelBtn = document.querySelector('#cancel-button');

// 點擊按鈕彈出表單
sellForm.style.display = 'block';

// 檢查必填項目是否填寫完整
submitBtn.addEventListener('click', () => {
  const name = document.querySelector('#item-name').value;
  const price = document.querySelector('#item-price').value;
  const transaction = document.querySelector('#item-transaction').value;
  const location = document.querySelector('#item-location').value;
  const quantity = document.querySelector('#item-quantity').value;
  const category = document.querySelector('#item-category').value;
  const condition = document.querySelector('#item-condition').value;

  if (!name || !price || !category || !condition) {
    alert('請填寫必填項目');
    return;
  }
});

// 點擊取消按鈕關閉表單
cancelBtn.addEventListener('click', () => {
    sellForm.style.display = 'none';
    window.location.href = 'http://127.0.0.1:8000/posts/';
});


// 提交表單時，建立一個新的商品並顯示在網頁上
sellForm.addEventListener("submit", (event) => {
    sellForm.style.display = "none";
    window.location.href = 'http://127.0.0.1:8000/posts/';
});