#!/usr/bin/node
/* prints the number of arguments already printesd
 * and the new argument value
 */
let counter = 0;
exports.logMe = function (item) {
  console.log(counter + ': ' + item);
  counter++;
};
