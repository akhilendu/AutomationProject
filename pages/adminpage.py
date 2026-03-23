from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Adminpage:
    def __init__(self,driver):
        self.driver = driver
        self.admintile=(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']")
        self.enter_name=(By.XPATH, "//input[@name='username']")
        self.enter_password=(By.XPATH, "//input[@name='password']")
        self.search=(By.XPATH, "//i[@class=' fa fa-search']")
        self.select_new=(By.XPATH, "//a[@class='btn btn-rounded btn-danger']")
        self.enter_oldusername=(By.XPATH, "//input[@id='un']")
        self.usertype=(By.XPATH, "//select[@name='user_type']")
        self.usertypesearch=(By.XPATH, "//select[@name='ut']")
        self.submit=(By.XPATH, "//button[@name='Search']")
        self.create=(By.XPATH, "//button[@name='Create']")
    def enter_admintile(self):
        self.driver.find_element(*self.admintile).click()
    def enter_newusername(self,username_value):
        self.driver.find_element(*self.enter_name).send_keys("AkilenduPaiyoor")
    def enter_newpassword(self,password_value):
        self.driver.find_element(*self.enter_password).send_keys("hello")
    def select_search(self):
        self.driver.find_element(*self.search).click()
    def select_new(self):
        self.driver.find_element(*self.select_new).click()
    def enter_username(self,username_value):
        username_value=self.driver.find_element(*self.enter_oldusername).send_keys("Akhilendu")
    def enter_usertype(self):
        usertype = self.driver.find_element(*self.usertype).text
        select = Select(usertype)
        select.select_by_value("staff")
    def enter_usertypeforsearch(self):
        usertype=self.driver.find_element(*self.usertypesearch)
        select = Select(usertype)
        select.select_by_value("staff")
    def click_submit(self):
        self.driver.find_element(*self.submit).click()
    def click_create(self):
        self.driver.find_element(*self.create).click()

