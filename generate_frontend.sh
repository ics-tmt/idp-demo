#!/usr/bin/env bash
set -e

# Scaffold React frontend structure and files
mkdir -p frontend/public frontend/src

# .gitignore
cat > frontend/.gitignore << 'EOF'
node_modules/
build/
EOF

# package.json
cat > frontend/package.json << 'EOF'
{
  "name": "jira-dashboard",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-scripts": "5.0.1",
    "axios": "^0.24.0",
    "recharts": "^2.1.9",
    "react-super-responsive-table": "^5.1.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build"
  }
}
EOF

# public/index.html
cat > frontend/public/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Jira Dashboard</title>
</head>
<body>
  <div id="root"></div>
</body>
</html>
EOF

# src/index.js
cat > frontend/src/index.js << 'EOF'
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
EOF

# src/App.js
cat > frontend/src/App.js << 'EOF'
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Table, Thead, Tbody, Tr, Th, Td } from 'react-super-responsive-table';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend } from 'recharts';
import 'react-super-responsive-table/dist/SuperResponsiveTableStyle.css';

function App() {
  const [data, setData] = useState([]);
  const [jql, setJql] = useState('project = YOUR_PROJECT');

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const res = await axios.get('/jira/metrics', { params: { jql } });
      setData(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Jira Dashboard</h1>
      <div style={{ marginBottom: '20px' }}>
        <input
          type="text"
          value={jql}
          onChange={(e) => setJql(e.target.value)}
          style={{ width: '400px', marginRight: '10px' }}
        />
        <button onClick={fetchData}>Fetch</button>
      </div>
      <Table>
        <Thead>
          <Tr>
            <Th>Issue Type</Th>
            <Th>Priority</Th>
            <Th>Status</Th>
            <Th>Count</Th>
          </Tr>
        </Thead>
        <Tbody>
          {data.map((row, idx) => (
            <Tr key={idx}>
              <Td>{row.issue_type}</Td>
              <Td>{row.priority}</Td>
              <Td>{row.status}</Td>
              <Td>{row.count}</Td>
            </Tr>
          ))}
        </Tbody>
      </Table>
      <BarChart width={600} height={300} data={data} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
        <XAxis dataKey="status" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="count" fill="#8884d8" />
      </BarChart>
    </div>
  );
}

export default App;
EOF