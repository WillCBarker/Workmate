import "../assets/css/calendar.css";

import React, { useState } from 'react';
import Day from "./day";

function getDaysInMonth(month) {
    return new Date(month.getFullYear(), month.getMonth() + 1, 0).getDate();
}
  
function getFirstDayOfMonth(date) {
    return new Date(date.getFullYear(), date.getMonth(), 1);
}
  
function getDayCountSinceFirstSunday(startingDate) {
    // Ensure startingDate is a valid Date object
    if (!(startingDate instanceof Date)) {
        throw new TypeError('startingDate must be a valid Date object');
    }

    const dayOfWeek = startingDate.getDay();
    return dayOfWeek === 0 ? 0 : (7 - dayOfWeek) % 7;
}

function buildCalendar(currentMonth, selectedDate, setSelectedDate) {
    const daysInMonth = getDaysInMonth(currentMonth);
    const firstDayOfMonth = getFirstDayOfMonth(currentMonth);
    const firstDayOfWeek = firstDayOfMonth.getDay();

    const startingDate = new Date(
        firstDayOfMonth.getFullYear(),
        firstDayOfMonth.getMonth(),
    );

    const calendarGrid = [];
  
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
        <button onClick={() => setCurrentMonth(new Date(currentMonth.getFullYear(), currentMonth.getMonth() - 1, 1))}>Previous Month</button>
        <button onClick={() => setCurrentMonth(new Date(currentMonth.getFullYear(), currentMonth.getMonth() + 1, 1))}>Next Month</button>
        <div className="calendar-div">
          <div className="calendar-grid">{calendarGrid}</div>
        </div>
      </div>
    );
}

export default Calendar;