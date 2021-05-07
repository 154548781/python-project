import pytesseract
from PIL import Image
from selenium import webdriver
import io
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(1)
swich = driver.find_element_by_class_name('login-hd-account').click()
uname = driver.find_element_by_id('J-userName').send_keys('15510507852')
pword = driver.find_element_by_id('J-password').send_keys('910526ting')
#伪装人的操作身份
script = 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined,});'
driver.execute_script(script)
#span = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
action = ActionChains(driver)
#action.click_and_hold(span)
action.move_by_offset(350, 0).perform()
action.release()