'use strict'

const mysql = require('mysql');
const connection = mysql.createConnection({
    host: '127.0.0.1',
    user: 'docker',
    password: 'docker',
    database: 'test_database',
});

// Connectionを定義する
connection.connect();

let sql = 'select * from test_database.test_table';
connection.query(sql, (err, rows, fields) => {
    if (err) throw err;
    console.log('test_tableの中身: ', rows);
});

connection.end();
