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
    if (userAgent.includes("Firefox")) {
        browser = "Firefox";
    } else if (userAgent.includes("Chrome")) {
        browser = "Chrome";
    } else if (userAgent.includes("Safari")) {
        browser = "Safari";
    } else if (userAgent.includes("Edge")) {
        browser = "Edge";
    } else if (userAgent.includes("MSIE") || !!document.documentMode) {
        browser = "MSIE";
    }

    // Determine the OS name
    if (userAgent.includes("Windows NT")) {
        os = "Windows";
    } else if (userAgent.includes("Macintosh")) {
        os = "MacOS";
    } else if (userAgent.includes("Linux")) {
        os = "Linux";
    } else if (userAgent.includes("Android")) {
        os = "Android";
    } else if (userAgent.includes("iPhone") || userAgent.includes("iPad")) {
        os = "iOS";
    }

    return { browser, os };
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
    return csrfTokenElement ? csrfTokenElement.value : null;
}

// Function to get the user's IP address and location using an external API
async function getIpAndLocation() {
    try {
        const response = await fetch('https://ipapi.co/json/');
        if (!response.ok) throw new Error('Failed to fetch IP and location data.');

        const data = await response.json();
        return {
            ip: data.ip || 'Unknown',
            country: data.country_name || 'Unknown',
            region: data.region || 'Unknown',
            city: data.city || 'Unknown'
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

// Set up periodic data collection and sending (e.g., every 10 seconds)
setInterval(collectAndSendData, 10000);

// Optionally, collect and send data when the form is submitted

