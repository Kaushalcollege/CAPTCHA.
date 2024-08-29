let lastKeyPressTime = 0;
let keyPressCount = 0;

document.addEventListener('mousemove', function(event) {
    let mouseData = {
        x: event.clientX,
        y: event.clientY,
        timestamp: new Date().toISOString()
    };
    console.log('Mouse Position:', mouseData);
    storeData('mouse_moves', mouseData);
});

document.addEventListener('keydown', function(event) {
    let currentTime = Date.now();
    let typingSpeed = calculateTypingSpeed(currentTime);
    let keyData = {
        key: event.key,
        typingSpeed: typingSpeed,
        timestamp: new Date().toISOString()
    };
    console.log('Key Pressed:', keyData);
    storeData('key_presses', keyData);
});

document.addEventListener('click', function(event) {
    let clickData = {
        x: event.clientX,
        y: event.clientY,
        timestamp: new Date().toISOString()
    };
    console.log('Click Position:', clickData);
    storeData('clicks', clickData);
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
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log('Data stored successfully', result);
    })
    .catch(error => console.error('Error storing data:', error));
}
