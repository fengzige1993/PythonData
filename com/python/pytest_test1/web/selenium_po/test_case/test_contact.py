"""
test_contact
"""
from com.python.pytest_test1.web.selenium_po.page.main_page import MainPage


class TestContact:

    def setup(self):
        #实例化MainPage()
        self.mainpage = MainPage()


    def test_addmember(self):
        username = "AifengAi2335"
        account = "AifengAi2335C"
        phone = "18221802335"

        page = self.mainpage.goto_add_member()
        page.add_member(username,account,phone)
        names = page.get_member()
        assert username in names
        #断言新添加的姓名是不是在已添加好的姓名列表中