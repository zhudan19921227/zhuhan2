'''
1.输入13362683621,输入密码：zhuhan19921227 点击登入
2.输入13362683621 输入密码 ""，点击登入
3.输入13362683621,输入密码：zhuhan19921227，点记住登入，点击登入按钮，
4.忘记密码
'''
import json
import os
from selenium import webdriver
import allure

from page.login_page import LoginPage
import pytest

from testCase.data.read import getData

url = "https://www.wlrc.com/"
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/data.yaml')
@allure.feature("登入模块")
@allure.story('登入测试用例')
@allure.severity('critical')
class TestLoginPageCase:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.login = LoginPage(cls.driver)

    def setup(self):
        self.driver.get(url)
        self.login.is_alter_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @allure.title("输入用户名,输入密码, 点击保持登入，点击登入")
    @pytest.mark.parametrize("data,rep",getData(path))
    def test001(self,data,rep):
        '''1.输入用户名,输入密码, 点击保持登入，点击登入'''
        self.login.input_user(json.loads(data)["user"])
        self.login.input_password(json.loads(data)["password"])
        self.login.click_login_button()
        result = self.login.get_login_name()
        assert result == json.loads(rep)["loginName"]

    def test002(self):
        '''4.忘记密码'''
        self.login.forget_name()
        result = self.login.is_check_exist()
        assert result

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

if __name__ == '__main__':
    pytest.main(['test_login_jenkins2.py','-s','--alluredir','../report/tmp'])
    os.system('allure generate  ../report/tmp  -o  ../report/report  --clean')