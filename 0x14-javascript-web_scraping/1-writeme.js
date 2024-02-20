#!/usr/bin/node
/* Script that writes a string to a file.
 * where file is passed as command line arg
 */

const fs = require('fs');
//  Imports the built-in Node.js fs module

if (process.argv.length !== 4) {
  process.exit(1);
}
/* process.argv helps us access command line args.
 * The Ist two element are for executable path & script name
 * so start writing from index 2
 */

const filename = process.argv[2];
const content = process.argv[3];

fs.writeFile(filename, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log(`${filename}`);
// fs.writeFile method to write the content of the file
});
