from datetime import time

from selenium.webdriver.common.by import By

from pages.adminpage import Adminpage
from pages.loginpage import Loginpage
from utilities.excelutility import ExcelUtility
from selenium.webdriver.support.select import Select


class Test_AdminLogin:
   def test_verifyusercreation(self, browzer_instance):
     self.driver = browzer_instance
     excelutility = ExcelUtility("C:\\Users\\Akhilendu\\Downloads\\TestData.xlsx")
     username_value = excelutility.get_string_data(2, 1, "LoginPage")
     password_value = excelutility.get_string_data(2, 2, "LoginPage")
     # username = self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username_value)
     # password = self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password_value)
     # login = self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
     # admintile = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']").click()
     # self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-danger']").click()
     # self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Akhilendu")
     # self.driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Hello")
     # usertype=self.driver.find_element(By.XPATH,"//select[@name='user_type']")
     # select=Select(usertype)
     # select.select_by_value("staff")
     # self.driver.find_element(By.XPATH, "//button[@name='Create']").click()
     loginpage = Loginpage(self.driver)
     loginpage.enter_username(username_value)
     loginpage.enter_password(password_value)
     loginpage.click_login()
     adminpage = Adminpage(self.driver)
     adminpage.enter_admintile()
     adminpage.select_new()
     adminpage.enter_newusername(username_value)
     adminpage.enter_newpassword(password_value)
     adminpage.enter_usertype()
     adminpage.click_create()
     actualurl=self.driver.current_url
     assert actualurl=="https://groceryapp.uniqassosiates.com/admin/list-admin?add=1"

   def test_searchusername(self, browzer_instance):
     self.driver = browzer_instance
     excelutility = ExcelUtility("C:\\Users\\Akhilendu\\Downloads\\TestData.xlsx")
     username_value = excelutility.get_string_data(2, 1, "LoginPage")
     password_value = excelutility.get_string_data(2, 2, "LoginPage")
     # username = self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username_value)
     # password = self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password_value)
     # login = self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
     # admintile = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']").click()
     # self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-danger']").click()
     # self.driver.find_element(By.XPATH, "//i[@class=' fa fa-search']").click()
     # self.driver.find_element(By.XPATH,"//input[@id='un']").send_keys("Akhilendu")
     # usertype = self.driver.find_element(By.XPATH, "//select[@name='ut']")
     # select = Select(usertype)
     # select.select_by_value("staff")
     # self.driver.find_element(By.XPATH, "//button[@name='Search']").click()
     loginpage = Loginpage(self.driver)
     loginpage.enter_username(username_value)
     loginpage.enter_password(password_value)
     loginpage.click_login()
     adminpage= Adminpage(self.driver)
     adminpage.enter_admintile()
     adminpage.select_search()
     adminpage.enter_username(username_value)
     adminpage.enter_usertypeforsearch()
     adminpage.click_submit()
     actualurl=self.driver.current_url
     assert actualurl=="https://groceryapp.uniqassosiates.com/admin/user/index?un=Akhilendu&ut=staff&Search=sr"




