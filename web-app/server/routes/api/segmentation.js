const express = require("express"); // express server
const { MongoClient } = require("mongodb"); // mongodb
require("dotenv").config(); // for accessing env variables

const router = express.Router();

// Get
router.get("/", async (req, res) => {
    const segmentation = await loadSegmentationCollection();
    res.send(await segmentation.find({}).toArray());
});

// Post
router.post("/", async (req, res) => {
    const segmentation = await loadSegmentationCollection();
    await segmentation.insertOne({
        text: req.body.text || "Test Text",
        createdAt: new Date(),
    });
    res.status(201).send();
});

async function loadSegmentationCollection() {
    const uri = `${process.env.VUE_APP_MONGO_URI}`;

    const dbName = "test_db";
    const colName = "test_col";

    // connect to Mongo client
    const client = await MongoClient.connect(uri, {
        useNewUrlParser: true,
        useUnifiedTopology: true,
    });

    if (client) console.log("Successfully connected to DB.");

    return client.db(dbName).collection(colName);
}

module.exports = router;
