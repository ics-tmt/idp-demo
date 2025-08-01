import React, { useEffect, useState } from "react";
import StoriesTable from "./components/StoriesTable";
import StoriesChart from "./components/StoriesChart";

function App() {
  const [stories, setStories] = useState([]);
  const [projectKey, setProjectKey] = useState("PROJ");

  useEffect(() => {
    fetch(`/stories/${projectKey}`)
      .then((res) => res.json())
      .then(setStories)
      .catch(console.error);
  }, [projectKey]);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Jira Stories Subtask Counts</h1>
      <div style={{ marginBottom: "10px" }}>
        <label htmlFor="project-key">Project Key: </label>
        <input
          id="project-key"
          value={projectKey}
          onChange={(e) => setProjectKey(e.target.value)}
        />
      </div>
      <StoriesTable stories={stories} />
      <StoriesChart stories={stories} />
    </div>
  );
}

export default App;
