#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.getJSON(url, function(data) {
    for (film of data.results) {
        var newItem = $("<li>").text(film.title);
        $('#list_movies').append(newItem)
    };
});