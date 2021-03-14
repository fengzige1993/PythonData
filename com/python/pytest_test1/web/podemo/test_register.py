"""
test_register
"""
from com.python.pytest_test1.web.podemo.index_page import IndexPage

class TestRegister:
    """注册测试case"""

    def setup(self):
        """setup方法实例化IndexPage()类得到首页模块"""
        self.index = IndexPage()

    def test_register(self):

        assert self.index.goto_register().register()
