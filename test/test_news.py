import time

import pytest
from selenium.webdriver.common.by import By

from pages.loginpage import Loginpage
from pages.newspage import News
from test.conftest import browzer_instance
from utilities.excelutility import ExcelUtility


class Test_news:
    def test_verifymanagenews(self, browzer_instance):
        self.driver = browzer_instance
        excelutility = ExcelUtility("C:\\Users\\Akhilendu\\Downloads\\TestData.xlsx")
        username_value = excelutility.get_string_data(2, 1, "LoginPage")
        password_value = excelutility.get_string_data(2, 2, "LoginPage")
        # username = self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username_value)
        # password = self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password_value)
        # login = self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        #manangetile=self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']").click()
        #time.sleep(2)
        #home=self.driver.find_element(By.XPATH,"//li[@class='breadcrumb-item']").click()
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(username_value)
        loginpage.enter_password(password_value)
        loginpage.click_login()
        news=News(self.driver)
        news.click_managetile()
        time.sleep(2)
        news.click_breadcrumb()


    def test_verify_addnews(self,browzer_instance):
        self.driver = browzer_instance
        excelutility = ExcelUtility("C:\\Users\\Akhilendu\\Downloads\\TestData.xlsx")
        username_value = excelutility.get_string_data(2, 1, "LoginPage")
        password_value = excelutility.get_string_data(2, 2, "LoginPage")
        # username = self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username_value)
        # password = self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password_value)
        # login = self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # time.sleep(2)
        #manangetile=self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']").click()
        # time.sleep(2)
        # newbutton=self.driver.find_element(By.XPATH,"//a[@class ='btn btn-rounded btn-danger']").click()
        # self.driver.find_element(By.XPATH,"//textarea[@id='news']").send_keys("Welcome")
        # submit=self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(username_value)
        loginpage.enter_password(password_value)
        loginpage.click_login()
        news = News(self.driver)
        news.click_managetile()
        time.sleep(2)
        news.click_newbutton()
        news.enter_newsinfo()
        news.click_submit()
        actualurl=self.driver.current_url
        assert actualurl == "https://groceryapp.uniqassosiates.com/admin/News/add"

    @pytest.mark.parametrize("newsinfo",["new1","current","sports"])
    def test_verifySearch(self,browzer_instance,newsinfo):
        self.driver = browzer_instance
        excelutility = ExcelUtility("C:\\Users\\Akhilendu\\Downloads\\TestData.xlsx")
        username_value = excelutility.get_string_data(2, 1, "LoginPage")
        password_value = excelutility.get_string_data(2, 2, "LoginPage")
        # username = self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username_value)
        # password = self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password_value)
        # login = self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # time.sleep(2)
        # manangetile = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']").click()
        # time.sleep(2)
        # search=self.driver.find_element(By.XPATH,"//i[@class=' fa fa-search']").click()
        # self.driver.find_element(By.XPATH,"//input[@class='form-control']").send_keys("Welcome")
        # self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(username_value)
        loginpage.enter_password(password_value)
        loginpage.click_login()
        news = News(self.driver)
        news.click_managetile()
        time.sleep(2)
        news.click_searchbutton()
        news.type_news(newsinfo)
        news.click_submit()
        # actualurl=self.driver.current_url
        # assert actualurl=="https://groceryapp.uniqassosiates.com/admin/news/index"












