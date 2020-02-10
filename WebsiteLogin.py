#!/usr/bin/python3
#Created By: JMedlock
#Created On: 1/28/20
import getpass
import re
import time

from resources.selenium import webdriver
from resources.selenium.webdriver.support.ui import WebDriverWait
from resources.selenium.webdriver.common.by import By
from resources.selenium.webdriver.support import expected_conditions as EC

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
	flags_question_bool = True
	option_number = 1
	flags_question = input("Are there flags you would like to attach with "
	                   "Chromium? y/N: ")
	if not re.match("[y|n]", flags_question.lower()):
		pass
	elif flags_question.lower() == 'y':
		print("Please add the options you would like to add to Chromium: ")
		while state is True:
			# Loop through until @param state = False
			if not True:
				break
			else:
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
	else:
		return None

def authentication():
	"""Checks if there is authentication required and if so to save
	username/password to list and return the list."""
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
	"""Start the browser with gathered information"""
	options = gather_browser_options()
	chrome_options = webdriver.ChromeOptions()

	if options is None:
		pass
	else:
		# Add option flags to Chromium
		for option in options:
			chrome_options.add_argument(option)

	# Create list for authentication parameters and add credentials to list
	credentials = []
	credentials.append(list(authentication()))

	# Apply flags to browser call
	browser = webdriver.Chrome(options=chrome_options)
	browser.get(website)

	# # Find username field and insert username index in @credentials
	# username = browser.find_element_by_id("id_username")
	# username.send_keys(credentials[0][0])
	#
	# # Find password field and insert password index in @credentials
	# password = browser.find_element_by_id("id_password")
	# password.send_keys(credentials[0][1])

	username = WebDriverWait(browser, 10).until(
		EC.presence_of_element_located((By.ID, 'id_username'))
	)
	password = WebDriverWait(browser, 10).until(
		EC.presence_of_element_located((By.ID, 'id_password'))
	)
	username.send_keys(credentials[0][0])
	password.send_keys(credentials[0][1])

	# Find submit_button field and 'click' the button
	# submit_button = browser.find_element_by_tag_name("button")
	# submit_button.click()
	submit_button = WebDriverWait(browser, 10).until(
		EC.element_to_be_clickable((By.XPATH, '/html/body/main/form/button'))
	)
	submit_button.click()

def main():
	website = input("Please enter the full URI that will be used: ")
	# if website.startswith("https"):
	# 	start_browser()

	##### TESTING ONLY #####
	if website.startswith("http"):
		start_browser(website)
		time.sleep(10)
	##### END TESTING #####
	else:
		print("It is not working")
		exit(1)


if __name__ == '__main__':
    main()
