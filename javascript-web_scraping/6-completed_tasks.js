#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const dict = {};
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const results = JSON.parse(body);
  for (const result of results) {
    if (result.completed === true) {
      if (dict[result.userId]) {
        dict[result.userId]++;
      } else {
        dict[result.userId] = 1;
      }
    }
  }
  console.log(dict);
});
