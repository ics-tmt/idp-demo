import React, { useEffect, useState } from 'react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from 'recharts';

function App() {
  const [data, setData] = useState([]);
  const [ticketsInput, setTicketsInput] = useState(`[
  {"key": "ABC-1", "issue_type": "Story", "parent": "EPIC-1"},
  {"key": "ABC-2", "issue_type": "Task", "parent": "EPIC-1"},
  {"key": "ABC-3", "issue_type": "Story", "parent": "EPIC-1"},
  {"key": "ABC-4", "issue_type": "Story", "parent": "EPIC-2"}
]`);

  const fetchData = () => {
    let tickets;
    try {
      tickets = JSON.parse(ticketsInput);
    } catch (e) {
      alert('Invalid JSON input');
      return;
    }
    fetch('/story_counts', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(tickets),
    })
      .then((res) => res.json())
      .then((resData) => {
        const chartData = Object.entries(resData).map(([parent, count]) => ({ parent, count }));
        setData(chartData);
      })
      .catch((err) => console.error(err));
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>Jira Story Counts by Parent</h1>
      <textarea
        rows={10}
        cols={80}
        value={ticketsInput}
        onChange={(e) => setTicketsInput(e.target.value)}
      />
      <br />
      <button onClick={fetchData}>Fetch Counts</button>
      <h2>Results</h2>
      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>Parent</th>
            <th>Story Count</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr key={item.parent}>
              <td>{item.parent}</td>
              <td>{item.count}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <h2>Chart</h2>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <XAxis dataKey="parent" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="count" fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default App;
