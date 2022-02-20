import "./App.css";
import { useState, useEffect } from "react";
import CAL from "./CalendarView";

function App() {
  const [data, setData] = useState(null);
  const [click, setClick] = useState(true);
  const host_name = "http://localhost:8000/";
  useEffect(() => {
    fetch(host_name + "update.py/api_to_json", {
      method: "Get",
      mode: "cors",
      headers: {
        'Content-Type': 'application/json'
      },
    })
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.log(error)
    });
  }, [click]);

  return (
    <div className="App">
      <h3>data</h3>
      <CAL/>
      <button onClick={() => setClick(~click)}>GET IT KING</button>
    </div>
  );
}

export default App;
