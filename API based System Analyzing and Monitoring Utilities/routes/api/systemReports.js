const express = require('express');
const router = express.Router();
const systemReportsController = require('../../controllers/systemReportsController.js');

router.route('/')
    .get(systemReportsController.searchWithoutID);

router.route('/:id')
    .get(systemReportsController.searchWithID);

module.exports = router;