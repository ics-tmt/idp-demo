const { useState, useEffect } = React;
const {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer
} = Recharts;

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('/jira/tickets_by_story')
      .then(response => {
        const items = response.data;
        const formatted = Object.entries(items).map(([story, count]) => ({ story, count }));
        setData(formatted);
      })
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    React.createElement('div', { style: { padding: '20px' } },
      React.createElement('h1', null, 'Jira Tickets by Story'),
      React.createElement('table', null,
        React.createElement('thead', null,
          React.createElement('tr', null,
            React.createElement('th', null, 'Story'),
            React.createElement('th', null, 'Ticket Count')
          )
        ),
        React.createElement('tbody', null,
          data.map(item => (
            React.createElement('tr', { key: item.story },
              React.createElement('td', null, item.story),
              React.createElement('td', null, item.count)
            )
          ))
        )
      ),
      React.createElement('div', { style: { width: '100%', height: 400, marginTop: 50 } },
        React.createElement(ResponsiveContainer, null,
          React.createElement(BarChart, { data },
            React.createElement(CartesianGrid, { strokeDasharray: '3 3' }),
            React.createElement(XAxis, { dataKey: 'story' }),
            React.createElement(YAxis, null),
            React.createElement(Tooltip, null),
            React.createElement(Legend, null),
            React.createElement(Bar, { dataKey: 'count', fill: '#8884d8' })
          )
        )
      )
    )
  );
}

ReactDOM.render(
  React.createElement(App),
  document.getElementById('root')
);
