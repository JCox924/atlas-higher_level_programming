$(document).ready(function() {
    $.ajax({
        url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
        method: 'GET',
        success: function(data) {
            $('#character').text(data.name);
        },
        error: function() {
            $('#character').text('Error fetching character name.');
        }
    });
});
