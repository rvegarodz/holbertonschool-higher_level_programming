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
}

module.exports = Rectangle;
