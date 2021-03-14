"""
add_menber_page

"""
# from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AddMemberPage:
    """添加成员类"""
    def __init__(self,driver:WebDriver):
        """driver:WebDriver 加载最底层的 WebDriver驱动，有提示作用"""
        self.driver = driver

    def add_member(self):
        """添加成员"""
        #输入用户名
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)")))
        # self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("AifengAi003")
        self.driver.find_element(By.ID,"username").send_keys("AifengAi012")
        #输入账号
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys("AifengAi012C")
        #输入手机号
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys("18221800012")
        #点击保存,当页面上相同属性的元素有多个时，通过find_element 找到的是第一个元素
        self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()

        return True
