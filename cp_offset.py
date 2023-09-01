# Used to find the offset of channel points button
# Why was this necessary?
# The channel points button html identifiers may change at some point but more than likely the positioning won't
# By getting this offset we will always know the button coordinates and can use that information if identifiers change

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def login(driver):

    username = input("Enter username: ")
    password = input("Enter password: ")

    enter_login = driver.find_element(By.XPATH, '//button[@data-test-selector="anon-user-menu__login-button"]')
    enter_login.click()
    
    # Wait until login page is loaded from the DOM
    wait = WebDriverWait(driver, timeout=10)
    login_container = (wait.until(ec.visibility_of_element_located((
        By.XPATH, '//button[@class="Layout-sc-1xcs6mc-0 gyuRLA auth-modal"]'))))
    login_wait = WebDriverWait(driver, timeout=10).until(lambda w: login_container.is_displayed())

    # Login
    input_username = driver.find_element(By.ID, "login-username").send_keys(f"{username}")
    input_password = driver.find_element(By.ID, "password-input").send_keys(f"{password}")
    login_user = driver.find_element(
        By.XPATH, '//button[@class="ScCoreButton-sc-ocjdkq-0 ScCoreButtonPrimary-sc-ocjdkq-1 TZYgI ktiwJH"]').click()


twitch_url = "https://www.twitch.tv/"
requested_channel = input("Input channel: ")
full_url = twitch_url + requested_channel

options = webdriver.FirefoxOptions()

# Firefox executable needs to be explicility set or it will throw..
# Chrome driver errors if Chrome is installed on User's system
current_directory = os.getcwd()
firefox_binary_path = os.path.join(current_directory, 'geckodriver.exe')
options.binary_location = firefox_binary_path

driver = webdriver.Firefox(options=options)

driver.get(full_url)

login(driver)

button_element = driver.find_elements(By.XPATH, '//button[@aria-label="Claim Bonus"]')

if button_element:
    for button_element in button_element:
        if button_element.is_displayed():
            location = button_element.location
            x_offset = location['x']
            y_offset = location['y']
            print(f"Claim Bonus button found at ({x_offset}, {y_offset})")
else:
    print('No "Claim Bonus" button found on the webpage.')
