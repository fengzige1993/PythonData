"""
main_page

"""
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from com.python.pytest_test1.web.selenium_po.page.add_member_page import AddMemberPage
from time import sleep

class MainPage:
    """企业微信首页"""

    def __init__(self):
        #复用浏览器，需要设置option.debugger_address
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver =  webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def goto_add_member(self):
        """添加成员功能服务"""
        # sleep(2)
        #click add member
        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)").click()
        # sleep(2)
        #return AddMemberPage
        return AddMemberPage(self.driver)

