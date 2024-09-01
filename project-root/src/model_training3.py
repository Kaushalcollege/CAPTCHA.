import os
import django
import requests
import sys
import time  # Keep time if used for timestamping

# Update the path to include your Django project
sys.path.append('/Users/kaushalkento/Desktop/GroupProject./CAPTCHARefinement./project-root/Different')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Different.settings')
django.setup()

print("Django setup successful!")

# Simulating the user interaction data storage
last_keypress_time = 0
keypress_count = 0

def simulate_mouse_move(x, y):
    timestamp = int(time.time() * 1000)  # Convert to milliseconds
    mouse_data = {
        'x': x,
        'y': y,
        'timestamp': timestamp
    }
    print('Mouse Position:', mouse_data)
    store_data('mouse_moves', mouse_data)

def simulate_key_press(key):
    global last_keypress_time, keypress_count
    current_time = int(time.time() * 1000)  # Convert to milliseconds
    typing_speed = calculate_typing_speed(current_time)
    key_data = {
        'key': key,
        'typing_speed': typing_speed,
        'timestamp': current_time
    }
    print('Key Pressed:', key_data)
    store_data('key_presses', key_data)

def simulate_click(x, y):
    timestamp = int(time.time() * 1000)  # Convert to milliseconds
    click_data = {
        'x': x,
        'y': y,
        'timestamp': timestamp
    }
    print('Click Position:', click_data)
    store_data('clicks', click_data)

def calculate_typing_speed(current_time):
    global last_keypress_time, keypress_count
    if last_keypress_time == 0:
        last_keypress_time = current_time
        return 0

    time_difference = (current_time - last_keypress_time) / 1000  # Convert to seconds
    last_keypress_time = current_time

    if time_difference > 0:
        keypress_count += 1
        return round(keypress_count / time_difference, 2)

    return 0

def store_data(endpoint, data):
    url = f"http://localhost:8000/api/{endpoint}/"
    try:
        response = requests.post(url, json=data, headers={'Content-Type': 'application/json'})
        response.raise_for_status()
        print('Data stored successfully:', response.json())
    except requests.exceptions.RequestException as e:
        print(f'Error storing data: {e}')

# Example usage
# Uncomment these lines to test the functions
# simulate_mouse_move(100, 200)
# simulate_key_press('a')
# simulate_click(300, 400)
