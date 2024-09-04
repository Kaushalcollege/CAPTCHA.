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
    const csrfTokenElement = document.querySelector('input[name="csrfmiddlewaretoken"]');
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
        return Promise.reject("CSRF token is missing");
    }

    try {
        const response = await fetch('/predict/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const errorText = await response.text();
            console.error(`Server responded with status ${response.status}: ${response.statusText}`);
            console.error("Response body:", errorText);
            return Promise.reject(`Server error: ${response.statusText}`);
        }

        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            const result = await response.json();
            console.log('Data sent successfully:', result);
            return Promise.resolve(result);
        } else {
            const errorText = await response.text();
            console.error("Unexpected response format:", errorText);
            return Promise.reject("Unexpected response format");
        }
    } catch (error) {
        console.error("Error sending data:", error);
        return Promise.reject(error);
    }
}



// Function to collect and send data
function collectAndSendData() {
    const form = document.getElementById('login-form');
    const formData = new FormData(form);

    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    return sendData(data);
}


    // Sending the data to the server

    document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    collectAndSendData()
        .then(result => {
            alert('Login successful!');
        })
        .catch(error => {
            alert('There was a problem with the login.');
        });
});

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


