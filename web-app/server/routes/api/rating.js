const { default: axios } = require("axios"); // for api calls
const { MongoClient } = require("mongodb"); // mongodb
require("dotenv").config(); // for accessing env variables
const express = require("express"); // express server

const router = express.Router();

// Post
router.post("/", async (req, res) => {
    const rating = await loadRatingCollection();
    await rating.insertOne({
        rating: req.body.ratingIsGood ? "good" : "bad", // string format of rating
        ratingValue: req.body.ratingIsGood ? 1 : 0, // numeric format of rating
        createdAt: new Date(), // datetime
    });
    res.status(201).send();
});

async function loadRatingCollection() {
    const uri = `${process.env.VUE_APP_MONGO_URI}`;
    const dbName = `${process.env.VUE_APP_MONGO_DB_NAME}`;
    const colName = `${process.env.VUE_APP_MONGO_COLLECTION_NAME}`;

    // connect to Mongo client
    const client = await MongoClient.connect(uri, {
        useNewUrlParser: true,
        useUnifiedTopology: true,
    });

    if (client) console.log("Successfully connected to DB.");

    return client.db(dbName).collection(colName);
}

module.exports = router;
