// js/router.js
document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll("nav a");
    const body = document.body;

    links.forEach(link => {
        link.addEventListener("click", function (e) {
            e.preventDefault();
            const url = this.getAttribute("href");

            // 添加淡出动画
            body.classList.add("fade-out");

            setTimeout(() => {
                window.location.href = url;
            }, 300); // 等待动画完成
        });
    });

    // 页面加载时添加淡入动画
    body.classList.add("fade-in");
});