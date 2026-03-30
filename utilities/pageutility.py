from selenium.webdriver.support.select import Select
class Page_utility:
    def staff_select(self,element):
        select = Select(element)
        select.select_by_value("staff")

