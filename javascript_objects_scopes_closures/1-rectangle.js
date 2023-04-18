#!/usr/bin/node
class Rectangle {
  constructor (width, height) {
    if (!isNaN(width)) {
      this.width = width;
    } else {
      this.width = undefined;
    }
    if (!isNaN(height)) {
      this.height = height;
    } else {
      this.height = undefined;
    }
  }
}

module.exports = Rectangle;
