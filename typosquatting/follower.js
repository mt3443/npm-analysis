var changes = require('concurrent-couch-follower');
var typosquatting = require('./typosquatting_follower.js')

// NPM CouchDB on_change function, pass to typosquatting detector
var dataHandler = function(data, done) {
    typosquatting.scan(data.id);
    done();
};

// NPM CouchDB listener settings
var configOptions = {
  db: 'https://replicate.npmjs.com/',
  include_docs: false,
  sequence: '.sequence',
  concurrency: 20
};

// start listener
changes(dataHandler, configOptions);
