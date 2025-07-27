import React, { useState } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';
import './App.css';

function App() {
  const [data, setData] = useState([]);
  const [projectKey, setProjectKey] = useState('');

  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:8000/jira/story-subtasks', {
        params: { project_key: projectKey },
      });
      setData(response.data);
    } catch (error) {
      console.error('Error fetching data', error);
    }
  };

  return (
    <div className="App">
      <h1>Jira Story Subtask Breakdown</h1>
      <div className="controls">
        <input
          type="text"
          placeholder="Project Key"
          value={projectKey}
          onChange={(e) => setProjectKey(e.target.value)}
        />
        <button onClick={fetchData}>Fetch</button>
      </div>
      {data.length > 0 && (
        <>
          <table>
            <thead>
              <tr>
                <th>Story Key</th>
                <th>Summary</th>
                <th>Subtask Count</th>
              </tr>
            </thead>
            <tbody>
              {data.map((item) => (
                <tr key={item.story_key}>
                  <td>{item.story_key}</td>
                  <td>{item.summary}</td>
                  <td>{item.subtask_count}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <BarChart width={600} height={300} data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="story_key" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="subtask_count" fill="#8884d8" />
          </BarChart>
        </>
      )}
    </div>
  );
}

export default App;
