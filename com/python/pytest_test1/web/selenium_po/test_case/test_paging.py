"""
分页
--获取分页的数据
--Variable annotations：变量注释”
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


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
