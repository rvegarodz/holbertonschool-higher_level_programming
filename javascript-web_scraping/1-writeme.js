#!/usr/bin/node
const input = process.argv[2];
const text = process.argv[3];
const fs = require('fs');

fs.writeFile(input, text, (err) => {
  if (err) {
    console.log(err);
  }
});
