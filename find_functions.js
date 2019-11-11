var esprima = require('esprima');
var estraverse = require('estraverse');
var fs = require('fs');


function find_functions(contents) {

	var s = new Set()

	var ast = esprima.parse(contents)
	estraverse.traverse(ast, {
		enter: function (node) {
			if (node.type == 'CallExpression') {
				if (node.callee.type == 'Identifier') {
					s.add(node.callee.name);
				} else {
					s.add(node.callee.property.name);
				}
			}
		}
	});

	console.log(s);

}


fs.readFile(process.argv[2], 'utf8', function(err, contents) {
	find_functions(contents);
});

