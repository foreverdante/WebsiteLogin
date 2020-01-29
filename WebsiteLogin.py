#!/usr/bin/python3
#Created By: JMedlock
#Created On: 1/28/20
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument("--kiosk")
browser = webdriver.Chrome(options=options)
browser.get('https://52.173.17.34')
user = browser.find_element_by_id('username')
user.clear()
user.send_keys("TBPAdmin")
passwd = browser.find_element_by_id("password")
passwd.clear()
passwd.send_keys("^8sUuYtz7Mmap5J8")
passwd.send_keys(Keys.RETURN)

sleep(5)
browser.get("https://52.173.17.34/p/app/#!/adom/dvm/groups/-3/")
sleep(5)
button = browser.find_element_by_class_name("btn-primary")
button.click()

# okButton = browser.find_element_by_id("submit-OK")
# okButton.send_keys(Keys.RETURN)


