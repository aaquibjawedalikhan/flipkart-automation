# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 01:16:35 2020

@author: shruti
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 19:09:14 2020

@author: shruti
"""



from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logindata1

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('C:\chromedriver.exe')
action = ActionChains(driver)
time.sleep(1)

driver.get('http://www.flipkart.com')
time.sleep(3)

sign = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input')
sign.send_keys(logindata1.USERNAME)
time.sleep(3)

passwordelement = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input')
passwordelement.send_keys(logindata1.PASSWORD)
time.sleep(3)

login = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button')
login.click()
time.sleep(3)

search = driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
search.send_keys('sunglasses')
search.send_keys(Keys.ENTER)
time.sleep(3)

element = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[4]')
element.click()
time.sleep(3)

driver.switch_to_window(driver.window_handles[1])

cart = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button')
cart.click()
time.sleep(3)

place = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div/div[1]/div/div[3]/div/form/button')
place.click()
time.sleep(3)

proceed = driver.find_element_by_xpath('//*[@id="to-payment"]/button')
proceed.click()
time.sleep(3)
# pay button ko ab click karenge
pay = driver.find_element_by_xpath(
    '//*[@id="container"]/div/div[2]/div/div[1]/div[4]/div/div/div[1]/div/label[4]/div[2]/div/div/ul/li')
pay.click()
time.sleep(3)
