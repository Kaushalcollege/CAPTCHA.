from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import time

def simulate_bot():
    options = Options()
    options.add_argument('--headless')  # Run in headless mode if desired

    # Ensure you have the correct path to your chromedriver
    service = Service('/path/to/chromedriver')  # Update with your chromedriver path
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("http://127.0.0.1:8000/")
        # Wait for the page to load completely
        time.sleep(3)

        # Fill out the login form
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        username.send_keys("testuser")
        password.send_keys("testpassword")
        login_button.click()

        # Wait for login action to complete
        time.sleep(3)

        # Print the page source after login attempt
        print(driver.page_source)

    except WebDriverException as e:
        print(f"WebDriverException: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    simulate_bot()
