#!/usr/bin/node
const id = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/';
const request = require('request');
request.get(url + id, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const results = JSON.parse(body);
  console.log(results.title);
});
