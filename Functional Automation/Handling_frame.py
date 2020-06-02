from selenium import webdriver
import time

# ifrme, frameset, frame
driver = webdriver.Chrome("D:\Python_Selenium_Concepts\drivers\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am able to automate")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)
driver.close()
