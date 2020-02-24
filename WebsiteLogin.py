#!/usr/bin/python3
#Created By: JMedlock
#Created On: 1/28/60
#Label: FortiAnalyzer SOC Monitor TAMKO 2

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument("--kiosk")
browser = webdriver.Chrome(options=options)
browser.get('https://52.173.17.34')

# Find username field and input username
user = WebDriverWait(browser, 60).until(
    EC.presence_of_element_located((By.ID, 'username'))
)
user.clear()
user.send_keys("TBPAdmin")

# Find password field and input password
passwd = WebDriverWait(browser, 60).until(
    EC.presence_of_element_located((By.ID, 'password'))
)
passwd.clear()
passwd.send_keys("^8sUuYtz7Mmap5J8")
passwd.send_keys(Keys.RETURN)

# Navigate to FortiAnalyzer SOC Monitor TAMKO 2 dashboard
sleep(2)
browser.get("https://52.173.17.34/p/app/#!/adom/soc/noc/275a3c05-9f1e-4b7e-8758-c4711a7db22d")

# Select sorted_descent by xpath
sorted_descent = WebDriverWait(browser, 60).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/fi-noc-dash-widget/div/div[2]/div/div/div/div/div[1]/fi-noc-fortiview-list/div/div/div/div[1]/ng-ftv-table/div/div[1]/div[4]'))
)
sorted_descent.click()

# Put page into fullscreen
sleep(1)
fullscreen_button = WebDriverWait(browser, 60).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/ul[2]/li[5]/button'))
)
fullscreen_button.click()

while True:
    sleep(350)
    browser.refresh()
    sorted_descent = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/fi-noc-dash-widget/div/div[2]/div/div/div/div/div[1]/fi-noc-fortiview-list/div/div/div/div[1]/ng-ftv-table/div/div[1]/div[4]'))
    )
    sorted_descent.click()
    sleep(1)
    fullscreen_button = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/ul[2]/li[5]/button'))
    )
    fullscreen_button.click()

