const express = require("express"); // express server
const cors = require("cors"); // allows the client to communicate with the server
// const bodyParser = require("body-parser"); // to allow the server to read the data sent from the client
const morgan = require("morgan"); // used to log http requests to the console

// const path = require("path"); // for relative paths

const port = process.env.PORT || 8080; // use port specified by system or fallback to 8080
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
// app.get("/", (req, res) => {
//     res.json({
//         message: "Behold The MEVN Stack!",
//     });
// });

// Serve all the files in '/dist' directory
// app.use(express.static(path.join(__dirname, "dist")));
// app.use(express.static("dist"));

app.listen(port, () => {
    console.log("App listening at http://localhost:" + port);
});
