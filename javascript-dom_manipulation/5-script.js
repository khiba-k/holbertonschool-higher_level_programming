const myHeader = document.body.querySelector("header");

const myUpdate = document.body.querySelector("#update_header");
myUpdate.addEventListener("click", () => {
    myHeader.textContent = "New Header!!!";
})