import "../assets/css/day.css";

const Day = ({ date, isSelected, onClick, inCurrentMonth }) => {
  const dayNumber = date.getDate();

  return (
    <div className={`calendar-day ${isSelected ? 'selected' : ''} ${ !inCurrentMonth ? "not-current-month" : ""}`} onClick={onClick}>
          <div className="day-container">
              <p>{dayNumber}</p>
          </div>
    </div>
  );
};

export default Day;