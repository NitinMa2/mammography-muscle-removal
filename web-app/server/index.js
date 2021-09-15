const express = require("express"); // express server
const cors = require("cors"); // allows the client to communicate with the server
// const bodyParser = require("body-parser"); // to allow the server to read the data sent from the client
const morgan = require("morgan"); // used to log http requests to the console

const path = require("path"); // for relative paths

const port = process.env.PORT || 5000; // use port specified by system or fallback to 8080
const app = express(); // instantiate server

// middleware
app.use(morgan("tiny"));
app.use(cors());
app.use(express.json()); // allows us to parse incoming json
app.use(
    express.urlencoded({
        extended: true,
    })
);

const segmentation = require("./routes/api/segmentation");

app.use("/api/segmentation", segmentation);

// Handle production
if (process.env.NODE_ENV === "production") {
    // Static folder
    app.use(express.static(path.join(__dirname, "/public/")));

    // Handle SPA
    app.get(/.*/, (req, res) => res.sendFile(__dirname + "public/index.html"));
}

app.listen(port, () => {
    console.log("App listening at http://localhost:" + port);
});
