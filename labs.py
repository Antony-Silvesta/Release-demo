from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class WebTest:
    def __init__(self):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options)
        print("Browser initialized.")
    
    def open_page(self, url):
        self.driver.get(url)
        sleep(3)
        print(f"Opened page: {url}")
    
    def test_title(self, expected_title):
        title = self.driver.title
        assert expected_title in title, f"Expected title '{expected_title}' not found in '{title}'"
        print("TEST 0: `title` test passed")

    def login(self, username_id, password_id, username, password, submit_button_class):
        self.driver.find_element(By.ID, username_id).send_keys(username)
        self.driver.find_element(By.ID, password_id).send_keys(password)
        self.driver.find_element(By.CLASS_NAME, submit_button_class).click()
        sleep(2)
        print(f"Attempted login with username: {username}")
    
    def verify_element_by_text(self, by_type, identifier, expected_text):
        # Use explicit wait to wait for the element to appear on the page
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((by_type, identifier))
            )
            assert expected_text in element.text, f"Expected text '{expected_text}' not found."
            print(f"TEST: Element with identifier '{identifier}' contains the expected text.")
        except Exception as e:
            print(f"Error finding element by {by_type} '{identifier}': {e}")
    
    def take_screenshot(self, file_name="screenshot.png"):
        self.driver.save_screenshot(file_name)
        print(f"Screenshot saved as {file_name}")
    
    def check_element_present(self, by_type, identifier):
        try:
            element = self.driver.find_element(by_type, identifier)
            print(f"Element found: {identifier}")
            return element
        except:
            print(f"Element not found: {identifier}")
            return None
    
    def close(self):
        self.driver.quit()
        print("Browser closed.")

# Usage of the WebTest class
if __name__ == "__main__":
    test = WebTest()
    print("Testing started")
    
    test.open_page("https://www.saucedemo.com/")
    test.test_title("Swag Labs")
    
    # Attempt to login
    test.login("user-name", "password", "standard_user", "secret_sauce", "btn_action")
    
    # Use explicit wait to verify that the error message is present
    test.verify_element_by_text(By.TAG_NAME, "h3", "Epic sadface")  # Adjust according to the actual page
    
    # Take a screenshot after attempting to log in
    test.take_screenshot("login_test_screenshot.png")

    # Check if a specific element is present (e.g., a logout button or error message)
    test.check_element_present(By.CLASS_NAME, "error-message-container")

    # Close the browser
    test.close()
