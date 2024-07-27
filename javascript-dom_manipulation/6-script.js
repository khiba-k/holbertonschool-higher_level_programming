const myDiv = document.body.querySelector("#character");

const fetched = fetch('https://swapi-api.hbtn.io/api/people/5/?format=json').then(
    response => {
        return response.json();
    }
).then(data => {
    const name = data.name;
    myDiv.textContent = name;
})
.catch(error => {
    console.error('Error:', error);
    myDiv.textContent = 'Error fetching character';
});


