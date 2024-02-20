#!/usr/bin/node
/* Script that reads and prints the content of a file.
 * where file is passed as command line arg
 */

const fs = require('fs');
//  Imports the built-in Node.js fs module

if (process.argv.length < 3) {
  process.exit(1);
}
/* process.argv helps us access command line args.
 * The Ist two element are for executable path & script name
 * so start reading from index 2
 */

const filename = process.argv[2];

fs.readFile(filename, 'utf8', (err, data) => {
// fs.readFile method to read the content of the file

  if (err) {
    console.error(err);
    return;
// If error, it logs error message to console
  }

// If reading is successful, log the content to the console
  console.log(data);
});
