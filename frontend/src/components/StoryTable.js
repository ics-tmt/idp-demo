import React from 'react';

function StoryTable({ data }) {
  return (
    <table border="1" cellPadding="5" cellSpacing="0">
      <thead>
        <tr>
          <th>Story</th>
          <th>Subtask Count</th>
        </tr>
      </thead>
      <tbody>
        {data.map(({ story, subtask_count }) => (
          <tr key={story}>
            <td>{story}</td>
            <td>{subtask_count}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default StoryTable;
