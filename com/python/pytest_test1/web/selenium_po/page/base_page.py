"""
base_page
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from com.python.pytest_test1.web.selenium_po.page.runcmd import TestPythonCMD


class BasePage:

    #默认URL为空，什么都不去做，不去打开URL
    base_url =""
    # def __init__(self,driver:WebDriver):
    #     """driver:WebDriver 加载最底层的 WebDriver驱动，有提示作用"""
    #     self.driver = driver
    def __init__(self,driver:WebDriver = None):
        if driver == None:
            #服用浏览器需要设置 option.debugger_address
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            #创建完driver立刻设置隐士等待
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver
        if self.base_url !="":
            self.driver.get(self.base_url)

    #保存日志、截图
    def find(self,locator,value):
        return self.driver.find_element(locator,value)

    def finds(self,locator,value):
        return self.driver.find_elements(locator,value)

    def wait_for_click(self,time_out,locator):
        WebDriverWait(self.driver,time_out).until(expected_conditions.element_to_be_clickable((locator)))
