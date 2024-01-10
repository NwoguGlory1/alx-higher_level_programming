#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
//|| isNaN(w) || isNaN(h))
//   this.width = 0;
//    this.height = 0;
