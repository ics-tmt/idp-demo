import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import 'chart.js/auto';

function App() {
  const [counts, setCounts] = useState({});

  useEffect(() => {
    fetch('/count_by_story', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        tickets: [
          { id: 'T1', story: 'Story A' },
          { id: 'T2', story: 'Story B' },
          { id: 'T3', story: 'Story A' },
        ],
      }),
    })
      .then((res) => res.json())
      .then((data) => setCounts(data.counts))
      .catch((err) => console.error(err));
  }, []);

  const stories = Object.keys(counts);
  const values = stories.map((s) => counts[s]);

  const data = {
    labels: stories,
    datasets: [
      {
        label: 'Ticket Count',
        data: values,
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
      },
    ],
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>JIRA Tickets Broken Down by Story</h1>
      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>Story</th>
            <th>Count</th>
          </tr>
        </thead>
        <tbody>
          {stories.map((story) => (
            <tr key={story}>
              <td>{story}</td>
              <td>{counts[story]}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div style={{ maxWidth: '600px', marginTop: '40px' }}>
        <Bar data={data} />
      </div>
    </div>
  );
}

export default App;
