# Automated Login Tester


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Start the browser.
browser = webdriver.Chrome()

try:
    # Open a demo login page.
    browser.get("https://the-internet.herokuapp.com/login")

    # Find username and password fields.
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")

    # Enter test credentials.
    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")

    # Click login button.
    login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Wait for page to load.
    time.sleep(2)

    try:
        success_message = browser.find_element(By.ID, "flash")

        if "You logged into a secure area!" in success_message.text:
            print("Login Successful!")
        else:
            print("Login Failed!")

    except NoSuchElementException:
        print("Could not verify login results.")

finally:
    # Keep browser open for 5 seconds.
    time.sleep(5)
    browser.quit()