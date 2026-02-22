document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll(".match-card");
    elements.forEach((el, i) => {
        el.style.opacity = 0;
        setTimeout(() => {
            el.style.transition = "1s";
            el.style.opacity = 1;
        }, i * 300);
    });
});