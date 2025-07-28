import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from 'recharts';

function App() {
  const [ticketsJson, setTicketsJson] = useState(
    '[{"id":"T1","story":"S1"},{"id":"T2","story":"S1"},{"id":"T3","story":"S2"}]'
  );
  const [counts, setCounts] = useState([]);

  const handleFetch = () => {
    try {
      const tickets = JSON.parse(ticketsJson);
      axios
        .post('http://localhost:8000/jira/story_counts', tickets)
        .then((response) => {
          const data = Object.entries(response.data).map(([story, count]) => ({ story, count }));
          setCounts(data);
        })
        .catch((error) => {
          console.error(error);
          alert('Error fetching data');
        });
    } catch (e) {
      alert('Invalid JSON');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Jira Ticket Count by Story</h1>
      <textarea
        rows={6}
        cols={50}
        value={ticketsJson}
        onChange={(e) => setTicketsJson(e.target.value)}
      />
      <br />
      <button onClick={handleFetch}>Fetch Counts</button>
      {counts.length > 0 && (
        <>
          <h2>Table</h2>
          <table border="1" cellPadding="5">
            <thead>
              <tr>
                <th>Story</th>
                <th>Count</th>
              </tr>
            </thead>
            <tbody>
              {counts.map((item) => (
                <tr key={item.story}>
                  <td>{item.story}</td>
                  <td>{item.count}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <h2>Chart</h2>
          <BarChart width={600} height={300} data={counts}>
            <CartesianGrid stroke="#ccc" />
            <XAxis dataKey="story" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="count" fill="#8884d8" />
          </BarChart>
        </>
      )}
    </div>
  );
}

export default App;
