#!/usr/bin/node

const Square5 = require('./5-square');
// imports Square class in 5-square.js

class Square extends Square5 {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
// Exporst Square class so that another module can have access to it
