#!/usr/bin/node
// Script to print all characters of a Star Wars movie in the order provided

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach((characterUrl) => {
      request.get(characterUrl, (err, res, characterBody) => {
        if (err) {
          console.error(err);
        } else {
          console.log(JSON.parse(characterBody).name);
        }
      });
    });
  }
});
