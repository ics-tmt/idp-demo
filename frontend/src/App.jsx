import React, { useState, useEffect } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

const App = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("/tickets/summary", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify([]),
    })
      .then((res) => res.json())
      .then((resData) => {
        const summary = resData.summary || {};
        const chartData = Object.keys(summary).map((key) => ({
          story: key,
          count: summary[key],
        }));
        setData(chartData);
      })
      .catch((err) => console.error(err));
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>Jira Tickets Summary by Story</h1>
      <table border="1" cellPadding="8" cellSpacing="0">
        <thead>
          <tr>
            <th>Story</th>
            <th>Count</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr key={item.story}>
              <td>{item.story}</td>
              <td>{item.count}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div style={{ width: "100%", height: 300, marginTop: 40 }}>
        <ResponsiveContainer>
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="story" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="count" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default App;
