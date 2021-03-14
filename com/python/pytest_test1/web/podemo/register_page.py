"""
register_page
"""
# from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage():
    """注册页面"""
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def register(self):
        """注册"""
        #输入公司名
        self.driver.find_element(By.ID, "corp_name").send_keys("枫神集团")
        #输入管理者姓名
        self.driver.find_element(By.ID, "manager_name").send_keys("枫神")
        #输入电话号
        self.driver.find_element(By.ID, "register_tel").send_keys("18225893616")
        #点击注册
        self.driver.find_element(By.ID, "submit_btn").click()

        # return True
