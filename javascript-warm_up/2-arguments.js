#!/usr/bin/node
const variables = process.argv;
if (variables.length <= 2) {
  console.log('No argument');
} else if (variables.length === 3) {
  console.log('Argument found');
} else if (variables.length > 3) {
  console.log('Arguments founds');
}
