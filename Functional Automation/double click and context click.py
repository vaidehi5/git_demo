


from selenium import webdriver
import time

from selenium.webdriver import ActionChains

driver = webdriver.Chrome("D:\Python_Selenium_Concepts\drivers\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
act = ActionChains(driver)
act.context_click(driver.find_element_by_xpath("//input[@id='double-click']")).perform()  # this will right click
act.double_click(driver.find_element_by_xpath("//input[@id='double-click']")).perform()
ale = driver.switch_to.alert
print(ale.text)
ale.accept()