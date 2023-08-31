import sys
import selenium
from selenium import webdriver
import numpy
import time

while True:

    twitch_url = "https://www.twitch.tv/"


    print("Whose channel would you like to collect points for?")
    requested_channel = input()

    print("How long would you like to collect points for this channel?")
    full_url = twitch_url + requested_channel

    print(f"You would like to collect points for {full_url}?")
    print("Enter 'y' to confirm, 'n' to change channel name, and 'e' to exit the program.")
    confirmation = input().lower()

    if not confirmation.islapha():
        print("Must enter either y, n, or e.")
    
    # desired_time = 

    if confirmation == 'y':
        if 4 <= len(requested_channel) <= 25:

            options = webdriver.FirefoxOptions()
            # options.add_argument(
            #     "-headless"
            # )

            driver = webdriver.Firefox(options=options)

            driver.get(full_url)

            # if desired_time == True:
            # driver.quit()

        if len(requested_channel) < 4:
            print("Channel name must be at least 4 characters.")

        if len(requested_channel) > 25:
            print("Channel name must be less than 25 characters.")

    if confirmation =='e':
        continue

    if confirmation == 'n':
        sys.exit()