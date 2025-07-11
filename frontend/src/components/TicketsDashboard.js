import React from 'react';
import { Bar } from 'react-chartjs-2';

function TicketsDashboard({ data }) {
  if (!data.length) {
    return <p>No data</p>;
  }

  const tableRows = data.map((item) => (
    <tr key={`${item.issuetype}-${item.priority}-${item.status}`}>
      <td>{item.issuetype}</td>
      <td>{item.priority}</td>
      <td>{item.status}</td>
      <td>{item.count}</td>
    </tr>
  ));

  const issuetypes = [...new Set(data.map((item) => item.issuetype))];
  const priorities = [...new Set(data.map((item) => item.priority))];

  const datasets = priorities.map((priority, idx) => {
    const counts = issuetypes.map((type) =>
      data
        .filter((d) => d.issuetype === type && d.priority === priority)
        .reduce((sum, d) => sum + d.count, 0)
    );
    const colors = ['#FF6384', '#36A2EB', '#FFCE56', '#66BB6A', '#BA68C8'];
    return {
      label: priority,
      data: counts,
      backgroundColor: colors[idx % colors.length],
    };
  });

  const chartData = {
    labels: issuetypes,
    datasets,
  };

  return (
    <div>
      <h2>Tickets Table</h2>
      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>Issue Type</th>
            <th>Priority</th>
            <th>Status</th>
            <th>Count</th>
          </tr>
        </thead>
        <tbody>{tableRows}</tbody>
      </table>
      <h2>Tickets Chart</h2>
      <Bar data={chartData} />
    </div>
  );
}

export default TicketsDashboard;