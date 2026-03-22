import time

from selenium.webdriver.common.by import By

from pages.homepage import Homepage
from pages.loginpage import Loginpage
from utilities.excelutility import ExcelUtility


class Test_Logout:
    def test_verify_logoutfunction(self, browzer_instance):
       self.driver = browzer_instance
       excelutility = ExcelUtility("C:\\Users\\Akhilendu\\Downloads\\TestData.xlsx")
       username_value = excelutility.get_string_data(2, 1, "LoginPage")
       password_value = excelutility.get_string_data(2, 2, "LoginPage")
       # username = self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username_value)
       # password = self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password_value)
       # login = self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
       # admin = self.driver.find_element(By.XPATH, "//li[@class='nav-item dropdown']").click()
       time.sleep(5)
       # logout = self.driver.find_element(By.XPATH, "//i[@class='ace-icon fa fa-power-off']").click()
       loginpage = Loginpage(self.driver)
       loginpage.enter_username(username_value)
       loginpage.enter_password(password_value)
       loginpage.click_login()
       logoutpage = Homepage(self.driver)
       logoutpage.click_admin()
       logoutpage.click_logout()
       time.sleep(5)

       actualurl = self.driver.current_url
       assert actualurl == "https://groceryapp.uniqassosiates.com/admin/login"





