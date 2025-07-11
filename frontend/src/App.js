import React, { useState } from 'react';
import TicketsDashboard from './components/TicketsDashboard';

function App() {
  const [jql, setJql] = useState('project = MYPROJECT');
  const [data, setData] = useState([]);

  const handleFetch = () => {
    fetch(`/jira-summary?jql=${encodeURIComponent(jql)}`)
      .then((res) => res.json())
      .then(setData)
      .catch(console.error);
  };

  return (
    <div className="App">
      <h1>Jira Tickets Summary</h1>
      <div style={{ marginBottom: '1rem' }}>
        <input
          type="text"
          value={jql}
          onChange={(e) => setJql(e.target.value)}
          style={{ width: '300px', marginRight: '0.5rem' }}
        />
        <button onClick={handleFetch}>Fetch</button>
      </div>
      <TicketsDashboard data={data} />
    </div>
  );
}

export default App;