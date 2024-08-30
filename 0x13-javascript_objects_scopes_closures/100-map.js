#!/usr/bin/node
/* imports an array and computes a new array  */
const array = require('./100-data').list;
console.log(array);
console.log(array.map((item, list) => item * list));
