"""
main_page

"""
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from com.python.pytest_test1.web.selenium_po.page.add_member_page import AddMemberPage
from time import sleep
from com.python.pytest_test1.web.selenium_po.page.base_page import BasePage
# from com.python.pytest_test1.web.selenium_po.page.runcmd import TestPythonCMD


class MainPage(BasePage):
    """企业微信首页"""

    base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member(self):
        """添加成员功能服务"""
        # sleep(2)
        #click add member
        self.find(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)").click()
        # sleep(2)
        #return AddMemberPage
        return AddMemberPage(self.driver)

