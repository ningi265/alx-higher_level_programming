#!/usr/bin/node
/** a class Rectangle that defines a rectangle */
module.exports = class Rectangle {
  #temp;

  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rec = [];
      for (let j = 0; j < this.width; j++) {
        rec += 'X';
      }
      console.log(rec);
    }
  }

  rotate () {
    this.#temp = this.height;
    this.height = this.width;
    this.width = this.#temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
