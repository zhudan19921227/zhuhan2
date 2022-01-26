import os
import sys

import allure
from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.by import By

url="https://www.wlrc.com/"


class LoginPage(Base):
    loc_user = (By.ID,"username")
    loc_password = (By.NAME,"password")
    loc_button = (By.CSS_SELECTOR,"#form-login > button")
    loc_keep = (By.CLASS_NAME,"checkbox-custom")
    loc_forget = (By.CLASS_NAME,"forget-type3")
    loc_forgetList = (By.CSS_SELECTOR,"body > div.forget-main > span")
    loc_loginName = (By.CSS_SELECTOR,"ul.float-right.zwq-marbottom > li > a")

    @allure.step("输入用户名")
    def input_user(self,text):
        self.sendKey(self.loc_user,text)

    @allure.step("输入密码")
    def input_password(self,text):
        self.sendKey(self.loc_password,text)

    @allure.step("点击登入")
    def click_login_button(self):
        self.click(self.loc_button)

    @allure.step("输保持登入")
    def keep_login(self):
        self.click(self.loc_keep)

    @allure.step("点击忘记密码")
    def forget_name(self):
        self.click(self.loc_forget)

    @allure.step("获取登入名")
    def get_login_name(self):
        res = self.get_text(self.loc_loginName)
        return res

    def is_alter_exist(self):
            try:
                alter = self.driver.switch_to.alert
                text = alter.text
                alter.accept()
                return text
            except:
                return ""
    @allure.step("判断忘记密码页是否存在")
    def is_check_exist(self):
        re = self.is_Element_Exsit(self.loc_forgetList)
        return re

    @allure.step("输入用户名，输入密码，点击登入")
    def login(self,user="13362683621",psw="zhuhan19921227"):
        self.input_user(user)
        self.input_password(psw)
        self.click_login_button()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get(url)
    login = LoginPage(driver)
    """login.input_user("13362683621")
    login.input_password("zhuhan19921227")
    login.keep_login()
    login.click_login_button()
    r = login.get_login_name()
    print(r)"""
    login.login()
