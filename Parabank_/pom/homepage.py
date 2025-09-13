from selenium.webdriver.common.by import By

class Homepage():
    def __init__(self,pdriver):
        self.driver = pdriver
        self._register_user = (By.XPATH, '//a[text()="Register"]')

    def register_new_user(self):
        self.driver.find_element(*self._register_user).click()