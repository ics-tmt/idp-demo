import React, { useState } from 'react';
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
  const [data, setData] = useState([]);
  const [tickets, setTickets] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const ticketsArray = JSON.parse(tickets);
      const resp = await axios.post('/tickets/count_by_story', ticketsArray);
      setData(resp.data);
    } catch (err) {
      console.error(err);
      alert('Invalid input or server error');
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Jira Ticket Counter</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          rows={10}
          cols={50}
          value={tickets}
          onChange={(e) => setTickets(e.target.value)}
          placeholder='[{"id":"T1","story_id":"S1"}, ...]'
        />
        <br />
        <button type="submit">Count Tickets</button>
      </form>
      {data.length > 0 && (
        <>
          <h2>Results</h2>
          <table border="1">
            <thead>
              <tr>
                <th>Story ID</th>
                <th>Count</th>
              </tr>
            </thead>
            <tbody>
              {data.map((item) => (
                <tr key={item.story_id}>
                  <td>{item.story_id}</td>
                  <td>{item.count}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <BarChart width={600} height={300} data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="story_id" />
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
