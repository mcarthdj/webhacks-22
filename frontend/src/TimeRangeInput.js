import "./App.css";
import { useState, useEffect } from "react";

function TimeRangeInput({ freeTime, setFreeTime }) {
  const [timeRange, setTimeRange] = useState(null);
  const [day, setDay] = useState(null);
  const [location, setLocation] = useState(null);

  const getBestTime = (baseURL, setFreeTime) => {
    fetch(baseURL + "PATH TO CALL", {
      method: "Get",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((data) => {
        console.log(data);
        setFreeTime(data.body);
      })
      .catch((error) => {
        console.log(error);
        setFreeTime(null);
      });
  };

  const updateTimeRange = (event) => {
    setTimeRange(event.target.value);
  };

  const updateLocation = (event) => {
    setLocation(event.target.value);
  };

  const updateDay = (event) => {
    setDay(event.target.value);
  }

  const submitForm = (event) => {
    event.preventDefault();
    //api call here
    console.log(location, timeRange, day);
    //getBestTime()
    setLocation("");
    setTimeRange("");
  };

  return (
    <form onSubmit={submitForm}>
      <label>
        Pick your level:
        <select value={location} onChange={updateLocation}>
          <option value="Track">Track</option>
          <option value="Level3">Level3</option>
          <option value="Level2">Level2</option>
          <option value="Level1">Level1</option>
          <option value="PowerHouse">PowerHouse</option>
        </select>
      </label>
      <label>
        Pick your day:
        <select value={day} onChange={updateDay}>
          <option value="Monday">Monday</option>
          <option value="Tuesday">Tuesday</option>
          <option value="Wednesday">Wednesday</option>
          <option value="Thursday">Thursday</option>
          <option value="Friday">Friday</option>
          <option value="Saturday">Saturday</option>
          <option value="Sunday">Sunday</option>
        </select>
      </label>
      <label>
        Time ranges:
        <input type="text" value={timeRange} onChange={updateTimeRange} />
      </label>
      <input type="submit" value="Submit" />
    </form>
  );
}

export default TimeRangeInput;
