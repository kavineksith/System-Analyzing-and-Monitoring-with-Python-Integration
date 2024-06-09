const db = require('../database.js');
const GeneralTableSelector = require('../models/generalTableSelector');

const searchWithoutID = (req, res, next) => {
    try {
        const { section } = req.body;

        if (!section) {
            return res.status(404).json({
                'error': 'Section is required'
            });
        }

        const query = GeneralTableSelector(section);

        db.all(query, (err, rows) => {
            if (err) {
                return res.status(400).json({ "error": err.message });
            } else {
                return res.json({
                    "message": "success",
                    "data": rows
                });
            }
        });
    } catch (err) {
        return res.status(400).send(err);
    }
};

const searchWithID = (req, res, next) => {
    try {
        const { id } = req.params;
        const { section } = req.body;

        if (!section) {
            return res.status(404).json({
                'error': 'Section is required'
            });
        }

        const query = GeneralTableSelector(section) + ` WHERE DeviceName = ?`;
        const params = [id];

        db.all(query, params, (err, rows) => {
            if (err) {
                return res.status(400).json({ "error": err.message });
            } else {
                return res.json({
                    "message": "success",
                    "data": rows
                });
            }
        });
    } catch (err) {
        return res.status(400).send(err);
    }
};

module.exports = {
    searchWithoutID,
    searchWithID
};
