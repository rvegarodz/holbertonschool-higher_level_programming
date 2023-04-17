#!/usr/bin/node
const variables = process.argv;
if (variables.length < 4) {
  console.log(0);
} else {
  const array = variables.slice(2);
  const aInt = array.map(str => parseInt(str));
  aInt.sort((a, b) => b - a);
  console.log(aInt[1]);
}
