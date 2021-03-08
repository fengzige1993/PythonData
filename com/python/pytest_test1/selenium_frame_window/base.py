"""
base
-- setup 和 teardown 基类

"""

import pytest
from selenium import webdriver
from time import sleep

class TestWindows():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardowd(self):
        self.driver.quit()