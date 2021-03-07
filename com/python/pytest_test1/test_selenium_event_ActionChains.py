"""
test_ActionChains
--鼠标 单机 双击事件
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
import pytest
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    #定义setup方法
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    #定义teardown方法
    def teardown(self):
        self.driver.quit()

    #定义鼠标点击事件
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        element_doubleclick = self.driver.find_element_by_xpath("/html/body/form/input[2]")
        element_rightclick = self.driver.find_element_by_xpath("/html/body/form/input[4]")
        #ActionChains用法(分布式用法)
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(3)
        #调用perform()方法去执行添加进去的事件
        action.perform()
        sleep(3)

    #定义鼠标移动事件(光标移动到某个事件上)
    @pytest.mark.skip
    def test_moveto_element(self):
        self.driver.get("http://www.baidu.com")
        # ele = self.driver.find_element_by_link_text("设置")
        ele = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(2)

    #定义鼠标拖拽元素事件
    @pytest.mark.skip
    def test_drag_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath('/html/body/div[2]')

        #调用ActionChains
        action = ActionChains(self.driver)
        #方法一
        # action.drag_and_drop(drag_element,drop_element).perform()
        #方法二
        # action.click_and_hold(drag_element).release(drop_element).perform()
        #方法三
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        ele.click()
        #定义ActionChains
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)
# if __name__ == '__main__':
#     #可以在命令行里执行
#     pytest.main(['-v','s','test_selenium_event_ActionChains.py'])