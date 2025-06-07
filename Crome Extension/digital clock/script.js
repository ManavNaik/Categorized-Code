// Function to display the current time, date, and day
function updateClock() {
    const now = new Date();
    
    // Time
    let hours = now.getHours();
    let minutes = now.getMinutes();
    let seconds = now.getSeconds();
    
    hours = hours < 10 ? '0' + hours : hours;
    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;
    
    document.getElementById('time').textContent = `${hours}:${minutes}:${seconds}`;
    
    // Date
    let day = now.getDate();
    let month = now.getMonth() + 1; // January is 0
    let year = now.getFullYear();
    
    day = day < 10 ? '0' + day : day;
    month = month < 10 ? '0' + month : month;
    
    document.getElementById('date').textContent = `${day}/${month}/${year}`;
    
    // Day
    const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    document.getElementById('day').textContent = daysOfWeek[now.getDay()];
  }
  
  // Initial clock update and setInterval to refresh every second
  setInterval(updateClock, 1000);
  updateClock();
  
  // Stopwatch functionality
  let stopwatchInterval;
  let stopwatchTime = 0;
  let isRunning = false;
  
  function formatTime(timeInMilliseconds) {
    const totalSeconds = Math.floor(timeInMilliseconds / 1000);
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;
    const milliseconds = timeInMilliseconds % 1000;
  
    return (
      (hours < 10 ? '0' + hours : hours) + ':' +
      (minutes < 10 ? '0' + minutes : minutes) + ':' +
      (seconds < 10 ? '0' + seconds : seconds) + ':' +
      (milliseconds < 100 ? '0' + (milliseconds < 10 ? '0' + milliseconds : milliseconds) : milliseconds)
    );
  }
  
  function startStopStopwatch() {
    if (isRunning) {
      clearInterval(stopwatchInterval);
      isRunning = false;
      document.getElementById('startStopBtn').textContent = 'Start';
    } else {
      stopwatchInterval = setInterval(() => {
        stopwatchTime += 10; // Update every 10ms for millisecond precision
        document.getElementById('stopwatch').textContent = formatTime(stopwatchTime);
      }, 10);
      isRunning = true;
      document.getElementById('startStopBtn').textContent = 'Stop';
    }
  }
  
  function resetStopwatch() {
    clearInterval(stopwatchInterval);
    isRunning = false;
    stopwatchTime = 0;
    document.getElementById('stopwatch').textContent = '00:00:00:000';
    document.getElementById('startStopBtn').textContent = 'Start';
  }
  
  document.getElementById('startStopBtn').addEventListener('click', startStopStopwatch);
  document.getElementById('resetBtn').addEventListener('click', resetStopwatch);
  