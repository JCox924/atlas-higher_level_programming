#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  function printCharacterNames (urls, index = 0) {
    if (index >= urls.length) {
      return;
    }

    request.get(urls[index], (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
      printCharacterNames(urls, index + 1);
    });
  }

  printCharacterNames(characterUrls);
});
