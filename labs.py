from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize WebDriver (Chrome)
driver = webdriver.Chrome()

# Open YouTube
driver.get("https://www.youtube.com")

# Find the search bar using its name attribute
search_bar = driver.find_element(By.NAME, "search_query")

# Enter a search query (e.g., "Selenium tutorial")
search_bar.send_keys("Selenium tutorial")

# Simulate pressing 'Enter'
search_bar.send_keys(Keys.RETURN)

# Wait for a few seconds to load the results (optional)
driver.implicitly_wait(5)

# Close the browser
driver.quit()
