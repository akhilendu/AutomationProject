from selenium.webdriver.common.by import By
from utilities.wait_utility import Wait_utility


class Loginpage:

    def __init__(self,driver):
        self.driver = driver
        self.wait_utility=Wait_utility()
        self.login_username=(By.XPATH, "//input[@name='username']")
        self.login_password=(By.XPATH, "//input[@name='password']")
        self.login_button=(By.XPATH, "//button[@type='submit']")
    def enter_username(self,username_value):
        self.driver.find_element(*self.login_username).send_keys(username_value)
        return self
    def enter_password(self,password_value):
        self.driver.find_element(*self.login_password).send_keys(password_value)
        return self
    def click_login(self):
        from pages.homepage import Homepage
        self.wait_utility.wait_until_clickable(self.driver,self.login_button)
        self.driver.find_element(*self.login_button).click()
        return Homepage(self.driver)



