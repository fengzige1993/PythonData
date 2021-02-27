"""
test_calc_new

"""
import pytest
import yaml


with open("./datas/calc.yaml") as f:
    datas_f = yaml.safe_load(f)
    print("f文件里的内容为：",datas_f)
    datas = datas_f['add']
    print("datas参数为：",datas)
    add_datas = datas['datas']
    print("add_datas参数为:",add_datas)
    myid = datas['myid']
    print("myid参数为：",myid)

# """
# 文件名以【test_*】开头，类名以【Test*】开头，方法名以【test_*】开头
# 注意：测试类里一定不要加__init__()方法
# """
class TestCalc:

    @pytest.mark.parametrize(
        "a,b,expect",
        add_datas,ids=myid
    )
    @pytest.mark.add
    def test_add(self, get_calc, a, b, expect):
        """
        实例化计算器 ： self.calc = Calculator()
        定义result变量接收add方法的返回值
        调用相加方法
        :param a:
        :param b:
        :param expect:
        :return:
        """
        print("参数a为：",a)
        print("参数b为：",b)
        print("参数expect为：",expect)
        result = get_calc.add(a,b)
        #如果result是浮点类型的参数，就是保留两位小数
        if isinstance(result, float): # float
            result = round(result, 2)
        #得到相加结果之后写断言
        assert result == expect