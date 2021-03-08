"""
test_window
--多窗口处理
"""
import pytest
from selenium import webdriver
from com.python.pytest_test1.selenium_frame_window.base import TestWindows
from time import sleep

class TestWindows(TestWindows):
    """多窗口切换类"""

    def test_window(self):
        """打印当前全部窗口，用列表取要切换到的窗口"""
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        print('登录之后的当前窗口',self.driver.current_window_handle)
        print('登录之后的全部窗口',self.driver.window_handles)

        self.driver.find_element_by_link_text("立即注册").click()
        print('立即注册之后的当前窗口',self.driver.current_window_handle)
        print('立即注册之后的全部窗口',self.driver.window_handles)
        windows = self.driver.window_handles
        #"""得到当前全部窗口"""
        self.driver.switch_to.window(windows[-1])
        #"""切换到新的窗口"""
        #进行用户的注册
        self.driver.find_element_by_css_selector('#TANGRAM__PSP_4__userName').send_keys("username")
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys("18221801111")
        sleep(2)
        self.driver.switch_to.window(windows[0])
        # """回到用户名登录页，切换窗口"""
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        # """进行点击用户名登录"""
        # 进行用户名密码的登录
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys("login_username")
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys("login_password")
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(3)

