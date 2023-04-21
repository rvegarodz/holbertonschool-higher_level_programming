#!/usr/bin/node
const url = process.argv[2];
const fileName = process.argv[3];
const fs = require('fs');

const request = require('request');
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(fileName, body, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
