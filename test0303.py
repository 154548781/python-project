from PIL import Image
from selenium import webdriver
import io
import time
import pytesseract
driver = webdriver.Chrome()
#打开网站
driver.get('http://192.168.11.220/login.html')
#输入用户名
usname = driver.find_element_by_id('username').send_keys('admin')
#输入密码
password = driver.find_element_by_id('password').send_keys('admin@123')
#聚焦验证码会刷新刷新验证码，需要先聚焦在进行屏幕截图
driver.find_element_by_id('vldcode').send_keys()
#屏幕截图
img = driver.save_screenshot('scree.png')
#图片处理函数
imgs = Image.open('scree.png')
#获取验证码位置
vcode = driver.find_element_by_id('myvld')
print(vcode.location)
print(vcode.size)
#返回在浏览器中的位置
location = vcode.location
#翻译图片大小 宽高
size = vcode.size
left = location['x']
top = location['y']
right = left + size['width']
bottom = top + size['height']
#切割验证码图片
vc = imgs.crop((left, top, right, bottom))
#指定一种图片色彩模式
cvcimg = vc.convert('L')
pixdata = cvcimg.load()
w, h = cvcimg.size
threshold = 160
for y in range(h):
    for x in range(w):
        if pixdata[x, y] < threshold:
            pixdata[x, y] = 0
        else:
            pixdata[x, y] = 255
num = pytesseract.image_to_string(cvcimg)

vcodes = driver.find_element_by_id('vldcode').send_keys(num)

driver.find_element_by_id('myButton').click()
#cvcimg.show()