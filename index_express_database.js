var express = require('express');
var app = express();

var mysql      = require('mysql');
var connection = mysql.createConnection({
	host: '127.0.0.1',
	user: 'docker',
	password: 'docker',
	database: 'test_database'
});

app.get('/', function (req, res) {
	let sql = 'select * from test_table';
	connection.query(sql, function (error, results, fields) {
		if (error) throw error;
		// データベースの1行目の参照
		res.send(results[0]);
	});
});

app.listen(3000, function () {
	console.log('Example app listening on port 3000!');
});
