#!/usr/bin/node
// Print all characters of a Star Wars movie

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body).characters;
    printCharacters(data, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], (err, resp, body) => {
    if (!err && resp.statusCode === 200) {
      console.log(JSON.parse(body).name);
      // characters MUST be printed recursively not in a for loop
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
