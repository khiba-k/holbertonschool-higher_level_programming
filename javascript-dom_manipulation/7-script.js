const myUl = document.body.querySelector("#list_movies");

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        const films = data.results;
        films.forEach(film => {
            const li = document.createElement('li');
            li.textContent = film.title;
            myUl.appendChild(li);
        });
    })
    .catch(error => {
        console.error('Error:', error);
        myUl.textContent = 'Error fetching movie titles';
    });