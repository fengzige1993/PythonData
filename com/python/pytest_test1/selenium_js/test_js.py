"""
test js
--处理滑动滚动条
--处理时只读的时间控件
"""
from com.python.pytest_test1.selenium_js.base import TestWindows
from time import sleep
import  pytest



class TestJs(TestWindows):
    """jS测试类"""

    @pytest.mark.skip
    def test_js_scroll(self):
        """js滑动处理"""
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys("selenium测试")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=0")
        # 执行滑动，回到页面的最顶端
        sleep(1)
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        #执行滑动，滑到页面的最底端
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(3)
        #用法一
        # for code in [
        #     'return document.title','return JSON.stringify(performance.timing)'
        # ]:
        #用法二
        print(self.driver.execute_script('return document.title ; return JSON.stringify(performance.timing)'))

    def test_datetime(self):
        """更改12306出发日期的时间控件"""
        self.driver.get("https://www.12306.cn/index/")
        #先移除只读模式，然后再去赋值，分两步走，可以修改时间控件成功
        self.driver.execute_script("document.getElementById('train_date').removeAttribute('readonly ')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))