import React, { useEffect, useState } from 'react';
import StoryTable from './components/StoryTable';
import StoryChart from './components/StoryChart';

function App() {
  const [data, setData] = useState([]);
  useEffect(() => {
    fetch('/stories/subtasks-count')
      .then((res) => res.json())
      .then(setData)
      .catch(console.error);
  }, []);
  return (
    <div style={{ padding: '20px' }}>
      <h1>JIRA Story Subtasks Count</h1>
      <StoryTable data={data} />
      <StoryChart data={data} />
    </div>
  );
}

export default App;
