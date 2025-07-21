import React, { useEffect, useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('/counts?base_url=YOUR_JIRA_URL&username=YOUR_USER&token=YOUR_TOKEN')
      .then((res) => res.json())
      .then((json) => {
        const chartData = Object.entries(json).map(([key, count]) => ({ story: key, count }));
        setData(chartData);
      });
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>Jira Tickets Broken by Stories</h1>
      <table border="1" cellPadding="5" cellSpacing="0">
        <thead>
          <tr>
            <th>Story</th>
            <th>Count</th>
          </tr>
        </thead>
        <tbody>
          {data.map((d) => (
            <tr key={d.story}>
              <td>{d.story}</td>
              <td>{d.count}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div style={{ height: 300, marginTop: 20 }}>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
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
