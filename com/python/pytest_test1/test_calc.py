"""
计算器 calc
"""
import pytest

class TestCalculator:
    #加法
    def add(self,a,b):
        return a + b

    #减法
    def sub(self,a,b):
        return a - b

    #乘法
    def mul(self,a,b):
        return a * b

    #除法
    def div(self,a,b):
        return  a / b
    @pytest.mark.add
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        if isinstance(result,format):
            result = round(result,2)
        assert result == expect

    @pytest.mark.add
    def test_add1(self):
        result = self.calc.add(0.1,0.1)
        assert result == 0.2

    @pytest.mark.add
    def test_add2(self):
        result = self.calc.add(-1,-1)
        assert result == -2

    @pytest.mark.div
    def test_div(self):
        print("test_div")

    @pytest.mark.sub
    def test_sub(self):
        print("test_sub")

    @pytest.mark.mul
    def test_mul(self):
        print("test_mul")












