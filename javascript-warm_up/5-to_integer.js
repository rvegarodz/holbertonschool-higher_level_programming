#!/usr/bin/node
const variables = process.argv;
const error = 'Not a number';
if (variables.length <= 2) {
  console.log(error);
} else {
  if (isNaN(variables[2])) {
    console.log(error);
  } else {
    console.log(variables[2]);
  }
}
