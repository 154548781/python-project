# url = input("请输入url地址：")
# name = input("请输入用户名：")
# password = input("请输入密码：")
# python打开浏览器
# os 操作系统接口模块
import os
os.startfile("C:\\Users\\zhangtingting\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")
os.system(r'C:\\Users\\zhangtingting\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe')
# noinspection PyUnresolvedReferences
#import webbrowser
#webbrowser.open('192.168.11.220')
# webbrowser.open(url, new=0, autoraise=True),
# webbrowser.open(urls)
# import requests,time
# http://192.168.11.220/login_auth.php
#import win32api
#win32api.ShellExecute(0,'open',"C:\\Users\\zhangtingting\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe",'','',1)
# selenium 导入浏览器驱动，用get方式打开浏览器
# noinspection PyUnresolvedReferences
from selenium import webdriver