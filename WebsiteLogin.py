#!/usr/bin/python3
#Created By: JMedlock
#Created On: 1/28/20
import getpass
import re
import time

from resources.selenium import webdriver
# import resources.selenium.webdriver.common.keys as keys
# # from resources.selenium.webdriver.common import Keys
# from time import sleep

class InvalidInput(Exception):
	pass

class WebsiteLogin(object):
	def __init__(self, website, username, password, options):
		self.website = website
		self.username = username
		self.password = password
		self.options = options


def gather_browser_options():
	# Gather the flags to be applied to Chromium
	option_flags = []
	state = True
	option_number = 1
	print("Please add the options you would like to add to Chromium: ")
	while state is True:
		# Loop through until @param state = False
		if not True:
			break
		else:
			# print("Option {}".format(option_number))
			# Get options to add to the option_flags[] list
			option = input("Option {}: ".format(option_number))
			option_flags.append(''.join(option.lower()))

			# Iterate the number of options added to Chromium

			continue_options = input("Continue [y/N] or [C]orrect previous "
			                         "entry?: ")
			try:
				# Check to make sure correct input was used. If not, raise InvalidInput exception
				if not re.match("[y|n|c]", continue_options.lower()):
					raise InvalidInput
					# If exception is raised, remove
					# option_flags.remove(option)
					# option_flags.remove(option)
					continue
				else:
					if continue_options.lower() == "n":
						for x in option_flags:
							print("Adding the following flags: --{}".format(x))
						state = False
					elif continue_options.lower() == "c":
						option_flags.remove(option)
					else:
						option_number += 1
						continue
			except InvalidInput:
				print("Invalid Input")
				option_flags.remove(option)
	return option_flags

def authentication():
	# Check if there is authentication required and gather authentication
	# information
	auth = {}
	authentication_option = input("Will there be authentication required? y/N: ")
	if authentication_option.lower() == "n":
		pass
	else:
		username = input("Username: ")
		password = getpass.getpass()
		auth.update([('username', username), ('password', password)])
	return auth.values()

def start_browser(website):
	options = gather_browser_options()
	chrome_options = webdriver.ChromeOptions()
	for option in options:
		chrome_options.add_argument(option)
	browser = webdriver.Chrome(options=chrome_options)
	browser.get(website)
		# username = browser.find_element_by_id("id_username")
		# username.send_keys(info[0])
		# password = browser.find_element_by_id("id_password")
		# password.send_keys(info[1])
	for num, name in enumerate(authentication()):
		print("{}".format(name[0]))

def main():
	# website = input("Please enter the full URI that will be used: ")
	# if website.startswith("https"):
	# 	start_browser()
	# if website.startswith("http"):
	start_browser("http://127.0.0.1:8000/accounts/login")
		# print(list(authentication())[1])
	time.sleep(10)
	# else:
	# 	print("It is not working")
	# 	exit(1)


if __name__ == '__main__':
    main()
























# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument("--kiosk")
# browser = webdriver.Chrome(options=options)
# browser.get('https://52.173.17.34')
# user = browser.find_element_by_id('username')
# user.clear()
# user.send_keys("TBPAdmin")
# passwd = browser.find_element_by_id("password")
# passwd.clear()
# passwd.send_keys("^8sUuYtz7Mmap5J8")
# passwd.send_keys(keys.Keys.RETURN)
#
# sleep(5)
# browser.get("https://52.173.17.34/p/app/#!/adom/soc/noc/fff797a8-d4c6-4667-a61b-ea545a2bd834")
# sleep(6)
# fullscreen_button = browser.find_element_by_class_name("fullscreen-btn")
# fullscreen_button.click()
# sleep(3)
#
# while True:
# 	sleep(60)
# 	browser.refresh()
# 	sleep(7)
# 	fullscreen_button = browser.find_element_by_class_name("fullscreen-btn")
# 	fullscreen_button.click()