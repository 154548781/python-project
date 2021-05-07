from selenium import webdriver
from PIL import Image
from aip import AipOcr
driver = webdriver.Chrome()
driver.get('http://192.168.11.220/login.html')
driver.maximize_window()
usname = driver.find_element_by_id('username').send_keys('admin')
password = driver.find_element_by_id('password').send_keys('admin@123')
img = driver.find_element_by_id('myvld')
driver.find_element_by_id('myButton').click()
