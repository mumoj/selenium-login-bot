"""A python script for automating last.fm log ins using selenium"""

import os
from selenium import webdriver


USERNAME_STR = 'frodiavolo@gmail.com'
PASSWORD_STR = '#$$&Uave9'

project_dir = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(project_dir, 'chromedriver')
browser = webdriver.Chrome(executable_path=driver_path)

browser.get('https://secure.last.fm/login')
username = browser.find_element_by_id('id_username_or_email')
username.send_keys(USERNAME_STR)
password = browser.find_element_by_id('id_password')
password.send_keys(PASSWORD_STR)
submit_button = browser.find_element_by_name('submit')
submit_button.click()
