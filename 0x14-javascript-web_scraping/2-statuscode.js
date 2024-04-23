#!/usr/bin/node
// displays the status of a GET request

const request = require('request');
const requestURL = process.argv[2];

request(requestURL, function (error, response) {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code: ', response && response.statusCode);
});
