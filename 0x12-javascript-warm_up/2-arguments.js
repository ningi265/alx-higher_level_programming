#!/usr/bin/node
/* a script that prints a msg depending of the number of args
 */
const argv = process.argv;

if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
