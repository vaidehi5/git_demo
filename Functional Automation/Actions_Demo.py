import self as self
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("D:\Python_Selenium_Concepts\drivers\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()
act = ActionChains(driver)
# wait = WebDriverWait(driver, 5)
# #wb = wait.until(expected_conditions.presence_of_all_element_located((By.ID, "search")))
# wb = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Account & Lists")))
# #wb = self.driver.find_element_by_id("search")
act.move_to_element(driver.find_element_by_xpath("//a[@id='nav-link-accountList']")).perform()
act.move_to_element(driver.find_element_by_link_text("Create a Wish List")).click().perform()

driver.close()