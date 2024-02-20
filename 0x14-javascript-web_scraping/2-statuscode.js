#!/usr/bin/node
/* Script that writes a string to a file.
 * where file is passed as command line arg
 */

const request = require('request');
//  Imports request module

if (process.argv.length !== 3) {
  process.exit(1);
}
/* process.argv helps us access command line args.
 * The Ist two element are for executable path & script name
 * so start writing from index 2
 */

const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    console.log('code:', response.statusCode);
  } else {
    console.error('code:', response.statusCode);
  }
});
