const Day = ({ date, isSelected, onClick }) => {
    const dayNumber = date.getDate();
    const dayName = date.toLocaleDateString('en-US', { weekday: 'short' });
  
    return (
      <div className={`calendar-day ${isSelected ? 'selected' : ''}`} onClick={onClick}>
        <span>{dayNumber}</span>
        <span>{dayName}</span>
      </div>
    );
  };

export default Day;