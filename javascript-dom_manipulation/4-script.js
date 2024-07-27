const myUl = document.body.querySelector(".my_list");

const myAdd = document.body.querySelector("#add_item");
myAdd.addEventListener("click", () => {
    const mylist = document.createElement("li");
    mylist.textContent = "Item";
    parent.appendChild(mylist);
});