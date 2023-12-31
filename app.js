const express = require('express');
const app = express();
const port = 3000;

app.get('/api', (req, res) => {
  const { slack_name, track } = req.query;

  const validTracks = ["frontend", "mobile", "design", "backend"];
  if (!validTracks.includes(track)) {
    return res.status(400).json({ error: "Invalid track parameter" });
  }

  // Get current UTC time with validation of +/-2 hours
  const now = new Date();
  const currentUtcTime = now.toISOString().slice(0, 19) + 'Z';
  const utcOffsetHours = new Date().getTimezoneOffset() / 60;
  if (Math.abs(utcOffsetHours) > 2) {
     return res.status(400).json({ error: "UTC time offset exceeds +/-2 hours" });
   }


  // Other information
  const githubFileUrl = "https://github.com/Prideland-Okoi/endpoints-task/blob/master/app.js";
  const githubRepoUrl = "https://github.com/Prideland-Okoi/endpoints-task";

  // Create the response JSON
  const response = {
    slack_name,
    current_day: new Date().toLocaleDateString('en-US', { weekday: 'long' }),
    utc_time: currentUtcTime,
    track: track,
    github_file_url: githubFileUrl,
    github_repo_url: githubRepoUrl,
    status_code: 200
  };

  res.json(response);
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
