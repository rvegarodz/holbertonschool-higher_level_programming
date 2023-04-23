#!/usr/bin/node
const url = 'https://stefanbohacek.com/hellosalut/?lang=fr';
$(function () {
    $.getJSON(url, function(data) {
        $('#hello').append(data.hello);
    });
});
