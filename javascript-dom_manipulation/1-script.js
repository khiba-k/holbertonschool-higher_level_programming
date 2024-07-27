const myHeader = document.body.querySelector("header");

const myClick = document.body.querySelector("#red_header");
myClick.addEventListener("click", () => {
    myHeader.style.color = "#FF0000";
});