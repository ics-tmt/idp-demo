(() => {
  const e = React.createElement;

  function App() {
    const [ticketsJson, setTicketsJson] = React.useState(
      '[{"id":"T1","story":"ST-1"},{"id":"T2","story":"ST-1"},{"id":"T3","story":"ST-2"}]'
    );
    const [counts, setCounts] = React.useState({});
    const [error, setError] = React.useState(null);

    const handleSubmit = async () => {
      setError(null);
      try {
        const tickets = JSON.parse(ticketsJson);
        const response = await fetch('/jira/story-count', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ tickets }),
        });
        if (!response.ok) {
          const data = await response.json();
          throw new Error(data.detail || 'Error fetching data');
        }
        const data = await response.json();
        setCounts(data);
        drawChart(data);
      } catch (err) {
        setError(err.message);
      }
    };

    const drawChart = (data) => {
      const ctx = document.getElementById('chart').getContext('2d');
      if (window.myChart) {
        window.myChart.destroy();
      }
      window.myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: Object.keys(data),
          datasets: [
            {
              label: 'Ticket Count',
              data: Object.values(data),
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1,
            },
          ],
        },
        options: {
          scales: {
            y: { beginAtZero: true, precision: 0 },
          },
        },
      });
    };

    return e(
      'div',
      { style: { padding: '20px', fontFamily: 'Arial, sans-serif' } },
      e('h1', {}, 'Jira Story Ticket Counts'),
      e('textarea', {
        rows: 6,
        cols: 60,
        value: ticketsJson,
        onChange: (evt) => setTicketsJson(evt.target.value),
      }),
      e('br'),
      e(
        'button',
        { onClick: handleSubmit, style: { margin: '10px 0', padding: '8px 16px' } },
        'Compute Counts'
      ),
      error && e('div', { style: { color: 'red' } }, error),
      Object.keys(counts).length > 0 &&
        e(
          'table',
          { border: 1, cellPadding: 5, style: { marginTop: '20px' } },
          e(
            'thead',
            {},
            e('tr', {}, e('th', {}, 'Story'), e('th', {}, 'Count'))
          ),
          e(
            'tbody',
            {},
            Object.entries(counts).map(([story, count]) =>
              e('tr', { key: story }, e('td', {}, story), e('td', {}, count))
            )
          )
        ),
      e('canvas', { id: 'chart', width: 600, height: 300, style: { marginTop: '20px' } })
    );
  }

  ReactDOM.render(e(App), document.getElementById('root'));
})();
