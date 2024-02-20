#!/usr/bin/node
/* Script that prints the title of a Star Wars movie
 * where the episode number matches a given integer
 * episode number is passed as cmd line arg
 */

const request = require('request');
//  Imports request module

if (process.argv.length !== 3) {
  process.exit(1);
}
/* process.argv helps us access command line args.
 * The Ist two element are for executable path & script name
 * so start writing from index 2, error if=index3
 */

const id = parseInt(process.argv[2]);
if (isNaN(id)) {
  process.exit(1);
}

const Apiurl = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(Apiurl, (error, response, body) => {
  if (!error) {
    const filmName = JSON.parse(body);
    console.log(filmName.title);
  } else {
    console.error(error);
  }
});
