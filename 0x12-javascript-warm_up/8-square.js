#!/usr/bin/node
/* a script that prints square */
const size = process.argv[2];

if (size === undefined || isNaN(parseInt(size))) {
  console.log('Missing size');
} else {
  for (let l = 0; l < size; l++) {
    let row = '';
    for (let w = 0; w < size; w++) {
      row += 'X';
    }
    console.log(row);
  }
}
