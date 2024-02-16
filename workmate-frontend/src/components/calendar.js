import "../assets/css/calendar.css";

import React, { useState } from 'react';
import Day from "./day";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChevronLeft, faChevronRight, faHouse } from "@fortawesome/free-solid-svg-icons";
import { Link } from 'react-router-dom';

function getDaysInMonth(month) {
    return new Date(month.getFullYear(), month.getMonth() + 1, 0).getDate();
}
  
function getFirstDayOfMonth(date) {
    return new Date(date.getFullYear(), date.getMonth(), 1);
}

function buildCalendar(currentMonth, selectedDate, setSelectedDate) {
    const daysInMonth = getDaysInMonth(currentMonth);
    const firstDayOfMonth = getFirstDayOfMonth(currentMonth);
    const firstDayOfWeek = firstDayOfMonth.getDay();

    const startingDate = new Date(
        firstDayOfMonth.getFullYear(),
        firstDayOfMonth.getMonth(),
    );

    const calendarGrid = [<p className="day-label">Su</p>, <p className="day-label">Mo</p>, <p className="day-label">Tu</p>, <p className="day-label">We</p>, <p className="day-label">Th</p>, <p className="day-label">Fr</p>, <p className="day-label">Sa</p>];
  
    for (let i = 1 - startingDate.getDay(); i < 43 - startingDate.getDay(); i++) {
      const day = new Date(currentMonth);
      day.setDate(i);
  
      const inCurrentMonth = i >= 1 && i <= daysInMonth;
      calendarGrid.push(
        <Day
          key={day.getTime()}
          date={day}
          isSelected={day.getTime() === selectedDate.getTime()}
          onClick={() => setSelectedDate(day)}
          inCurrentMonth={inCurrentMonth} // Pass boolean directly
        />
      );
    }
  
    return calendarGrid;
}

export function Calendar() {
    const [selectedDate, setSelectedDate] = useState(new Date());
    const [currentMonth, setCurrentMonth] = useState(new Date());
  
    const calendarGrid = buildCalendar(currentMonth, selectedDate, setSelectedDate);
  
    return (
      <div className="container">
      <Link to="/"><FontAwesomeIcon icon={faHouse} /></Link>
      <div className="calendar-header">
            <FontAwesomeIcon icon={faChevronLeft} onClick={() => setCurrentMonth(new Date(currentMonth.getFullYear(), currentMonth.getMonth() - 1, 1))}></FontAwesomeIcon>
          <div className="calendar-title">
            {currentMonth.toLocaleString('en-US', { month: 'long', year: 'numeric' })}
          </div>
            <FontAwesomeIcon icon={faChevronRight} onClick={() => setCurrentMonth(new Date(currentMonth.getFullYear(), currentMonth.getMonth() + 1, 1))}></FontAwesomeIcon>
      </div>
      <div className="calendar-grid">{calendarGrid}</div>
    </div>
    );
}

export default Calendar;