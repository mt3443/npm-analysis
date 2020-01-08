var changes = require('concurrent-couch-follower');
var typosquatting = require('./typosquatting')

// NPM CouchDB on_change function, pass to typosquatting detector
var dataHandler = function(data, done) {
    process.stdout.clearLine();
    process.stdout.cursorTo(0);
    process.stdout.write(data.seq.toString());
    typosquatting.detect_typosquatting(data.id);
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