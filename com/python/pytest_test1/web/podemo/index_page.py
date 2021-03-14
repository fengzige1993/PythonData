"""
首页po
--先定义事件动作，再返回服务页面模块
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from com.python.pytest_test1.web.podemo.login_page import LoginPage
from com.python.pytest_test1.web.podemo.register_page import RegisterPage


class IndexPage:
    """企业微信的首页po"""

    def __init__(self):
        """定义初始化的构造方法"""
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        """进入登录页面"""
        #1. click login button
        self.driver.find_element(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        #2. rerurn LoginPage
        return LoginPage(self.driver)

    def goto_register(self):
         """进入到注册页面"""
         # 1. click register button
         self.driver.find_element(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn").click()
         # 2. rerurn RegisterPage
         return RegisterPage(self.driver)


