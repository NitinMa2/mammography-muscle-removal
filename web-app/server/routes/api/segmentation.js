const express = require("express"); // express server
const { MongoClient } = require("mongodb"); // mongodb

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
        text: req.body.text,
        createdAt: new Date(),
    });
    res.status(201).send();
});

async function loadSegmentationCollection() {
    const uri =
        "mongodb+srv://admin:adminFYP2021@cluster0.banxa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";

    const dbName = "test";
    const colName = "people";

    const client = await MongoClient.connect(uri, {
        useNewUrlParser: true,
        useUnifiedTopology: true,
    });

    return client.db(dbName).collection(colName);
}

module.exports = router;
