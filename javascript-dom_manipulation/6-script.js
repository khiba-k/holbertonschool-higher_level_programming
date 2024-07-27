const myDiv = document.body.querySelector("#id");

const fetched = fetch('https://swapi-api.hbtn.io/api/people/5/?format=json').then(
    response => {
        return response.json();
    }
).then(data => {
    myDiv.textContent = JSON.stringify(data);
}).catch(error => {
    console.error('The was a problem with the fetch operation');
});


