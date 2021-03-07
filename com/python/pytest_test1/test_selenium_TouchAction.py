"""
test_TouchAction

"""
from selenium import webdriver
import pytest
from selenium.webdriver import TouchActions
from time import sleep


class TestTouchAction():

    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('data',['selenium测试'])
    def test_touchaction_scrollbottom(self, data):
        """
        打开chrome
        打开URL：http：//www.baidu.com
        向搜素框中输入'selenium测试'
        通过 TouchAction 点击搜索框
        滑动到底部，点击下一页
        关闭Chrome
        :return:
        """
        self.driver.get("https://www.baidu.com/")
        el_input = self.driver.find_element_by_id("kw")
        el_search = self.driver.find_element_by_id("su")
        el_input.send_keys(data)
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()

        #滑动
        action.scroll_from_element(el_input,0,10000).perform()
        sleep(3)