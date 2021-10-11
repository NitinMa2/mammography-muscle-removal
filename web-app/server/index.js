const express = require("express"); // express server
const cors = require("cors"); // allows the client to communicate with the server
const morgan = require("morgan"); // used to log http requests to the console
const path = require("path"); // for relative paths
const port = process.env.PORT || 5000; // use port specified by system or fallback to 8080
const app = express(); // instantiate server

// middleware
app.use(
    history({
        verbose: true,
    })
);
app.use(morgan("tiny"));
app.use(cors());
app.use(express.json()); // allows us to parse incoming json
app.use(
    express.urlencoded({
        extended: true,
    })
);

// handling api calls to backend
const segmentation = require("./routes/api/segmentation");
app.use("/api/segmentation", segmentation);

// handle production
if (process.env.NODE_ENV === "production") {
    // static folder
    app.use(express.static(path.join(__dirname, "/public/")));

    // handle SPA
    app.get(/.*/, (req, res) => res.sendFile(__dirname + "public/index.html"));
}

app.listen(port, () => {
    console.log("App listening at http://localhost:" + port);
});
