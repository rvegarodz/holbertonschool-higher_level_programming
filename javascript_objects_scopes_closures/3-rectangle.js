#!/usr/bin/node
class Rectangle {
  constructor (width, height) {
    if (!isNaN(width) && !isNaN(height)) {
      if (width > 0 && height > 0) {
        this.width = width;
        this.height = height;
      }
    }
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'X';
        }
        console.log(row);
      }
    }
  }
}

module.exports = Rectangle;
