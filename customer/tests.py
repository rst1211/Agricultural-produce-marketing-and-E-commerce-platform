from django.test import TestCase
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import HTMLTestRunner
# Create your tests here.
driver=webdriver.Chrome('C:\\Users\\Dell\\Downloads\\chromedriver_win32\\chromedriver')
driver.get('...')
driver.maximize_window()
print("Opened website")
time.sleep(2)

#click on customer account
#customer=driver.find_element_by_xpath('//input[@value="customer"]')
#customer.click()

fruits=driver.find_element_by_xpath('//a[text()="FRUITS"]')
fruits.click()

quantity=driver.find_element_by_id('quantity')
time.sleep(1)
quantity.send_keys('2')
time.sleep(1)


add_to_button=driver.find_element_by_xpath("//option[@value='Update']") 
add_to_button.click()
time.sleep(2)