const express = require('express');
const { request, response } = require('express');
const bodyParser = require('body-parser');
const helmet = require('helmet');
const cors = require('cors');
const app = express();

const corsOptions = require('./middleware/corsOptions.js');
const limiter = require('./middleware/rateLimiter.js');
const { logger } = require('./middleware/eventLogger.js');
const errorHandler = require('./middleware/errorLogger.js');

const hostname = '127.0.0.1';
const port = 8080;

app.use(cors(corsOptions));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(helmet());
app.use(limiter);
app.use(logger);
app.use(errorHandler);

app.use('/', require('./routes/root.js'));
app.use('/api', require('./routes/api/systemReports.js'));

app.listen(port, hostname, () => {
    console.log(`Server is running on http://${hostname}:${port}/`);
});