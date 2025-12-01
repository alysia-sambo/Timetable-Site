import React, { useState, useEffect } from 'react';
import axios from 'axios';


function App() {
  const [trips, setTrips] = useState([]);
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/departing/')
      .then(response => {
        setTrips(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the departing trips!", error);
      });
  }, []);
  return (
    <div className="App">
      <h1>Upcoming Departures</h1>

      {Object.entries(trips).map(([stopId, stopData]) => (
        <div key={stopId}>
          <h2>{stopData.stop_name} ({stopId})</h2>

          {stopData.trips.length === 0 ? (
            <p>No upcoming departures</p>
          ) : (
            <ul>
              {stopData.trips.map((trip, i) => (
                <li key={i}>
                  <strong>{trip.route}</strong>  
                  &nbsp;at&nbsp; 
                  {trip.time}
                </li>
              ))}
            </ul>
          )}

          <hr />
        </div>
      ))}
    </div>
  );
}
export default App;
