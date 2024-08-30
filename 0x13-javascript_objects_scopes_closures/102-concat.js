#!/usr/bin/node
/* concat 2 files */
const fs = require('fs');
const dataFile1 = fs.readFileSync(process.argv[2], 'utf-8');
const dataFile2 = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFileSync(process.argv[4], dataFile1 + dataFile2);
