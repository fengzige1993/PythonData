"""
conftest 公共文件，放在测试用例的同一个包下面
"""
import pytest


@pytest.fixture(scope="session")
def connectDB():
    print("连接数据库的操作")
    yield
    print("断开数据库的连接")