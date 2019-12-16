from selenium import webdriver
import time
d=webdriver.Chrome("C:\\Users\\rashmi\\AppData\\Local\\Programs\\Python\\Python35\\Scripts\\chromedriver.exe")
d.implicitly_wait(10)
d.get("https://opensource-demo.orangehrmlive.com")
time.sleep(10)
d.find_element_by_id("txtUsername").send_keys("Admin")
d.find_element_by_id("txtPassword").send_keys("admin123")
d.implicitly_wait(10)
d.find_element_by_id("btnLogin").click()
d.find_element_by_id("welcome").click()
d.find_element_by_link_text("Logout").click()
