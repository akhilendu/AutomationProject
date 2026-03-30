from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.homepage import Homepage
from utilities.wait_utility import Wait_utility
from utilities.pageutility import Page_utility


class Adminpage:
    def __init__(self,driver):
        self.driver = driver
        self.wait_utility = Wait_utility()
        self.page_utility=Page_utility()
        #self.admintile=(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']")
        self.enter_name=(By.XPATH, "//input[@name='username']")
        self.enter_password=(By.XPATH, "//input[@name='password']")
        self.search=(By.XPATH, "//i[@class=' fa fa-search']")
        self.select_newbutton=(By.XPATH, "//a[@class='btn btn-rounded btn-danger']")
        self.enter_oldusername=(By.XPATH, "//input[@id='un']")
        self.usertypestaff=(By.XPATH, "//select[@name='user_type']")
        self.usertypesearch=(By.XPATH, "//select[@name='ut']")
        self.submit=(By.XPATH, "//button[@name='Search']")
        self.create=(By.XPATH, "//button[@name='Create']")
    # def enter_admintile(self):
    #     self.wait_utility.wait_until_clickable(self.driver,self.admintile)
    #     self.driver.find_element(*self.admintile).click()
    #     return self
    def enter_newusername(self,username_value):
        self.driver.find_element(*self.enter_name).send_keys("AkilenduPaiyoor")
        return self
    def enter_newpassword(self,password_value):
        self.driver.find_element(*self.enter_password).send_keys("hello")
        return self
    def select_search(self):
        self.driver.find_element(*self.search).click()
        return self
    def select_new(self):
        self.driver.find_element(*self.select_newbutton).click()
        return self
    def enter_username(self,username_value):
        username_value=self.driver.find_element(*self.enter_oldusername).send_keys("Akhilendu")
        return self
    def enter_usertype(self):
        usertype = self.driver.find_element(*self.usertypestaff)
        # select = Select(usertype)
        # select.select_by_value("staff")
        self.page_utility.staff_select(usertype)
        return self
    def enter_usertypeforsearch(self):
        usertype=self.driver.find_element(*self.usertypesearch)
        select = Select(usertype)
        select.select_by_value("staff")
        return self
    def click_submit(self):
        self.driver.find_element(*self.submit).click()
        return self
    def click_create(self):
        self.driver.find_element(*self.create).click()
        return self

