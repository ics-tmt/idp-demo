import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from 'recharts';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await axios.get('/api/tickets/broken-by-stories', {
          params: { jql_story: 'type=Sub-task' },
        });
        const formatted = Object.entries(res.data).map(([story, count]) => ({ story, count }));
        setData(formatted);
      } catch (err) {
        console.error(err);
      }
    };
    fetchData();
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>Jira Tickets Broken by Stories</h1>
      <table border="1" cellPadding="5" cellSpacing="0">
        <thead>
          <tr>
            <th>Story</th>
            <th>Ticket Count</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr key={item.story}>
              <td>{item.story}</td>
              <td>{item.count}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div style={{ width: '100%', height: 300, marginTop: 40 }}>
        <ResponsiveContainer>
          <BarChart data={data} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="story" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="count" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export default App;
