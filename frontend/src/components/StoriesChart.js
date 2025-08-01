import React from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

function StoriesChart({ stories }) {
  return (
    <BarChart width={600} height={300} data={stories} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="key" />
      <YAxis />
      <Tooltip />
      <Bar dataKey="subtask_count" fill="#8884d8" />
    </BarChart>
  );
}

export default StoriesChart;
