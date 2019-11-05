var GeohashHeatmap = require('../lib');
var assert = require('assert');
var californiaCities = require('../californiaCities.js');

describe('geohash heatmap', function () {
  it('should add latlong to map', function () {
    var hm = new GeohashHeatmap();
    hm.addLatLong(37.3939829, -122.0802028);
  });

  it('should add several latlongs to map', function () {
    var hm = new GeohashHeatmap();
    hm.addLatLong(37.3939829, -122.0802028); // mountain view
    hm.addLatLong(37.758683, -122.457678); // san francisco - sutro open space preserve
    hm.addLatLong(37.768187, -122.504643); // san francisco - golden gate park
    hm.addLatLong(41.849295, -87.610306); // chicago
  });

  it('query sparse map', function () {
    var hm = new GeohashHeatmap();
    hm.addLatLong(37.3939829, -122.0802028); // mountain view
    assert.equal(hm.getLatLongHeat(37.3939829, -122.0802028, 12).weight, 1);
    assert.equal(hm.getLatLongHeat(37.3939829, -122.0802028, 1).weight, 1);
  });

  it('query denser map', function () {
    var hm = new GeohashHeatmap();
    hm.addLatLong(37.3939829, -122.0802028); // mountain view
    hm.addLatLong(37.758683, -122.457678); // san francisco - sutro open space preserve
    hm.addLatLong(37.768187, -122.504643); // san francisco - golden gate park
    hm.addLatLong(41.849295, -87.610306); // chicago
    assert.equal(hm.getLatLongHeat(37.3939829, -122.0802028, 12).weight, 1);

    // only 3 points on the entire west coast
    assert.equal(hm.getLatLongHeat(37.3939829, -122.0802028, 1).weight, 3);

    // 1 point (in chicago) near the east coast
    assert.equal(hm.getLatLongHeat(23, -90, 1).weight, 1);
  });

  it('should get density at all precision levels', function () {
    var hm = new GeohashHeatmap();
    hm.addLatLong(37.3939829, -122.0802028); // mountain view
    hm.addLatLong(37.758683, -122.457678); // san francisco - sutro open space preserve
    hm.addLatLong(37.768187, -122.504643); // san francisco - golden gate park
    hm.addLatLong(41.849295, -87.610306); // chicago

    const heats = hm.getLatLongHeatAll(37.3939829, -122.0802028);
    assert.equal(Object.keys(heats).length, 12);
    assert.equal(heats[12].weight, 1);
    assert.equal(heats[1].weight, 3);
  });

  it('should work with copy constructor / readonly use-case', function () {
    var hm = new GeohashHeatmap();
    hm.addLatLong(37.3939829, -122.0802028);
    assert.equal(hm.getLatLongHeat(37.3939829, -122.0802028, 12).weight, 1);

    var hm2 = new GeohashHeatmap(hm);
    assert.equal(hm2.getLatLongHeat(37.3939829, -122.0802028, 12).weight, 1);
    hm2.addLatLong(37.3939829, -122.0802028);
    assert.equal(hm2.getLatLongHeat(37.3939829, -122.0802028, 12).weight, 2);
    assert.equal(hm.getLatLongHeat(37.3939829, -122.0802028, 12).weight, 1);
  });

  it('make density map of all cities in california, just for fun', function () {
    var hm = new GeohashHeatmap();
    californiaCities.forEach(function (city) {
      var lat = city[1];
      var lon = city[2];
      hm.addLatLong(lat, lon);
    });
    assert.equal(hm.heatmap['9'].weight, 459);
    assert.equal(hm.heatmap['9q'].weight, 364);
    assert.equal(hm.heatmap['9qh'].weight, 86);
    assert.equal(hm.heatmap['9qhs'].weight, 2);
  });
});
