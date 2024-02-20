#!/usr/bin/node
/* Script that gets the contents of a webpage
 * and stores it in a file
 * the url too request is the Ist cmdline arg passed
 * 2nd arg is the file path to store the body response
 */

const http = require('http');
const fs = require('fs');
//  Imports request fs, http modules

if (process.argv.length !== 4) {
  process.exit(1);
// ensures that user does not pass 3 commandline args
}

const url = process.argv[2];
const fileToStore = process.argv[3];
// Extract the values of the cmdline args

http.get(url, (response) => {
// Initializing a variable to store the received data
  let data = '';

  // Event listener for each chunk of data received in the HTTP response
  response.on('data', (chunk) => {
    data += chunk; // Appends each chunk to data variable
  });

  // Event listener triggered when the entire HTTP response has been received
  response.on('end', () => {
    // Writing the accumulated data to the specified output file
    fs.writeFile(fileToStore, data, (err) => {
      // Callback fxn '(err) => { ... }' triggered after file writing operatn
      if (err) {
        process.exit(1);
        // Handling errors during file writing
      } else {
        // Successful file writing
        console.log();
      }
    });
  });
})
// Event listener for errors during the HTTP request
  .on('error', (error) => {
    console.error(error.message);
  });
