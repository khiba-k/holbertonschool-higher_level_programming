const myHeader = document.body.querySelector("header");

const myClick = document.body.querySelector("#red_header");
myClick.addEventListener("click", () => {
    myClick.classList.add("red");
});