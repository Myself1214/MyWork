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

#declaring list of emails variable
emails_list = []

#reading candidates list provided
candidate_list = [line.strip("\n") for line in list(open('path_to_file_with_list_of_candidate_names/filename.txt', 'r'))]

#for each candidate from provided list, do the following:
for candidate in candidate_list:
    #Find search box
    search_box = browser.find_element(By.CLASS_NAME, 'search-global-typeahead__input')
    search_box.clear()

    #Send input
    search_box.send_keys(candidate)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    #clickign on candidate's name to open their main page

    link = browser.find_element(By.PARTIAL_LINK_TEXT, candidate)
    link.send_keys(Keys.ENTER)
    time.sleep(2)
    
    #refreshing page to insure 'info' element is identifyable
    browser.refresh()

    #clicking on 'Contact info' link/button
    contact_info = browser.find_element(By.ID, 'top-card-text-details-contact-info')
    contact_info.send_keys(Keys.ENTER)

    #parsing through contat info html code
    contact_details = browser.page_source
    soup = bs(contact_details, 'html.parser')

    # Define the email pattern using regex
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    #searching for email if exists and extracting it
    for data in soup.find_all("a"):
        filtered_data = data.get_text()
        # Search for the email pattern in the text
        match = re.search(email_pattern, filtered_data)
        #if email is found
        if match:
            email = filtered_data.strip(' ').strip('\n').strip(',').strip(' ')
            emails_list.append(candidate+"'s email is: "+email)
            break
        #if emails is not found
        else:
            email = 'No email found for this candidate'
            emails_list.append(candidate+"'s email is: "+email)

#removing duplicate values
emails_list = list(set(emails_list))

#removing incorrect findings
for item in emails_list:
    count = 0
    text = (item.split()[0]+' '+item.split()[1])
    for i in emails_list:
        if text in i:
            count+=1
    if count > 1:
        if item == text+' email is: No email found for this candidate':
            emails_list.remove(item)
    
emails_list