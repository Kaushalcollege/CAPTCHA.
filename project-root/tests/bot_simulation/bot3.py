from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('http://localhost:8000/')  # Replace with your Django server URL

# Create an ActionChain object
actions = ActionChains(driver)

# Simulate mouse movements and clicks
for i in range(5):
    x_offset = i * 50
    y_offset = i * 50
    actions.move_by_offset(x_offset, y_offset).click().perform()
    time.sleep(0.5)  # Wait for a bit between actions

# Find an element to type into (assume there's an input field in your HTML)
input_field = driver.find_element_by_tag_name('body')  # or use a specific element if needed

# Simulate typing keys
keys_to_type = "This is a bot performing typing and mouse actions!"
for char in keys_to_type:
    input_field.send_keys(char)
    time.sleep(0.1)  # Adjust the speed of typing

# Close the browser after all actions
driver.quit()
