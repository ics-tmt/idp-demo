import React, { useState } from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";
import "./App.css";

function App() {
  const [tickets, setTickets] = useState("");
  const [data, setData] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const ticketsArr = JSON.parse(tickets);
      const response = await fetch("http://localhost:8000/tickets_by_story", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(ticketsArr),
      });
      const result = await response.json();
      const chartData = Object.entries(result).map(([story, count]) => ({ story, count }));
      setData(chartData);
    } catch (err) {
      alert("Invalid JSON or server error");
      console.error(err);
    }
  };

  return (
    <div className="App">
      <h1>JIRA Tickets Broken by Stories</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          rows="10"
          cols="50"
          placeholder='Paste JIRA tickets JSON here'
          value={tickets}
          onChange={(e) => setTickets(e.target.value)}
        />
        <br />
        <button type="submit">Submit</button>
      </form>
      {data.length > 0 && (
        <>
          <table>
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
          <BarChart width={600} height={300} data={data}>
            <CartesianGrid stroke="#ccc" />
            <XAxis dataKey="story" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="count" fill="#8884d8" />
          </BarChart>
        </>
      )}
    </div>
  );
}

export default App;

