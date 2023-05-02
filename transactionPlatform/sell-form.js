const sellBtn = document.querySelector('#sell-button');
const sellForm = document.querySelector('#sell-form');
const submitBtn = document.querySelector('#sell-submit-button');
const cancelBtn = document.querySelector('#cancel-button');

// 點擊按鈕彈出表單
sellBtn.addEventListener('click', () => {
    sellForm.style.display = 'block';
});

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

  // 創建一個物品對象
  const item = {
    name: name,
    price: price,
    transaction: transaction,
    location: location,
    quantity: quantity,
    category: category,
    condition: condition
    // 其他選填項目可以在這裡添加
  };

  console.log(item); // 印出物品對象
});

// 點擊取消按鈕關閉表單
cancelBtn.addEventListener('click', () => {
    sellForm.style.display = 'none';
});


const itemContainer = document.querySelector('#item-container');

// 提交表單時，建立一個新的商品並顯示在網頁上
sellForm.addEventListener("submit", (event) => {
    sellForm.style.display = "none";

    console.log('Submit button clicked')
    event.preventDefault();
    const itemName = document.getElementById("item-name").value;
    const itemPrice = document.getElementById("item-price").value;
    const itemImage = document.getElementById("item-image").value;
    const newItem = document.createElement("div");
    newItem.className = "newItem";
    newItem.innerHTML = `
      <img src="${itemImage}">
      <h3>${itemName}</h3>
      <p>價格：${itemPrice}</p>
      <button class="item-details-button">詳細資訊</button>
      <div class="item-details-container" style="display:none;">
        <!-- 商品詳細資訊 -->
      </div>
    `;
    itemContainer.appendChild(newItem);
  });