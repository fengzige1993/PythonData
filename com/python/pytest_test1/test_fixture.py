"""
fixture : 用法
用fixture 实现不同的测试用例准备
"""

import pytest

#方法一：
#加上pytest的fixture装饰器，变成fixture()方法
@pytest.fixture()
def login():
    print("用户登陆")
    #yield 关键字可以激活 fixture 的 teardown 功能
    yield
    print("注销操作")
"""在测试用例中传入 fixture 方法名实现调用登陆"""
#需要提前登陆
def test_case1(login):
     print("测试用例1")


def test_case2():
    print("测试用例2")

"""在测试用例中传入 fixture 方法名实现调用登陆"""
#需要提前登陆
def test_case3(login):
    print("测试用例3")

#方法二：（优点--可以不用向方法里面传参）
#使用装饰器的方法，实现用户先登陆操作,装饰器传入的参数为字符串
@pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")

