var esprima = require('esprima');
var estraverse = require('estraverse');
var fs = require('fs');


function find_functions(contents) {

	var s = new Set()
	var invalid_types = [
		'FunctionExpression',
		'LogicalExpression',
		'AssignmentExpression'
	];

	var ast = esprima.parse(contents)
	estraverse.traverse(ast, {
		enter: function (node) {
			if (node.type == 'CallExpression') {
				if (!invalid_types.includes(node.callee.type)) {
					if (node.callee.type == 'Identifier') {
						s.add(node.callee.name);
					} else if (node.callee.type == 'MemberExpression') {
						s.add(node.callee.property.name);
					}
				}
			}
		}
	});

	var a = Array.from(s);
	var i;
	for (i in a) {
		console.log(a[i]);
	}

}


fs.readFile(process.argv[2], 'utf8', function(err, contents) {
	find_functions(contents);
});

