import React from 'react';
import '../assets/css/navboxes.css';
import { Link } from 'react-router-dom';

export function Navboxes() {

    return (
        <ul>
            <li>
                <Link to="/calendar">
                    <i class="Calendar"></i>
                    <div className="calendar-icon" />
                </Link>
                <label class="hide">Calendar</label>
            </li>
            <li>
                <a href="#">
                <i class="Today"></i>
                </a>
                <label class="hide">Today</label>
                </li>
            <li>
                <a href="#">
                <i class="Notes"></i>
                </a>
                <label class="hide">Notes</label>
            </li>
            <li>
                <a href="#">
                <i class="Reminders"></i>
                </a>
                <label class="hide">Reminders</label>
            </li>
            <li>
                <a href="#">
                <i class="Tool Suite"></i>
                </a>
                <label class="hide">Tool Suite</label>
            </li>
        </ul>
    )
}


export default Navboxes;