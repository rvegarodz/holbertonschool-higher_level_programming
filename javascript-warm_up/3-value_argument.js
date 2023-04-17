#!/usr/bin/node
const variables = process.argv;
if (variables[2]) {
  console.log(variables[2]);
} else {
  console.log('No argument');
}
