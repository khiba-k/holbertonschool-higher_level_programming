const myHeader = document.body.querySelector("header");
myHeader.style.color = "red";

const myClick = document.body.querySelector("#toggle_header");
myClick.addEventListener("click", () => {
    if (myHeader.style.color === "red") {
        myHeader.style.color = "green";
    }else {
        myHeader.style.color = "red";
    }
});