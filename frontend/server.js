const express = require("express"); // express server
// const path = require("path"); // for relative paths
const port = process.env.PORT || 8080; // use port specified by system or fallback to 8080
const app = express(); // instantiate server

// Serve all the files in '/dist' directory
// app.use(express.static(path.join(__dirname, "dist")));
app.use(express.static("dist"));

app.listen(port, function() {
    console.log("App listening on port " + port);
});
