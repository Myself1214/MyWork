#!/usr/bin/env python
# coding: utf-8

# In[15]:


#import chrome webdriver and BeautifulSoup

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By


#declare login credentials
username = 'your_username'
password='your_password'

#creating an instance of browser to work on
browser = webdriver.Chrome('D:\All from D\chromedriver_win32\chromedriver.exe')

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


# In[ ]:




