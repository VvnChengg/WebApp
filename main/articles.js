var articles = [
    { title: "文章 1", image: "pic3.jpeg", content: "這是文章 1 的內容" },
    { title: "文章 2", image: "pic4.jpg.webp", content: "這是文章 2 的內容" },
    { title: "文章 3", image: "pic5.jpg", content: "這是文章 3 的內容" }
];


// var container = document.getElementById("articles-container");

// for (var i = 0; i < articles.length; i++) {
//   var article = articles[i];
//   var articleDiv = document.createElement("div");
//   articleDiv.classList.add("article");
//   articleDiv.innerHTML = "<img src='" + article.image + "'><h3>" + article.title + "</h3>";
//   container.appendChild(articleDiv);
// }

// for (var i = 0; i < articles.length; i++) {
//     var articleDiv = document.createElement("div");
//     articleDiv.className = "article";

//     var articleImg = document.createElement("img");
//     articleImg.className = "article-img";
//     articleImg.src = articles[i].image;

//     var articleTitle = document.createElement("p");
//     articleTitle.className = "article-title";
//     articleTitle.textContent = articles[i].title;

//     articleDiv.appendChild(articleImg);
//     articleDiv.appendChild(articleTitle);

//     var container = document.getElementById("article-title");
//     container.appendChild(articleDiv);
// }

var articles = document.getElementsByClassName("article");

for (var i = 0; i < articles.length; i++) {
  articles[i].addEventListener("click", function() {
    var articleIndex = Array.prototype.indexOf.call(articles, this);
    var article = articles[articleIndex];
    var content = article.content;
    window.alert(content);
  });
}

// var scrollAmount = 300;

// document.querySelector("#articles-container button.left").addEventListener("click", function() {
//   document.getElementById("articles-container").scrollLeft -= scrollAmount;
// });

// document.querySelector("#articles-container button.right").addEventListener("click", function() {
//   document.getElementById("articles-container").scrollLeft += scrollAmount;
// });
