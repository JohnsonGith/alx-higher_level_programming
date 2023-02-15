#!/usr/bin/node
// import the Rectangle class
 const Rectangle = require('./4-rectangle');

// define the Square class that inherits from Rectangle
 class Square extends Rectangle {
   constructor(size) {
       super(size, size);
         }
         }
        export the Square class
         module.exports = Square;

