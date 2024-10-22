from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (here using Chrome)
driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH

try:
    # Navigate to Google
    driver.get("https://www.google.com")

    # Find the search box using its name attribute value
    search_box = driver.find_element(By.NAME, "q")

    # Type the search query and hit Enter
    search_box.send_keys("Selenium WebDriver")
    search_box.send_keys(Keys.RETURN)

    # Wait for a few seconds to see the results
    time.sleep(10)

finally:
    # Close the browser
    driver.quit()
