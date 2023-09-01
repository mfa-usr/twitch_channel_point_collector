import sys
import time
import selenium
import threading
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


##
# Position and click action for channel point button
##

def cp_click(x, y):
    actions = ActionChains(driver)
    actions.move_by_offset(10, 15)
    actions.click()
    actions.perform()


while True:

    twitch_url = "https://www.twitch.tv/"

    print("Whose channel would you like to collect points for?")
    requested_channel = input()
    full_url = twitch_url + requested_channel

    # User desired watch-time - must be less than 24 hours
    desired_time = int(input("How long would you like to collect points for this channel? Enter time in hours."))
    start_time = threading.Timer(desired_time, fun)
    start_time.start() # Will need to be fixed later so that program stops once timer has been exceeded

    # 
    print(f"You would like to collect points for {full_url} for {desired_time} hours?")
    print("Enter 'y' to confirm, 'n' to change channel name, and 'e' to exit the program.")
    confirmation = input().lower()

    if not confirmation.isalpha():
        print("Must enter either y, n, or e.")

    if confirmation == 'y':
        if 4 <= len(requested_channel) <= 25:

            options = webdriver.FirefoxOptions()
            # options.add_argument(
            #     "-headless"
            # )

            driver = webdriver.Firefox(options=options)

            driver.get(full_url)

            # Call channel points click function and continuously click
            while True:
                cp_click()
                time.sleep(1)

            # if desired_time == True:
            # driver.quit()

        if len(requested_channel) < 4:
            print("Channel name must be at least 4 characters.")

        if len(requested_channel) > 25:
            print("Channel name must be less than 25 characters.")

    if confirmation =='n':
        continue

    if confirmation == 'e':
        sys.exit()