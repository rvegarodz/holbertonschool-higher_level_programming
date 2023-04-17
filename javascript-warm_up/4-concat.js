#!/usr/bin/node
const variables = process.argv;
if (variables.length <= 2) {
  console.log('undefined is undefined');
} else if (variables.length === 3) {
  console.log(variables[2], 'is undefined');
} else {
  console.log(variables[2], 'is', variables[3]);
}
