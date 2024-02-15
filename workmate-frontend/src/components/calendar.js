import "../assets/css/calendar.css";

import React, { useState } from 'react';
import Day from "./day";

// Define a helper function to get the number of days in a month
function getDaysInMonth(month) {
    return new Date(month.getFullYear(), month.getMonth() + 1, 0).getDate();
}

export function Calendar() {
    const [selectedDate, setSelectedDate] = useState(new Date());
    const [currentMonth, setCurrentMonth] = useState(new Date());
    const day = new Date(currentMonth);
    const dayNumber = day.getDate();
    const daysInMonth = getDaysInMonth(currentMonth);
    const calendarGrid = [];
    for (let i = 0; i < daysInMonth-dayNumber; i++) {
        const day = new Date(currentMonth); // Create a new Date object for each day
        day.setDate(dayNumber + i);
        calendarGrid.push(
        <Day key={day.getTime()} date={day} isSelected={day.getTime() === selectedDate.getTime()} onClick={() => setSelectedDate(day)} />
        );
    }

    return (
        <div class="container">
            <div className="calendar-grid">
                {calendarGrid}
            </div>
        </div>
    );
}

export default Calendar;