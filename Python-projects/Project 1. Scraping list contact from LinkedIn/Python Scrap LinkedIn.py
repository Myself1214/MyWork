#!/usr/bin/env python
# coding: utf-8

#import chrome webdriver and BeautifulSoup

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#declare login credentials
username = 'your_username'
password='your_password'


#creating an instance of browser to work on
browser = webdriver.Chrome('<path_to_chromedriver>\chromedriver.exe')

#opening linkedIn main page to log in in browser instance opened previousely
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

#Find element (username filed) by id 
user_filed = browser.find_element(By.ID, 'username')
#Enter username
user_filed.send_keys(username)

#Find element (password field) by id
pass_field= browser.find_element(By.ID, 'password')
#Enter password
pass_field.send_keys(password)

#submit log in credentials
pass_field.submit()
time.sleep(3)

#Find search box
search_box = browser.find_element(By.CLASS_NAME, 'search-global-typeahead__input')
#Send input
search_box.send_keys('john doe')
search_box.send_keys(Keys.ENTER)
time.sleep(3)