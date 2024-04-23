#!/usr/bin/node

// Writes a string to a file

const filePath = process.argv[2];
const textString = process.argv[3];
const fs = require('fs');

try {
  fs.writeFileSync(filePath, textString, 'utf-8');
} catch (err) {
  console.error(err);
}
