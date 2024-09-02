// Function to get the current timestamp in ISO format
function getCurrentTimestamp() {
    return new Date().toISOString();
}

// Function to get user browser and OS information
function getBrowserAndOSInfo() {
    const userAgent = navigator.userAgent;
    const browserInfo = userAgent.match(/(Firefox|MSIE|Trident|Edge|Chrome|Safari|Opera)/i);
    const osInfo = userAgent.match(/(Windows NT|Macintosh|Linux|Android|iPhone|iPad)/i);
    return {
        browser: browserInfo ? browserInfo[0] : 'Unknown',
        os: osInfo ? osInfo[0] : 'Unknown'
    };
}

// Function to simulate measuring round-trip time (RTT)
// Replace this with actual logic to measure RTT if needed
function getRoundTripTime() {
    // Example: Simulating round-trip time as a random value between 50 and 250 ms
    return Math.floor(Math.random() * 200) + 50;
}

// Function to send the collected data to the server
async function sendData(data) {
    try {
        const response = await fetch('/predict/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams(data) // Convert the data to URL-encoded format
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();
        console.log('Prediction:', result.prediction);
    } catch (error) {
        console.error('Error:', error);
    }
}

// Function to collect and send data
function collectAndSendData() {
    // Collecting the necessary data
    const roundTripTime = getRoundTripTime();
    const country = 'USA'; // Example static value, use IP geolocation API for dynamic value
    const { browser, os } = getBrowserAndOSInfo();
    const loginTimestamp = getCurrentTimestamp();
    const loginSuccessful = 'True'; // Example static value, update based on actual login status

    // Constructing the data object to send
    const data = {
        'Round-Trip Time [ms]': roundTripTime,
        'Country': country,
        'Browser Name and Version': browser,
        'OS Name and Version': os,
        'Login Timestamp': loginTimestamp,
        'Login Successful': loginSuccessful
    };

    // Sending the data to the server
    sendData(data);
}

// Function to handle form submission
function handleFormSubmit(event) {
    event.preventDefault(); // Prevent form submission
    collectAndSendData(); // Collect and send data on form submission
}

// Setting up periodic data collection and sending (e.g., every 10 seconds)
setInterval(collectAndSendData, 10000);

// Optionally, collect and send data when the form is submitted
const formElement = document.querySelector('form');
if (formElement) {
    formElement.addEventListener('submit', handleFormSubmit);
}
