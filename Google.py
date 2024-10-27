from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options if needed
chrome_options = Options()


# Set up the Chrome WebDriver using ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Navigate to Google
    driver.get("https://www.google.com")

    # Find the search box
    search_box = driver.find_element("name", "q")  # Updated to new Selenium syntax
    search_box.send_keys("Selenium WebDriver")
    search_box.submit()

    # Wait for a moment and print the page title
    driver.implicitly_wait(5)
    print(driver.title)

finally:
    driver.quit()  # Make sure to close the browser



