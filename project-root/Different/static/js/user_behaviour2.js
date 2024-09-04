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

// Function to get CSRF token from the hidden input
// Function to get CSRF token
function getCsrfToken() {
    // Find the CSRF token element by its ID or name
    const csrfTokenElement = document.querySelector('input[name="csrfmiddlewaretoken"]');

    // Check if the element exists before accessing its value
    if (csrfTokenElement) {
        return csrfTokenElement.value;
    } else {
        console.error("CSRF token element not found.");
        return null;
    }
}

// Function to send data to the server
async function sendData(data) {
    const csrfToken = getCsrfToken();
    if (!csrfToken) {
        console.error("Cannot send data: CSRF token is missing.");
        return;
    }

    try {
        const response = await fetch('/your-api-endpoint/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(data)
        });

        // Check if the response is JSON
        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            // Parse and handle the JSON response
            const result = await response.json();
            console.log('Data sent successfully:', result);
        } else {
            // Handle unexpected response types
            const responseText = await response.text(); // Get the raw response
            console.error("Unexpected response format:", responseText);
            alert("Unexpected response format. Please contact support.");
        }
    } catch (error) {
        console.error("Error sending data:", error);
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

    sendData(data)
    .then(result => {
        // Handle successful data send
        console.log('Data was successfully sent and received:', result);
    })
    .catch(error => {
        // Handle errors
        console.error('There was a problem sending the data:', error);
    });
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

function getCSRFToken() {
    let csrfToken = null;
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith('csrftoken=')) {
            csrfToken = cookie.substring('csrftoken='.length, cookie.length);
            break;
        }
    }
    return csrfToken;
}

const csrfToken = getCSRFToken();

fetch('/predict/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
    },
    body: JSON.stringify({ /* your data here */ }),
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));


