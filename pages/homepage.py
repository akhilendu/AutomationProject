from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self,driver):
        self.driver = driver
        self.admin=(By.XPATH, "//li[@class='nav-item dropdown']")
        self.logoutbutton=(By.XPATH, "//i[@class='ace-icon fa fa-power-off']")
    def click_admin(self):
      admin = self.driver.find_element(*self.admin).click()
    def click_logout(self):
        self.driver.find_element(*self.logoutbutton).click()