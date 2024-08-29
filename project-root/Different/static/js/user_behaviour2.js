let lastKeyPressTime = 0;
let keyPressCount = 0;

document.addEventListener('DOMContentLoaded', function () {
    const loginButton = document.getElementById('login-button');

    if (loginButton) {
        loginButton.addEventListener('click', function (event) {
            event.preventDefault();

            console.log('Login button clicked!');

            fetch('/UserBehavior/log_interaction/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),
                },
                body: JSON.stringify({
                    action: 'login',
                    username: document.getElementById('username').value,
                }),
            }).then(response => {
                if (response.ok) {
                    console.log('Interaction logged successfully!');
                } else {
                    console.error('Failed to log interaction');
                }
            });
        });
    }

    document.addEventListener('mousemove', function (event) {
        let mouseData = {
            x: event.clientX,
            y: event.clientY,
            timestamp: Date.now()
        };
        storeData('mouse_moves', mouseData);
    });

    document.addEventListener('keydown', function (event) {
        let currentTime = Date.now();
        let typingSpeed = calculateTypingSpeed(currentTime);
        let keyData = {
            key: event.key,
            typingSpeed: typingSpeed,
            timestamp: currentTime
        };
        storeData('key_presses', keyData);
    });

    document.addEventListener('click', function (event) {
        let clickData = {
            x: event.clientX,
            y: event.clientY,
            timestamp: Date.now()
        };
        storeData('clicks', clickData);
    });
});

function calculateTypingSpeed(currentTime) {
    if (lastKeyPressTime === 0) {
        lastKeyPressTime = currentTime;
        return 0;
    }

    let timeDifference = (currentTime - lastKeyPressTime) / 1000; // in seconds
    lastKeyPressTime = currentTime;

    if (timeDifference > 0) {
        keyPressCount++;
        return (keyPressCount / timeDifference).toFixed(2);
    }

    return 0;
}

function storeData(endpoint, data) {
    fetch(`http://localhost:8000/api/${endpoint}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(),
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(result => {
        console.log('Data stored successfully', result);
    })
    .catch(error => console.error('Error storing data:', error));
}

function getCSRFToken() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    return csrfToken;
}
