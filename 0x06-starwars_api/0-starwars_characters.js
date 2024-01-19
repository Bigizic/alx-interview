#!/usr/bin/node

const starWar = (url) => {
  const number = process.argv[2];
  const request = require('request');
  request.get(url, (error, response, body) => {
    if (error) { console.error(error); return; }
    const data = JSON.parse(body);
    for (const items of data.results) {
      if (parseInt(number) === parseInt(items.episode_id)) {
        async function letsWaitForNames () {
          for (const link of items.characters) {
            await new Promise((resolve, reject) => {
              request.get(link, (err, resp, body) => {
                if (err) { reject(err); }
                const name = JSON.parse(body);
                console.log(name.name);
                resolve();
              });
            });
          }
        }
        letsWaitForNames();
      }
    }
  });
};
starWar('https://swapi-api.alx-tools.com/api/films/');
// starWar('https://ezyurl.xyz');
