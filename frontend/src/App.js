import "./App.css";
import { useState, useEffect } from "react";
import CAL from "./CalendarView";
import Calendar from './Calendar.js';
import TimeRangeInput from "./TimeRangeInput";

function App() {
  const [data, setData] = useState(null);
  const [click, setClick] = useState(true);
  const [viewEvents, setViewEvents] = useState(null);
  const [freeTime, setFreeTime] = useState(null);

  const host_name = "http://localhost:8000/";
  useEffect(() => {
    fetch(host_name + "update.py/api_to_json", {
      method: "Get",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, [click]);

  return (
    <div className="App">
      <h3>data</h3>
      {viewEvents ? <CAL viewEvents={viewEvents}/> : null}
      <Calendar setViewEvents={setViewEvents}/>
      <button onClick={() => setClick(~click)}>GET IT KING</button>
      <h2>
        Enter time ranges that you can go to the gym below in this format
        <h3>HH:MM AM/PM-HH:MM AM/PM</h3>
      </h2>
      <TimeRangeInput/>
    </div>
  );
}

export default App;
