from selenium.webdriver.common.by import By
from utilities.wait_utility import Wait_utility


class News:
  def __init__(self,driver):
      self.driver = driver
      self.wait_utility = Wait_utility()
      #self.managenews_tile=(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']")
      self.breadcrumb=(By.XPATH, "//li[@class='breadcrumb-item']")
      self.newbutton=(By.XPATH,"//a[@class ='btn btn-rounded btn-danger']")
      self.newsinfo=(By.XPATH, "//textarea[@id='news']")
      self.submit=(By.XPATH, "//button[@type='submit']")
      self.searchbutton=(By.XPATH, "//i[@class=' fa fa-search']")
      self.enter_news=(By.XPATH,"//input[@class='form-control']")
  # def click_managetile(self):
  #     self.wait_utility.wait_until_clickable(self.driver, self.managenews_tile)
  #     self.driver.find_element(*self.managenews_tile).click()
  def click_breadcrumb(self):
      from pages.homepage import Homepage
      self.driver.find_element(*self.breadcrumb).click()
      return Homepage(self.driver)
  def click_newbutton(self):
      self.driver.find_element(*self.newbutton).click()
      return self
  def click_searchbutton(self):
      self.driver.find_element(*self.searchbutton).click()
      return self
  def enter_newsinfo(self):
      self.driver.find_element(*self.newsinfo).send_keys("welcome")
      return self
  def type_news(self,message):
      self.driver.find_element(*self.enter_news).send_keys(message)
      return self
  def click_submit(self):
      self.driver.find_element(*self.submit).click()
      return self
  def search_news(self):
      self.driver.find_element(*self.searchbutton).click()
      return self


