from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('http://localhost:8000/')  # Replace with your Django server URL

# Create an ActionChain object
actions = ActionChains(driver)

# Simulate mouse movements and clicks
for i in range(10):
    x_offset = i * 20
    y_offset = i * 20
    actions.move_by_offset(x_offset, y_offset).click().perform()
    time.sleep(0.5)  # Wait for a bit between actions

# Close the browser after actions
driver.quit()
