$(document).ready(function() {
    $.ajax({
        url: 'https://swapi-api.hbtn.io/api/films/?format=json',
        method: 'GET',
        success: function(data) {
            const movies = data.results;
            for (let i = 0; i < movies.length; i++) {
                $('#list_movies').append('<li>' + movies[i].title + '</li>');
            }
        },
        error: function() {
            $('#list_movies').append('<li>Error fetching movie titles.</li>');
        }
    });
});
