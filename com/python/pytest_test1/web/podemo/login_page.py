"""
login_page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage():
    """登录服务页面"""
    def __init__(self,driver:WebDriver):
        #driver:WebDriver 指定变量参数的类型
        self.driver = driver
    def scan(self):
        """扫码"""
        pass

    def goto_register(self):
        """注册"""
        #click register link
        self.driver.find_element(By.CSS_SELECTOR,".login_registerBar_link").click()
        # return RegisterPage()
        return RegisterPage()


