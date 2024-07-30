#!/usr/bin/node
// Script to write a string to a file

const fs = require('fs');
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
