import "../assets/css/calendar.css";

import React, { useEffect, useState } from 'react';
import Day from "./day";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChevronLeft, faChevronRight, faHouse } from "@fortawesome/free-solid-svg-icons";
import { Link } from 'react-router-dom';


function getDaysInMonth(date) {
  // Returns number of days in month containing the given date
    return new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
}
  

function getFirstDayOfMonth(date) {
  // Returns the first day of the month containing the given date
    return new Date(date.getFullYear(), date.getMonth(), 1);
}


 function fetchTaskData(currentDate) {
  // Fetch all tasks for current user in current month

  const monthParam = "month=" + (currentDate.getMonth() + 1);
  const yearParam = "year=" + (currentDate.getFullYear());
  const apiUrl = "http://127.0.0.1:8000/api/tasks/?" + monthParam + "&" + yearParam;

  return fetch(apiUrl).then(response => response.json());
}


async function buildCalendar(currentDate, selectedDate, setSelectedDate) {
  // Builds and populates calendar grid with annotations and day information

  const daysInMonth = getDaysInMonth(currentDate);
  const firstDayOfMonth = getFirstDayOfMonth(currentDate);
  
  try {
      const data = await fetchTaskData(currentDate);
      console.log("Data: ", data);
      const startingDate = new Date(
          firstDayOfMonth.getFullYear(),
          firstDayOfMonth.getMonth(),
      );

      const calendarGrid = [
          <p className="day-label">Su</p>,
          <p className="day-label">Mo</p>,
          <p className="day-label">Tu</p>,
          <p className="day-label">We</p>,
          <p className="day-label">Th</p>,
          <p className="day-label">Fr</p>,
          <p className="day-label">Sa</p>
      ];

      for (let i = 1 - startingDate.getDay(); i < 43 - startingDate.getDay(); i++) {
          const day = new Date(currentDate);
          const inCurrentMonth = i >= 1 && i <= daysInMonth;
          day.setDate(i);
          calendarGrid.push(
              <Day
                  key={i}
                  date={day}
                  isSelected={day.getTime() === selectedDate.getTime()}
                  onClick={() => setSelectedDate(day)}
                  inCurrentMonth={inCurrentMonth}
              />
          );
      }
      return calendarGrid;
  } catch (error) {
      console.error("Error fetching data:", error);
      return [];
  }
}


export function Calendar() {
  // Base Calendar component

  const [selectedDate, setSelectedDate] = useState(new Date());
  const [currentDate, setCurrentDate] = useState(new Date());
  const [calendarGrid, setCalendarGrid] = useState([]);
  
  useEffect(() => {
      const fetchDataAndBuildCalendar = async () => {
          const grid = await buildCalendar(currentDate, selectedDate, setSelectedDate, 1);
          setCalendarGrid(grid);
      };

      fetchDataAndBuildCalendar();
  }, [currentDate, selectedDate]);

  return (
    <div className="container">
      <Link to="/"><FontAwesomeIcon icon={faHouse} /></Link>
      <div className="calendar-header">
        <FontAwesomeIcon icon={faChevronLeft} onClick={() => setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1))}></FontAwesomeIcon>
        <div className="calendar-title">
          {currentDate.toLocaleString('en-US', { month: 'long', year: 'numeric' })}
        </div>
        <FontAwesomeIcon icon={faChevronRight} onClick={() => setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1))}></FontAwesomeIcon>
      </div>
      <div className="calendar-grid">{calendarGrid.map((gridItem, index) => (
        <div key={index}>{gridItem}</div>
      ))}
      </div>
    </div>
  );
}


export default Calendar;