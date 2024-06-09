const sqlite3 = require('sqlite3').verbose();
const DBSource = './monitoring_tool/systemDB.db';

const db = new sqlite3.Database(DBSource, (err) => {
    if (err) {
        console.error(err.message);
        throw err;
    } else {
        console.log('Connected to the SQlite3 Database...!!')
    }
});

module.exports = db;