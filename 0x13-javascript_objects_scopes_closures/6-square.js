#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/**
 * Class Square that defines a square and inherits from Rectangle.
 */
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    this.print(c);
  }
}

module.exports = Square;