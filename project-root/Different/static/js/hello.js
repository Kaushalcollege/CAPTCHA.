// Function to get the current timestamp in ISO format
function getCurrentTimestamp() {
    return new Date().toISOString();
}

// Function to get user browser and OS information
function getBrowserAndOSInfo() {
    const userAgent = navigator.userAgent;
    let browser = 'Unknown';
    let os = 'Unknown';

    // Determine the browser name and version
    if (userAgent.indexOf("Firefox") > -1) {
        browser = "Firefox";
    } else if (userAgent.indexOf("Chrome") > -1) {
        browser = "Chrome";
    } else if (userAgent.indexOf("Safari") > -1) {
        browser = "Safari";
    } else if (userAgent.indexOf("Edge") > -1) {
        browser = "Edge";
    } else if (userAgent.indexOf("MSIE") > -1 || !!document.documentMode === true) {
        browser = "IE";
    }

    // Determine the OS name
    if (userAgent.indexOf("Windows NT") > -1) {
        os = "Windows";
    } else if (userAgent.indexOf("Macintosh") > -1) {
        os = "MacOS";
    } else if (userAgent.indexOf("Linux") > -1) {
        os = "Linux";
    } else if (userAgent.indexOf("Android") > -1) {
        os = "Android";
    } else if (userAgent.indexOf("iPhone") > -1 || userAgent.indexOf("iPad") > -1) {
        os = "iOS";
    }

    return {
        browser: browser,
        os: os
    };
}

// Function to simulate measuring round-trip time (RTT)
// Replace this with actual logic to measure RTT if needed
function getRoundTripTime() {
    // Example: Simulating round-trip time as a random value between 50 and 250 ms
    return Math.floor(Math.random() * 200) + 50;
}

// Function to get CSRF token from the hidden input
function getCsrfToken() {
    const csrfTokenElement = document.querySelector('input[name="csrfmiddlewaretoken"]');
    if (csrfTokenElement) {
        return csrfTokenElement.value;
    } else {
        console.error("CSRF token element not found.");
        return null;
    }
}

// Function to get the user's IP address and country using an external API
async function getIpAndLocation() {
    try {
        const response = await fetch('https://ipapi.co/json/');
        if (!response.ok) {
            throw new Error('Failed to fetch IP and location data.');
        }
        const data = await response.json();
        return {
            ip: data.ip,
            country: data.country_name,
            region: data.region,
            city: data.city
        };
    } catch (error) {
        console.error('Error fetching IP and location data:', error);
        return {
            ip: 'Unknown',
            country: 'Unknown',
            region: 'Unknown',
            city: 'Unknown'
        };
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
        const response = await fetch('/predict/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(data)
        });

        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            const result = await response.json();
            console.log('Data sent successfully:', result);
        } else {
            const responseText = await response.text();
            console.error("Unexpected response format:", responseText);
            alert("Unexpected response format. Please contact support.");
        }
    } catch (error) {
        console.error("Error sending data:", error);
    }
}

// Function to collect and send data
async function collectAndSendData() {
    const roundTripTime = getRoundTripTime();
    const { browser, os } = getBrowserAndOSInfo();
    const loginTimestamp = getCurrentTimestamp();
    const loginSuccessful = 'True'; // Example static value, update based on actual login status

    // Fetch IP and location data asynchronously
    const { ip, country, region, city } = await getIpAndLocation();

    const data = {
        'Round-Trip Time [ms]': roundTripTime,
        'IP Address': ip,
        'Country': country,
        'Region': region,
        'City': city,
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
