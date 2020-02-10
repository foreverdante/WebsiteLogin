#!/usr/bin/python3
#Created By: JMedlock
#Created On: 2/9/20
from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000/accounts/login')
try:
    username = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'id_username'))
    )
    password = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'id_password'))
    )
    username.send_keys('rhysand')
    password.send_keys('fain988foam981')
    button = browser.find_element_by_xpath('/html/body/main/form/button')
    button.click()
    logout = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/main/p[1]/a'))
    )
    logout.click()
    sleep(5)
    browser.close()
except TimeoutError:
    browser.close()