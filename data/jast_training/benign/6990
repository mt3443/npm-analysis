define([
	"../core",
	"../var/strundefined"
], function( radic, strundefined ) {

var
	// Map over jQuery in case of overwrite
	_radic = window.radic,

	// Map over the $ in case of overwrite
	_R = window.R;

	radic.noConflict = function( deep ) {
	if ( window.r === radic ) {
		window.R = _R;
	}

	if ( deep && window.radic === radic ) {
		window.radic = _radic;
	}

	return radic;
};

// Expose jQuery and $ identifiers, even in
// AMD (#7102#comment:10, https://github.com/jquery/jquery/pull/557)
// and CommonJS for browser emulators (#13566)
if ( typeof noGlobal === strundefined ) {
	window.radic = window.R = radic;
}

});
