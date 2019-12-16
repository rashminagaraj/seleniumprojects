import select
from selenium import webdriver
import time
d=webdriver.Chrome("C:\\Users\\rashmi\\AppData\\Local\\Programs\\Python\\Python35\\Scripts\\chromedriver.exe")
d.implicitly_wait(10)
d.get("https://www.amazon.in/")
selectall=d.find_element_by_id("searchDropdownBox")
select=select(selectall)