var ru = require('../../radic-util');
describe("Config", function () {
    var defaultConfig = {
        foo: 'bar',
        fooNum: 1,
        fooBool: true
    };
    var config = new ru.Config(defaultConfig);
    beforeEach(function () {
        config = new Config({ foo: 'bar' });
    });
    describe('When creating', function () {
        it('should accept defaults', function () {
            expect(config.get('foo')).toEqual('bar');
        });
        it('can override defaults', function () {
            config.set('foo', 'foobar');
            expect(config.get('foo')).toEqual('foobar');
        });
        it('can process values from defaults', function () {
            config.set('barfoo', 'is:<%= foo %>');
            expect(config.get('barfoo')).toEqual('is:bar');
        });
    });
    describe('Dot notation', function () {
        it('can deeply set values using dot notation', function () {
            config.set('a.deeply.set.value', 'foo');
            expect(config.get('a.deeply.set.value')).toEqual('foo');
        });
        it('can set deep json structures and get them using dot notation', function () {
            config.set('a.deeply.set', { json: { structure: 'foo' }, bar: 'foobar' });
            expect(config.get('a.deeply.set.json.structure')).toEqual('foo');
            expect(config.get('a.deeply.set.bar')).toEqual('foobar');
        });
    });
    describe('Object structures and advanced processing', function () {
        var advancedStructure = {
            foo: 'bar',
            level2: {
                boolbar: true,
                foonum: 123,
                regexbar: /asdf/gm,
            },
            process: '<%= path.to.config.level2 %>'
        };
        beforeEach(function () {
            config.set('path.to.config', advancedStructure);
        });
        it("should be able to set object strutures", function () {
            expect(config.get('path.to.config.foo')).toEqual('bar');
        });
        it('should be able to get object structures', function () {
            expect(config.get('path.to.config.level2')).toEqual(advancedStructure.level2);
        });
        it('should parse object structures into itself', function () {
            var expected = advancedStructure;
            expected.process = advancedStructure.level2;
            expect(config.get('path.to.config')).toEqual(expected);
        });
    });
    //
    // describe("when song has been paused", function() {
    //     beforeEach(function() {
    //         player.play(song)
    //         player.pause()
    //     })
    //
    //     it("should indicate that the song is currently paused", function() {
    //         expect(player.isPlaying).toBeFalsy()
    //
    //         // demonstrates use of 'not' with a custom matcher
    //         expect(player).not.toBePlaying(song)
    //     })
    //
    //     it("should be possible to resume", function() {
    //         player.resume()
    //         expect(player.isPlaying).toBeTruthy()
    //         expect(player.currentlyPlayingSong).toEqual(song)
    //     })
    // })
    //
    // // demonstrates use of spies to intercept and test method calls
    // it("tells the current song if the user has made it a favorite", function() {
    //     spyOn(song, 'persistFavoriteStatus')
    //
    //     player.play(song)
    //     player.makeFavorite()
    //
    //     expect(song.persistFavoriteStatus).toHaveBeenCalledWith(true)
    // })
    //
    // //demonstrates use of expected exceptions
    // describe("#resume", function() {
    //     it("should throw an exception if song is already playing", function() {
    //         player.play(song)
    //
    //         expect(function() {
    //             player.resume()
    //         }).toThrowError("song is already playing")
    //     })
    // })
});
//# sourceMappingURL=configSpec.js.map