from selenium.webdriver.common.by import By

class Homepage():

    def __init__(self):
        self.username_locator = (By.NAME,'username')
        self.password_locator = (By.NAME,'password')
        self.login_button_locator = (By.XPATH,"//input[@value='Log In']")
        self.forgot_login_locator = (By.XPATH,"//a[text()='Forgot login info?']")
        self.register_locator = (By.XPATH, "//a[text()='Register']")

    def Login_(self,pdriver):
        pdriver.find_element(*self.username_locator).send_keys("testuser")
        pdriver.find_element(*self.password_locator).send_keys("testuser")
        pdriver.find_element(*self.login_button_locator).click()

    def Click_register(self,pdriver):
        pdriver.find_element(*self.register_locator).click()

