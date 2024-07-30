#!/usr/bin/node
// Script to print all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request.get(character, (err, res, bod) => {
        if (err) {
          console.error(err);
        } else {
          console.log(JSON.parse(bod).name);
        }
      });
    });
  }
});
