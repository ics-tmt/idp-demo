import React from 'react';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function StoryChart({ data }) {
  const labels = data.map((item) => item.story);
  const counts = data.map((item) => item.subtask_count);
  const chartData = {
    labels,
    datasets: [
      {
        label: 'Subtask Count',
        data: counts,
        backgroundColor: 'rgba(75,192,192,0.6)',
      },
    ],
  };
  return (
    <div style={{ maxWidth: '600px', marginTop: '20px' }}>
      <Bar data={chartData} />
    </div>
  );
}

export default StoryChart;
