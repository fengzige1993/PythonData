"""
conftest 公共文件，放在测试用例的同一个包下面
--session 多个文件一起执行
"""
import pytest

#加上fixture装饰器变成fixture方法
@pytest.fixture(scope="session")
def connectDB():
    print("连接数据库的操作")
    yield
    print("断开数据库的连接")