from selenium import webdriver
import time


driver = webdriver.Chrome("D:\Python_Selenium_Concepts\drivers\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
parentwindow = driver.window_handles[0]
childwindow= driver.window_handles[1]

driver.switch_to.window(childwindow)
print(driver.find_element_by_tag_name("h3").text)
driver.close()
driver.switch_to.window(parentwindow)
print(driver.find_element_by_tag_name("h3").text)
assert "Opening a new window" == driver.find_element_by_tag_name("h3").text
driver.close()
