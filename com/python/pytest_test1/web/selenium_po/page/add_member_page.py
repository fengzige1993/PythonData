"""
add_menber_page
python+selenium获取分页的数据内容
# 获取联系人的列表[包括页面元素很多的时候]
    def get_member(self):
        # 查看页面是否有分页的元素出现
        pages: str=self.finds(By.CSS_SELECTOR, '.ww_pageNav_info_text')
        print(pages)
        # if len(pages) == 0:
        # 如果列表为0,证明只有第一页,所有的名字都在第一页;
        # 无论是否只有一页,都需要获取第一页的数据
        members_name_list=self.finds(By.XPATH, '//*[@id="member_list"]/tr/td[2]')
        # 将第一页找到的元素的title都放到title_list中
        title_list = []
        # title_list=[element.get_attribute("title") for element in members_name_list]
        for element in members_name_list:
            # 获取title
            title_list.append(element.get_attribute("title"))
        if len(pages) > 0:
            # 证明有翻页功能,需要去翻页
            page: str=self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
            num, total=page.split('/')
            print(int(num), int(total))
            n=int(num)
            t=int(total)
            for i in range(1, t+1):
                self.find(By.CSS_SELECTOR, '.ww_commonImg_PageNavArrowRightNormal').click()
                members_name_list=self.finds(By.XPATH, '//*[@id="member_list"]/tr/td[2]')
                # title_list=[element.get_attribute("title") for element in members_name_list]
                for element in members_name_list:
                    # 获取title
                    title_list.append(element.get_attribute("title"))
        return title_list


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

    def add_member(self, username,account,phone):
        """添加成员"""
        #输入用户名
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)")))
        # self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("AifengAi003")
        while 1:
            try:
                self.driver.find_element(By.ID,"username").send_keys(username)
                break
            except:
                print("没有找到元素")
        #输入账号
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys(account)
        #输入手机号
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys(phone)
        #点击保存,当页面上相同属性的元素有多个时，通过find_element 找到的是第一个元素
        self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()

    def get_member(self):
        """获取所有的联系人姓名"""

        #查看页面是否有分页的元素
        pages: str=self.driver.find_elements(By.CSS_SELECTOR,".ww_pageNav_info_text")
        #显式等待勾选框可以点击
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".member_colRight_memberTable_th_Checkbox")))
        #拿到第一页所有的姓名元素,这里要用find_elements ,因为是取出的元素是列表数据，是一个集合，要用elements
        eles_list = self.driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        #把姓名的title文本属性取出放入list当中
        names = []
        for ele in eles_list:
            names.append(ele.get_attribute("title"))
        #如果找到有翻页的元素就去翻页
        if len(pages) > 0:
            page: str=self.driver.find_element(By.CSS_SELECTOR,".ww_pageNav_info_text").text
            num, total = page.split("/")
            # n = int(num)
            t = int(total)
            for  i in range(1, t+1):
                self.driver.find_element(By.CSS_SELECTOR,".ww_commonImg_PageNavArrowRightNormal").click()
                members_name_list = self.driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
                for pagelist in members_name_list:
                    names.append(pagelist.get_attribute("title"))
        return names
        #返回列表中的全部姓名
