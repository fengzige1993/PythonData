"""
frame 多窗口切换
"""
from com.python.pytest_test1.selenium_frame_window.base import TestWindows


class TestFrame(TestWindows):
    """切换frame"""

    def test_frame(self):
        """
        1.如果要操作frame中的标签数据，需要切换到frame框架中
        2.查看是否是frame嵌套，查找父级frame标签
        :return:
        """
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #切换到iframe 框架中
        #方法一
        self.driver.switch_to.frame("iframeResult")
        #方法二
        # self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element_by_id('draggable').text)
        #切回到默认frame页面
        #方法一
        # self.driver.switch_to.parent_frame()
        #方法二
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)