#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.getJSON(url, function(data) {
    $('#character').append(data.name)
});