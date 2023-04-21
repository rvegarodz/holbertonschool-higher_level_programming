#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
let count = 0;
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const results = JSON.parse(body);
  for (const film of results.results) {
    for (const characters of film.characters) {
      if (characters.includes(18)) {
        count += 1;
      }
    }
  }
  console.log(count);
});
