#!/usr/bin/node

const starWar = (url) => {
  const request = require('request');
  request.get(url, (error, response, body) => {
    if (error) { console.error(error); return; }
    const data = JSON.parse(body);
    const whatINeed = 'characters';
    const charsLink = data[`${whatINeed}`];
    async function letsWaitForNames () {
      for (const items of charsLink) {
        await new Promise((resolve, reject) => {
          request(items, { json: true }, (err, resp, body) => {
            if (err) { reject(err); return; }
            console.log(body.name);
            resolve();
          });
        });
      }
    }
    letsWaitForNames();
  });
};
const number = process.argv[2];
starWar(`https://swapi-api.alx-tools.com/api/films/${number}`);
// starWar('https://ezyurl.xyz');
