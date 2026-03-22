from selenium.webdriver.common.by import By


class Loginpage:
    def __init__(self,driver):
        self.driver = driver
        self.login_username=(By.XPATH, "//input[@name='username']")
        self.login_password=(By.XPATH, "//input[@name='password']")
        self.login_button=(By.XPATH, "//button[@type='submit']")
    def enter_username(self,username_value):
        self.driver.find_element(*self.login_username).send_keys(username_value)
    def enter_password(self,password_value):
        self.driver.find_element(*self.login_password).send_keys(password_value)
    def click_login(self):
        self.driver.find_element(*self.login_button).click()


