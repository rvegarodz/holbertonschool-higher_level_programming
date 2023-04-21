#!/usr/bin/node
const input = process.argv[2];
const request = require('request');
request.get(input).on('response', function (response) {
  console.log('code: ' + response.statusCode);
});
