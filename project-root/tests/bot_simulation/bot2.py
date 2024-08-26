from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('http://localhost:8000/')  # Replace with your Django server URL

# Find an element to type into (assume there's an input field in your HTML)
input_field = driver.find_element_by_tag_name('body')  # or use the specific element if there's one

# Simulate typing keys
keys_to_type = "kaushalkento"
for char in keys_to_type:
    input_field.send_keys(char)
    time.sleep(0.1)  # Adjust the speed of typing

# Close the browser after typing
driver.quit()
