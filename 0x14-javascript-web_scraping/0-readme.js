#!/usr/bin/node
const fs = require('fs');

if (process.argv.length < 3) {
  process.exit(1);
}

const filename = process.argv[2];

fs.readFile(filename, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(data);
});
