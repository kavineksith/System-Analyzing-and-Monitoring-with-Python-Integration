const fs = require('fs');
const fsPromises = require('fs').promises;
const path = require('path');

const logEvents = async (message, logName) => {
    try {
        if (!fs.existsSync(path.join(__dirname, '..', 'logs'))) {
            await fsPromises.mkdir(path.join(__dirname, '..', 'logs'));
        }

        await fsPromises.appendFile(path.join(__dirname, '..', 'logs', logName), message);
    } catch (err) {
        console.log(err);
    }
}
// Logging middleware
const logger = (req, res, next) => {
    logEvents(`${new Date().toISOString()} - ${req.method}\t${req.headers.origin}\t${req.originalUrl}\t${req.url}\t${req.ip}\t${req.path}`, 'reqLog.txt');
    next();
}

module.exports = { logger, logEvents };
