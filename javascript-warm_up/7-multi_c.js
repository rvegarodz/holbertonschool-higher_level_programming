#!/usr/bin/node
const variables = process.argv;
const message = 'C is fun';
if (variables.length <= 2) {
  console.log('Missing number of occurrences');
} else {
  if (isNaN(variables[2])) {
    for (let i = 0; i < variables[2]; i++) {
      console.log(message);
    }
  }
}
