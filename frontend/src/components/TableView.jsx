import React from 'react'

export default function TableView({ data }) {
  return (
    <table>
      <thead>
        <tr>
          <th>Story</th>
          <th>Count</th>
        </tr>
      </thead>
      <tbody>
        {data.map(({ story, count }) => (
          <tr key={story}>
            <td>{story}</td>
            <td>{count}</td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}
