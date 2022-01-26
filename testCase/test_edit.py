import os
#sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
import pytest
from selenium import webdriver
from page.edit_page import Edit
from page2.login_page import LoginPage
from page.url import Url
import allure


@allure.feature("编辑简历")
class TestEditPageCase:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.edit = Edit(cls.driver)
        cls.loginNew = LoginPage(cls.driver)
    def setup(self):
        self.driver.get(Url)
        self.edit.is_exist_alter()
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.loginNew.login()

    @allure.story("求职意向")
    def test_001(self):

        self.edit.click_edit()
        self.edit.click_excepted_post()
        self.edit.clic_button()
        self.edit.click_place()
        self.edit.click_type()
        self.edit.click_state()
        self.edit.save()
        res = self.edit.is_success()
        assert res

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
if __name__ == '__main__':
    pytest.main(['test_ok.py','-s','--alluredir','../report/tmp'])
    os.system('allure generate  ../report/tmp  -o  ../report/report  --clean')