#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let char = '';
    if (typeof c === 'string' || c instanceof String) {
      char = c;
    } else {
      char = 'X';
    }
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += char;
        }
        console.log(row);
      }
    }
  }
}

module.exports = Square;
