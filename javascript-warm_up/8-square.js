#!/usr/bin/node
const variable = process.argv[2];
if (variable) {
  if (!isNaN(variable)) {
    for (let i = 0; i < variable; i++) {
      let row = '';
      for (let j = 0; j < variable; j++) {
        row += 'X';
      }
      console.log(row);
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
