#!/usr/bin/node
const variables = process.argv;
if (variables.length >= 2) {
  if (!isNaN(variables[2]) && !isNaN(variables[3])) {
    const result = parseInt(variables[2]) + parseInt(variables[3]);
    console.log(result);
  } else {
    console.log(NaN);
  }
} else {
  console.log(NaN);
}
