const express = require("express");
const app = express();

app.use(express.json({ limit: "500mb" }));

app.get("/process", (req, res) => {
    res.json({
      language: "node",
      message: "GET /process is alive"
    });
  });
  

app.post("/process", (req, res) => {
  res.json({
    language: "node",
    message: "Processed successfully"
  });
});

app.listen(8003, () => {
  console.log("Node service running on port 8003");
});