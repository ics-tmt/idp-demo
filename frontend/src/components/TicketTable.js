import React from 'react';

function TicketTable({ data }) {
  const rows = Object.entries(data);
  return (
    <table border="1" cellPadding="5" cellSpacing="0">
      <thead>
        <tr>
          <th>Story ID</th>
          <th>Ticket Count</th>
        </tr>
      </thead>
      <tbody>
        {rows.map(([story, count]) => (
          <tr key={story}>
            <td>{story}</td>
            <td>{count}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default TicketTable;
