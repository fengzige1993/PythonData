"""
test_contact
"""
from com.python.pytest_test1.web.selenium_po.page.main_page import MainPage


class TestContact:

    def setup(self):
        #实例化MainPage()
        self.mainpage = MainPage()


    def test_addmember(self):
        assert self.mainpage.goto_add_member().add_member()