import random
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open URL and maximize window
driver.get('http://tutorialsninja.com/demo/')
driver.maximize_window()

# Adding error handling in case elements are not found
try:
    # Click on Phones & PDAs category
    phones = driver.find_element(By.XPATH, '//a[text()="Phones & PDAs"]')
    phones.click()
    print("Navigated to Phones & PDAs category.")
    
    # Select iPhone from the list
    iphone = driver.find_element(By.XPATH, '//a[text()="iPhone"]')
    iphone.click()
    print("iPhone page opened.")

    time.sleep(1)

    # Scroll down to make sure the image is visible
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(1)

    # Click on the first picture
    first_pic = driver.find_element(By.XPATH, '//ul[@class="thumbnails"]/li[1]')
    first_pic.click()
    print("First image clicked.")

    time.sleep(2)

    # Click through the next pictures
    next_click = driver.find_element(By.XPATH, '//button[@title="Next (Right arrow key)"]')
    for i in range(5):
        next_click.click()
        time.sleep(2)
    print("Navigated through all pictures.")

    # Save a screenshot of the iPhone page after viewing images
    screenshot_filename = f'screenshot#{random.randint(0, 101)}.png'
    driver.save_screenshot(screenshot_filename)
    print(f"Screenshot saved as {screenshot_filename}.")

    # Close the image view
    x_button = driver.find_element(By.XPATH, '//button[@title="Close (Esc)"]')
    x_button.click()
    time.sleep(1)

    # Scroll down to the "Quantity" input field
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(1)

    # Adjust quantity to '2'
    quantity = driver.find_element(By.ID, 'input-quantity')
    quantity.clear()
    quantity.send_keys('2')
    time.sleep(1)

    # Add the iPhone to cart
    add_to_button = driver.find_element(By.ID, 'button-cart')
    add_to_button.click()
    print("Item added to cart.")

    time.sleep(3)

    # Scroll to the top of the page to view the cart
    driver.execute_script("window.scrollBy(0, -1000);")
    time.sleep(2)

    # Click on the cart button to view items in the cart
    cart_button = driver.find_element(By.XPATH, '//a[@title="Shopping Cart"]')
    cart_button.click()
    print("Navigated to shopping cart.")

    time.sleep(2)

    # Extract item details from the cart
    cart_item = driver.find_element(By.XPATH, '//div[@id="content"]/form/div/table/tbody/tr/td[2]/a')
    cart_price = driver.find_element(By.XPATH, '//div[@id="content"]/form/div/table/tbody/tr/td[6]')

    print(f"Item in Cart: {cart_item.text}")
    print(f"Item Price: {cart_price.text}")

    # Proceed to Checkout (optional)
    # Uncomment the following lines if you want to proceed to checkout
    # checkout_button = driver.find_element(By.XPATH, '//a[contains(text(), "Checkout")]')
    # checkout_button.click()
    # print("Proceeding to checkout...")

except NoSuchElementException as e:
    print(f"An error occurred: {e}")

finally:
    # Wait and close the browser
    time.sleep(5)
    driver.quit()
    print("Browser closed.")
