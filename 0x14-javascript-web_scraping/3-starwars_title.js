#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const requestURL = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(requestURL, (err, response) => {
  if (err) return console.log(err);
  if (response.statusCode === 200) {
    const { title } = JSON.parse(response.body);
    return console.log(title);
  }
  console.log(`Error code: ${response.statusCode}`);
});
