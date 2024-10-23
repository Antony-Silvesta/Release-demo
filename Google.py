from selenium import webdriver

def test_google_search():
    # Set Chrome options
    options = webdriver.ChromeOptions()
    # You can add any other options if needed, but for using only Chrome, no need for headless or remote

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(options=options)  # This will launch a Chrome browser window

    # Open Google and verify the title
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    
    # Close the browser
    driver.quit()

# Run the test
test_google_search()
