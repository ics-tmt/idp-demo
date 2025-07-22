import React, { useEffect, useState } from 'react';
import TicketTable from './components/TicketTable';
import TicketChart from './components/TicketChart';

function App() {
  const [counts, setCounts] = useState({});

  const sampleTickets = [
    { id: 'T1', story_id: 'S1' },
    { id: 'T2', story_id: 'S1' },
    { id: 'T3', story_id: 'S2' },
  ];

  useEffect(() => {
    fetch('/jira/count', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(sampleTickets),
    })
      .then((res) => res.json())
      .then(setCounts)
      .catch(console.error);
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>Jira Tickets by Story</h1>
      <TicketTable data={counts} />
      <TicketChart data={counts} />
    </div>
  );
}

export default App;
