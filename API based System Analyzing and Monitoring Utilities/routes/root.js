const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
    res.status(200).json({
        'message': 'Welcome to System Monitor API'
    });
});

router.all('*', (req, res) => {
    res.status(404).json({
        'error': 'Page not found'
    });
});

module.exports = router;