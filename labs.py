from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the login page
driver.get("http://the-internet.herokuapp.com/login")

# Maximize the browser window
driver.maximize_window()

# Find the username input field and enter username
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

# Find the password input field and enter password
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

# Click the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Wait for the next page to load
time.sleep(3)

# Check for the success message after login
success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
if "You logged into a secure area!" in success_message.text:
    print("Login successful!")
else:
    print("Login failed.")

# Close the browser
driver.quit()
