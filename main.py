import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC4
from selenium.webdriver.support.select import Select
import time

import random
import time


def main():

    browser = webdriver.Chrome()
    accounts = []
    accounts.append(['username', 'password'])
    with open("dataset.csv", "r") as readFile:
        read = csv.reader(readFile, delimiter=":")
        count = 0
        for row in read:
            browser.get("https://www.spotify.com/in/signup/")
            id = browser.find_element_by_id("email")
            id.send_keys(row[0])
            print(row[0])
            id_c = browser.find_element_by_id("confirm")
            id_c.send_keys(row[0])
            print(row[0])
            pwd = browser.find_element_by_id("password")
            pwd.send_keys(row[1])
            dispname = browser.find_element_by_id("displayname")
            dispname.send_keys(row[2])
            year = browser.find_element_by_id("year")
            year.send_keys("1995")
            month = browser.find_element_by_id("month")
            drp = Select(month)
            drp.select_by_index(1)
            day = browser.find_element_by_id("day")
            day.send_keys("19")
            sex = browser.find_element_by_xpath(
                "/html/body/div[1]/main/div[2]/form/div[6]/div[2]/label[1]/span[1]")
            sex.click()

            time.sleep(15)
            sign_up = browser.find_element_by_xpath(
                "/html/body/div[1]/main/div[2]/form/div[9]/div/button")
            sign_up.click()
            if browser.current_url == "https://www.netflix.com/browse":
                accounts.append([row[0], row[1]])
                # logout after saving
                browser.get("https://www.netflix.com/SignOut?lnkctr=mL")
            # counting number of attempts
            count = count + 1
            # after every 3 attempts
            if count % 3 == 0:
                # generate a random number for delay
                r = random.randrange(10, 300)
                # delaying web page request after every 3 login attempts by the random no. of seconds
                time.sleep(r)
                # closing the current web page
                browser.get("https://google.com/")

    readFile.close()
    # opening a file to store working accounts
    with open("accounts.csv", "w") as writeFile:
        write = csv.writer(writeFile, delimiter=",")
        # storing all working accounts in csv file
        for account in accounts:
            write.writerow(account)


if __name__ == '__main__':
    main()
