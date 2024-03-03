# Developer: Jeremy Moser
# Created Date: Sunday, November 12th, 2023
# Last Modified Date: Sunday, March 3rd, 2024

from selenium import webdriver
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from wonderwords import RandomWord
from datetime import datetime
import time

edge_options = Options()
edge_options.add_argument(
    "user-data-dir=/Users/jeremymoser/Library/Application Support/Microsoft Edge"
)
edge_options.add_argument("profile-directory=Default")

edgeBrowser = webdriver.Edge(options=edge_options)


def perform_searches():

    # Initiate variables
    counter = 1
    searches = 35

    now = datetime.now()
    dt_string = now.strftime("%A, %B %d, %Y %-I:%M %p")

    print("")
    print("Current date & time:", dt_string)
    print("Searches include:")
    print("=========================")

    # While loop to interate from counter to searches value
    while counter <= searches:
        # Generate a rand word utilizing RandomWord
        rw = RandomWord()
        unique_word = rw.word()
        # Set URL to bing.com, set search, and press Return
        edgeBrowser.get("https://www.bing.com")
        time.sleep(5)

        # During first search, capture the Microsoft Rewards starting balance
        if counter == 1:
            current_points = edgeBrowser.find_element(By.ID, "id_rc")
            starting_balance = current_points.text
        search_box = edgeBrowser.find_element(By.ID, "sb_form_q")
        search_box.clear()
        search_box.send_keys(unique_word)
        search_box.send_keys(Keys.RETURN)
        # Print the word to the console
        if len(str(counter)) == 1:
            displayCounter = "0" + str(counter)
        else:
            displayCounter = str(counter)
        print("#" + displayCounter + ": " + unique_word)
        # Increment counter
        counter += 1
        # Wait 3 seconds before continuing
        time.sleep(3)
        # During last search, capture the Microsoft Rewards ending balance & calculate points earned
        if counter == searches:
            current_points = edgeBrowser.find_element(By.ID, "id_rc")
            ending_balance = current_points.text
            points_earned = int(ending_balance) - int(starting_balance)
    print("=========================")
    print("Points earned:", str(points_earned))
    print("")

    with open(
        "/Users/jeremymoser/Documents/Python/MS Rewards Search Automation/log.txt", "a"
    ) as file:
        file.write(dt_string + " | Points earned: " + str(points_earned) + "\n")
    print("Log file updated.")
    print("")


perform_searches()
