#!/usr/bin/node
/* Script that prints the number of Star Wars movies
 * where the character "Wedge Antilles" is present
 */

const request = require('request');
// Imports request module

if (process.argv.length !== 3) {
  process.exit(1);
}
/* process.argv helps us access command line args.
 * The Ist two elements are for the executable path & script name,
 * so start writing from index 2, error if index=3
 */

const url = process.argv[2];
const characterId = 18;

request(url, (error, response, body) => {
  if (!error) {
    try {
      const filmsData = JSON.parse(body).results;

      // Filter films where "Wedge Antilles" is present
      const filmsWithWedge = filmsData.filter((film) =>
        film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
      );

      // Print the number of films with "Wedge Antilles"
      console.log(`${filmsWithWedge.length}`);
    } catch (parseError) {
      console.error(parseError.message);
    }
  } else {
    console.error('Error fetching data from API:', error || `Status Code: ${response.statusCode}`);
  }
});
