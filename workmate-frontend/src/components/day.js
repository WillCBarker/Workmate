const Day = ({ date, isSelected, onClick, inCurrentMonth }) => {
    const dayNumber = date.getDate();
    const dayName = date.toLocaleDateString('en-US', { weekday: 'short' });
    return (
      <div className={`calendar-day ${isSelected ? 'selected' : ''} ${ !inCurrentMonth ? "not-current-month" : ""}`} onClick={onClick}>
        <span>{dayNumber}</span>
        <span>{dayName}</span>
      </div>
    );
  };

export default Day;