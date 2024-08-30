#!/usr/bin/node
/* a class Square that defines a square and inherits from Square
 * of 5-square.js
 */
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let shape = '';
      for (let j = 0; j < this.width; j++) {
        shape += c;
      }
      console.log(shape);
    }
  }
};
