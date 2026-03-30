from selenium.webdriver.common.by import By
from utilities.wait_utility import Wait_utility


class Homepage:
    def __init__(self,driver):
        self.wait_utility = Wait_utility()
        self.driver = driver
        self.admin=(By.XPATH, "//li[@class='nav-item dropdown']")
        self.logoutbutton=(By.XPATH, "//i[@class='ace-icon fa fa-power-off']")
        self.admintile = (By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']")
        self.managenews_tile = (By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']")
    def click_admin(self):
        admin = self.driver.find_element(*self.admin).click()
        return self
    def click_logout(self):
        from pages.loginpage import Loginpage
        self.wait_utility.wait_until_clickable(self.driver, self.logoutbutton)
        self.driver.find_element(*self.logoutbutton).click()
        return Loginpage(self.driver)
    def enter_admintile(self):
        from pages.adminpage import Adminpage
        self.wait_utility.wait_until_clickable(self.driver,self.admintile)
        self.driver.find_element(*self.admintile).click()
        return Adminpage(self.driver)

    def click_managetile(self):
        from pages.newspage import News
        self.wait_utility.wait_until_clickable(self.driver, self.managenews_tile)
        self.driver.find_element(*self.managenews_tile).click()
        return News(self.driver)