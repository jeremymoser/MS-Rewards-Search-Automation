# Developer: Jeremy Moser
# Created Date: Sunday, November 12th, 2023
# Last Modified Date: Monday, January 1st, 2024

from selenium import webdriver
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from wonderwords import RandomWord
from datetime import datetime
import time

edge_options = Options()
# edge_options.add_experimental_option("detach", True)
edge_options.add_argument("user-data-dir=/Users/jeremymoser/Library/Application Support/Microsoft Edge")
edge_options.add_argument("profile-directory=Default")

edgeBrowser = webdriver.Edge(options=edge_options)

def perform_searches():

    # Initiate variables
    counter = 1
    searches = 5

    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")

    print("")
    print("Current Date/Time: ", dt_string)
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
        search_box = edgeBrowser.find_element(By.ID, "sb_form_q")
        search_box.clear()
        search_box.send_keys(unique_word)
        search_box.send_keys(Keys.RETURN)
        # Print the word to the console
        if(len(str(counter)) == 1):
            displayCounter = "0" + str(counter)
        else:
            displayCounter = str(counter)
        print("#" + displayCounter + ": " + unique_word)
        # Increment counter
        counter += 1
        # Wait 3 seconds before continuing
        time.sleep(5)
    print("=========================")
    print("")

perform_searches()