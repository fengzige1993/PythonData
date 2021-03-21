"""
test_contact
"""

from com.python.pytest_test1.web.selenium_po.page.main_page import MainPage
from selenium.webdriver.support  import expected_conditions
from selenium.webdriver.common.by import By
import random
from com.python.pytest_test1.web.selenium_po.page.runcmd import TestPythonCMD
import commands
import os
import subprocess
import sys

class TestContact:
    """测试增加联系人"""

    def setup(self):
        """先CMD启用端口，然后在实例化MainPage()去执行测试用例"""

        #先CMD启用端口
        cmd1 = r"cd C:\Program Files (x86)\Google\Chrome\Application"
        cmd2 = "chrome --remote-debugging-port=9222"
        cmd  = cmd1 + "&&" + cmd2
        subprocess.Popen(cmd,shell=True)
        #实例化MainPage()
        self.mainpage = MainPage()


    def test_addmember(self):
        """添加成员"""

        username = "AifengAi0" + str(random.randint(1,100))
        phone = random.randint(18221800000, 18221810000)
        account = username + random.choice("abcdefghijklonopqrstuvwxyz12345678910111213141516171819")
        #实例化mainpage之后进行调用定义的添加成员方法
        page = self.mainpage.goto_add_member()
        page.add_member(username, account, phone)
        names = page.get_member()
        print(names)
        #对新添加的成员进行断言
        assert username in names

        # while 1:
        #     if (expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".ww_pageNav_info_text"))):
        #         break
        #     else:
        #         username = "AifengAi020"
        #         username1 = "AifengAi0"
        #         username2 = 20
        #         phone = random.randint(18221800000, 18221810000)
        #
        #         username2 = username2 + 1
        #         username = username1 + str(username2)
        #         account = username + "C"
        #
        #         page = self.mainpage.goto_add_member()
        #         page.add_member(username,account,phone)
        #         names = page.get_member()
        #         print(names)
        #         assert username in names
        #断言新添加的姓名是不是在已添加好的姓名列表中