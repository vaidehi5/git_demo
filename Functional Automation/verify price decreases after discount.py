from selenium import webdriver
import time

#Explicit wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
veglist1=[]
veglist2=[]
driver = webdriver.Chrome("D:\Python_Selenium_Concepts\drivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
productlist = driver.find_elements_by_xpath("//div[@class='products']/div")
print(len(productlist))
assert len(productlist)==3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for btn in buttons:
    veglist1.append(btn.find_element_by_xpath("parent::div/parent::div/h4").text)
    btn.click()
print(veglist1)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 10)

wait.until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, "promoCode")))

veggies = driver.find_elements_by_css_selector("p.product-name")
for veg in veggies:
    veglist2.append(veg.text)
print(veglist2)

assert veglist1 == veglist2

before_discount=driver.find_element_by_css_selector(".discountAmt").text
print(before_discount)
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element_by_css_selector("span.promoInfo").text)

after_discount = driver.find_element_by_css_selector(".discountAmt").text
print(after_discount)
assert float(after_discount) < float(before_discount)  # as these amounts are string so will convert to integer or float



driver.close()