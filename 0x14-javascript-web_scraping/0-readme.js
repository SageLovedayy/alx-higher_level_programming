#!/usr/bin/node

// Reads and prints the content of a file

const filepath = process.argv[2];
const fs = require('fs');

try {
  const data = fs.readFileSync(filepath, 'utf-8');
  console.log(data);
} catch (err) {
  console.error(err);
}
