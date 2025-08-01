import React from "react";

function StoriesTable({ stories }) {
  return (
    <table border="1" cellPadding="5" cellSpacing="0">
      <thead>
        <tr>
          <th>Key</th>
          <th>Summary</th>
          <th>Subtask Count</th>
        </tr>
      </thead>
      <tbody>
        {stories.map((s) => (
          <tr key={s.key}>
            <td>{s.key}</td>
            <td>{s.summary}</td>
            <td>{s.subtask_count}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default StoriesTable;
