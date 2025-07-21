import React, { useEffect, useState } from 'react'
import TableView from './components/TableView'
import ChartView from './components/ChartView'

function App() {
  const [data, setData] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch('/tickets/count-by-story')
      .then(res => {
        if (!res.ok) {
          throw new Error('Network response was not ok')
        }
        return res.json()
      })
      .then(data => {
        setData(data)
        setLoading(false)
      })
      .catch(err => {
        setError(err)
        setLoading(false)
      })
  }, [])

  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>

  return (
    <div>
      <h1>Jira Tickets Count by Story</h1>
      <TableView data={data} />
      <ChartView data={data} />
    </div>
  )
}

export default App
