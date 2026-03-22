import pytest
from selenium import webdriver


@pytest.fixture
def browzer_instance():
   driver = webdriver.Chrome()
   driver.get("https://groceryapp.uniqassosiates.com/admin/login")
   yield driver


