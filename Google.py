from selenium import webdriver

def test_google_search():
    # Set Chrome options
    options = webdriver.ChromeOptions()

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(options=options)  

    # Open Google and verify the title
    driver.get("https://www.google.com")
    assert "Google" in driver.title, "Google search page did not load properly"
    
    # Close the browser
    driver.quit()


