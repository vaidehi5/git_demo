from selenium import webdriver
import time

driver = webdriver.Chrome("D:\Python_Selenium_Concepts\drivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text)
# this will not print the text , it will print blank because it was entered by selenium
# to get the text there are 2 ways
print(driver.find_element_by_name("name").get_attribute("value"))  # 1 way  because edit box doesn't have value attribute
print(driver.execute_script('return document.getElementsByName("name")[0].value')) # 2 way
# document.getElementsByName("name")[0]print this can be created in console of browser

shopbtn = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopbtn)

# selenium doesn't support scroll to , this can be done using java script executor

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")