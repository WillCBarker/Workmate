import React from 'react';
import '../assets/css/navboxes.css';
import { Link } from 'react-router-dom';

export function Navboxes() {

    return (
        <ul>
            <li>
                <Link to="/calendar">
                    <i className="Calendar"></i>
                    <div className="calendar-icon" />
                </Link>
                <label className="hide">Calendar</label>
            </li>
            <li>
                <a href="#">
                <i className="Today"></i>
                </a>
                <label className="hide">Today</label>
                </li>
            <li>
                <a href="#">
                <i className="Notes"></i>
                </a>
                <label className="hide">Notes</label>
            </li>
            <li>
                <a href="#">
                <i className="Reminders"></i>
                </a>
                <label className="hide">Reminders</label>
            </li>
            <li>
                <a href="#">
                <i className="Tool Suite"></i>
                </a>
                <label className="hide">Tool Suite</label>
            </li>
        </ul>
    )
}


export default Navboxes;