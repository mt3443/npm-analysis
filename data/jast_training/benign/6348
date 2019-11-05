var Benchmark = require('benchmark');
var suite = new Benchmark.Suite;
var californiaCities = require('../californiaCities.js');
var GeohashHeatmap = require('../lib');

var denseMap = new GeohashHeatmap();
californiaCities.forEach(function (city) {
  var lat = city[1];
  var lon = city[2];
  denseMap.addLatLong(lat, lon);
});

var denseMap2 = new GeohashHeatmap();
californiaCities.forEach(function (city) {
  var lat = city[1];
  var lon = city[2];
  denseMap2.addLatLong(lat, lon);
});

suite.add('create new map', function () {
  var x = new GeohashHeatmap();
})
.add('add to sparse map', function () {
  var hm = new GeohashHeatmap();
  hm.addLatLong(37.3939829, -122.0802028);
})
.add('add to dense map', function () {
  denseMap.addLatLong(37.3939829, -122.0802028);
})
.add('add to dense map using copy constructor', function () {
  var hm = new GeohashHeatmap(denseMap2);
  hm.addLatLong(37.3939829, -122.0802028);
})
.add('query map at precise location', function () {
  denseMap.getLatLongHeat(37.3939829, -122.0802028, 12);
})
.add('query map at fuzzier location', function () {
  denseMap.getLatLongHeat(37.3939829, -122.0802028, 1);
})
.on('cycle', function(event) {
  console.log(String(event.target));
})
.on('complete', function() {
  console.log('Fastest is ' + this.filter('fastest').map('name'));
})
// run async
.run({ 'async': true });
