from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.by import By
import allure

from page.login_page import LoginPage


class Edit(Base):
    loc_edit = (By.CLASS_NAME,"btn-edit")
    loc_post = (By.XPATH,"//*[@id='intention']/form/div[1]/div/div/input")
    loc_clickPost = (By.XPATH,"/html/body/div[3]/div/div[2]/ul/li[2]/div/div[2]/div/label[1]/span[1]/span")
    loc_button = (By.XPATH,"/html/body/div[3]/div/div[1]/div/div[2]/button[1]/span")
    loc_place = (By.XPATH,'//*[@id="intention"]/form/div[2]/div[1]/div/div/div/div[1]/input')
    loc_place1 = (By.CSS_SELECTOR,' ul > ul > li:nth-child(2) > ul > li:nth-child(1)')
    loc_type = (By.XPATH,'//*[@id="intention"]/form/div[2]/div[2]/div/div/div/div/input')
    loc_type1 = (By.XPATH,'//div[3]/div[1]/div[1]/ul/li[3]')
    loc_place2 = (By.CSS_SELECTOR,' ul > ul > li:nth-child(2) > ul > li:nth-child(3) > span')
    loc_state = (By.XPATH,'//*[@id="intention"]/form/div[4]/div/div/div/input')
    loc_state1 = (By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li[1]')
    loc_save = (By.CSS_SELECTOR,' button.el-button.el-button--primary > span')
    loc_success = (By.CSS_SELECTOR,'#intention > div.intention > div > div > p:nth-child(1)')
    loc_update = (By.CSS_SELECTOR,'#intention > div.v-title > div.v-title-href > div')

    @allure.step("点击编辑我的简历")
    def click_edit(self):
        self.click(self.loc_edit)
        self.click(self.loc_update)
    @allure.step("点击期望岗位")
    def click_excepted_post(self):
        self.click(self.loc_post)
        self.click(self.loc_clickPost)

    @allure.step("点击确定按钮")
    def clic_button(self):
        self.click(self.loc_button)

    @allure.step("点击期望地址")
    def click_place(self):
        self.click(self.loc_place)
        self.move_to_element(self.loc_place1)
        self.click(self.loc_place1)
        self.move_to_element(self.loc_place2)
        self.click(self.loc_place2)
    @allure.step("点击工作类型")
    def click_type(self):
        self.click(self.loc_type)
        self.move_to_element(self.loc_type1)
        self.click(self.loc_type1)


    @allure.step("点击当前状态")
    def click_state(self):
        self.click(self.loc_state)
        self.move_to_element(self.loc_state1)
        self.click(self.loc_state1)

    @allure.step("点击保存")
    def save(self):
        self.click(self.loc_save)

    def is_success(self):
        r = self.is_Element_Exsit(self.loc_success)
        return r

if __name__ == '__main__':
    url = "https://www.wlrc.com/"
    driver = webdriver.Chrome()
    driver.get(url)
    login = LoginPage(driver)
    login.login()
    edit = Edit(driver)
    edit.click_edit()
    edit.click_excepted_post()
    edit.clic_button()
    edit.click_place()
    edit.click_type()
    edit.click_state()
    edit.save()
    r = edit.is_success()
    print(r)


    """login.input_user("13362683621")
    login.input_password("zhuhan19921227")
    login.keep_login()
    login.click_login_button()
    r = login.get_login_name()
    print(r)"""


