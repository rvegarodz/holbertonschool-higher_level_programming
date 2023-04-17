#!/usr/bin/node
const variables = process.argv;
function factorial (x) {
  if (x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

if (variables.length < 3) {
  console.log(1);
} else {
  console.log(factorial(parseInt(variables[2])));
}
