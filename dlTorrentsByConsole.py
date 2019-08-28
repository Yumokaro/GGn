from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import GGn.consoleList
import time



# Open web browser window
browser = webdriver.Chrome('D:\Downloads\chromedriver')
browser.get('https://gazellegames.net/login.php')
time.sleep(4)

# Login Form
browser.find_element_by_id('username').send_keys('Enter your Username here')

browser.find_element_by_id('password').send_keys('Enter your password here')

browser.find_element_by_id('keeplogged').click()

time.sleep(5)

browser.find_element_by_id('password').send_keys(Keys.ENTER)

time.sleep(30)

##################################################
##################################################
##################################################

# Visit Profile
# browser.get('https://gazellegames.net/user.php?id=')
time.sleep(10)


# Use consoleList array of second file, consoleList.py
# list = consoleList.secondaryConsoleList

# Example - Use a single console
list = [ ['atari 2600', 'https://gazellegames.net/torrents.php?searchstr=&artistname=Atari+2600&order_by=groupname&order_way=asc'] ]
print('Acquired console list')
time.sleep(5)

consoleComplete = []
# Begin scrape
consoleNumber = 0
for x in list:
    # Go to this console in the list and pull the second entry of the first item of the array - link
    browser.get(list[consoleNumber][1])
    print('Downloading torrents for: ', list[consoleNumber][0])
    time.sleep(15)

    t = 0
    e = 0
    while (e < 1):
        try:
            browser.find_elements_by_link_text('DL')[t].click()
            print('Download number:', (t + 1))
            time.sleep(4)
            t += 1

        except IndexError:
            print('No more torrents on this page.')
            print('This page is finished, moving to next page')

            try:
                browser.find_element_by_link_text('Next >').click()
                time.sleep(5)
                t = 0
            except:
                print('This console is finished')
                time.sleep(5)
                #next = 1
                t = 0
                e = 1

    print('<<< Moving on to the next console >>>')
    consoleNumber += 1


# Shut down
browser.close()
browser.quit()

print("Finished")