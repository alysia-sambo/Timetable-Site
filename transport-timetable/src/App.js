import React, { useState, useEffect } from 'react';
import axios from 'axios';


function App() {
  const [tasks, setTasks] = useState([]);
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/stops/')
      .then(response => {
        setTasks(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the stops!", error);
      });
  }, []);
  return (
    <div className="App">
      <h1>Stop List</h1>
      <ul>
        {tasks.map(stop => (
          <li key={stop.id}>
            <h3>{stop.name}</h3>
            <p>{stop.description}</p>
            <p>Stop Code: {stop.code}</p>
            <p>Transport Type: {stop.type}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
export default App;
