from selenium import webdriver
import time
d=webdriver.Chrome("C:\\Users\\rashmi\\AppData\\Local\\Programs\\Python\\Python35\\Scripts\\chromedriver.exe")
d.implicitly_wait(10)
d.get("https://www.urbanladder.com/")
d.implicitly_wait(5)
d.find_element_by_class_name("close-reveal-modal hide-mobile").click()
# d.find_element_by_xpath("//div[@id='topnav_wrapper']/ul/li/span[contains(text(),'Sale')]")
# d.find_element_by_xpath("////div[@id='topnav_wrapper']/ul/li/span[contains(text(),'Living')]")
# d.find_element_by_xpath("//div[@id='topnav_wrapper']/ul/li/span[contains(text(),'Bedroom')]")
# d.find_element_by_xpath("//div[@id='topnav_wrapper']/ul/li/span[contains(text(),'Dining')]")
# d.find_element_by_xpath("//div[@id='topnav_wrapper']/ul/li/span[contains(text(),'')]")
d.implicitly_wait(5)
list=d.find_elements_by_xpath("//div[@id='topnav_wrapper']/ul/li/span[@class='topnav_itemname']")
for i in list:
    print(i.text)



