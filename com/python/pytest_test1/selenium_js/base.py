"""
base
-- setup 和 teardown 基类

"""

import pytest
from selenium import webdriver
import os
from time import sleep

class TestWindows():
    """浏览器调用基类"""

    def setup(self):
        """多浏览器处理"""
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.phantomjs()
        elif browser == 'ie':
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()