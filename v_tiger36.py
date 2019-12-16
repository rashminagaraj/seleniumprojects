from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()

#launch website
driver.get("http://localhost:8888/")

#pass username,password and click on
driver.find_element_by_name("user_name").send_keys("admin")
driver.find_element_by_name("user_password").send_keys("root")
driver.find_element_by_id("submitButton").click()

#click on organisation and click on create filter
driver.find_element_by_link_text("Organizations").click()
driver.find_element_by_link_text("Create Filter").click()

#select same column name and it should display alert error msg
sel=Select(driver.find_element_by_name("column2"))
sel.select_by_index(1)
time.sleep(2)
alt=driver.switch_to_alert()
act_msg=alt.text
exp_msg="Columns cannot be duplicated"
assert act_msg==exp_msg,print("Fail")
print("pass")
driver.close()