import React from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';

function TicketChart({ data }) {
  const chartData = Object.entries(data).map(([story, count]) => ({ story, count }));
  return (
    <BarChart width={600} height={300} data={chartData}>
      <CartesianGrid stroke="#ccc" />
      <XAxis dataKey="story" />
      <YAxis />
      <Tooltip />
      <Bar dataKey="count" fill="#8884d8" />
    </BarChart>
  );
}

export default TicketChart;
