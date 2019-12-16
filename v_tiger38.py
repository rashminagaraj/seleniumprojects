from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.get("http://localhost:8888/")

#pass username,password and click on
driver.find_element_by_name("user_name").send_keys("admin")
driver.find_element_by_name("user_password").send_keys("root")
driver.find_element_by_id("submitButton").click()

#click on organisation and click on find duplicates
driver.find_element_by_link_text("Organizations").click()
driver.find_element_by_xpath("//img[@title='Find Duplicates']").click()

#select any one duplicate column from option and
#it should display  msg page
sel=Select(driver.find_element_by_id("availList"))
sel.select_by_value("1")
driver.find_element_by_name("Button").click()
driver.find_element_by_name("save&merge").click()
act_msg=driver.current_url
exp_msg='http://localhost:8888/index.php?module=Accounts&action=FindDuplicateRecords'
if act_msg==exp_msg:
    print("pass")
else:
    print("fail")
driver.close()