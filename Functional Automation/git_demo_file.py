# import self as self
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("D:\Python_Selenium_Concepts\drivers\chromedriver.exe")
driver.get("https://www.amazon.in/")
print("e commerce ")
print(" automate process")
print("after creating branch 1 , content added")
driver.close()