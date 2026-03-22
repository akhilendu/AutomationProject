import time

import pytest
from selenium.webdriver.common.by import By

from pages.loginpage import Loginpage
from utilities import excelutility
from utilities.excelutility import ExcelUtility


class Test_login:
    @pytest.mark.order(1)
    def test_verify_validlogin(self,browzer_instance):
        self.driver = browzer_instance
        excelutility = ExcelUtility("C:\\Users\\Akhilendu\\Downloads\\TestData.xlsx")
        username_value = excelutility.get_string_data(2,1,"LoginPage")
        password_value = excelutility.get_string_data(2,2,"LoginPage")
        #username=self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(username_value)
        # password=self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys(password_value)
        # login=self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        loginpage=Loginpage(self.driver)
        loginpage.enter_username(username_value)
        loginpage.enter_password(password_value)
        loginpage.click_login()
        time.sleep(2)
        actualurl = self.driver.current_url
        assert actualurl == "https://groceryapp.uniqassosiates.com/admin"

    @pytest.mark.order(2)
    def test_verify_invaliduserValidpassword(self,browzer_instance):
        self.driver = browzer_instance
        excelutility = ExcelUtility("C:\\Users\\Akhilendu\\Downloads\\TestData.xlsx")
        username_value = excelutility.get_string_data(3, 1, "LoginPage")
        password_value = excelutility.get_string_data(3, 2, "LoginPage")
        # username=self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(username_value)
        # password=self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys(password_value)
        # login = self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(username_value)
        loginpage.enter_password(password_value)
        loginpage.click_login()
        actualurl = self.driver.current_url
        assert actualurl == "https://groceryapp.uniqassosiates.com/admin/login"

    @pytest.mark.order(3)
    def test_verify_validuserInvalidpwd(self,browzer_instance):
        self.driver = browzer_instance
        excelutility = ExcelUtility("C:\\Users\\Akhilendu\\Downloads\\TestData.xlsx")
        username_value = excelutility.get_string_data(3, 1, "LoginPage")
        password_value = excelutility.get_string_data(3, 2, "LoginPage")
        # username = self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username_value)
        # password = self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password_value)
        # login = self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(username_value)
        loginpage.enter_password(password_value)
        loginpage.click_login()
        actualurl = self.driver.current_url
        assert actualurl == "https://groceryapp.uniqassosiates.com/admin/login"

    @pytest.mark.order(4)
    def test_verify_invaliduserandPwd(self,browzer_instance):
        self.driver = browzer_instance
        excelutility = ExcelUtility("C:\\Users\\Akhilendu\\Downloads\\TestData.xlsx")
        username_value = excelutility.get_string_data(4, 1, "LoginPage")
        password_value = excelutility.get_string_data(4, 2, "LoginPage")
        # username = self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username_value)
        # password = self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password_value)
        # login = self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(username_value)
        loginpage.enter_password(password_value)
        loginpage.click_login()
        actualurl = self.driver.current_url
        assert actualurl == "https://groceryapp.uniqassosiates.com/admin/login"













