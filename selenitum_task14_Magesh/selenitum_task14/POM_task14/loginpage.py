import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class LoginPage:
    # locators

# show example for class and instance variable
    #Initializing driver and wait time
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_locator = (By.XPATH, "//input[contains(@placeholder,'Enter your mail')]")
        self.password_locator = (By.XPATH, "//input[contains(@type, 'password')]")
        self.login_button_locator = (By.XPATH, "//button[contains(@type, 'submit')]")
        self.error_msg = (By.CSS_SELECTOR, ".error")
        # dropdown_click = (By.ID, "profile-click-icon")
        self.user_profile_locator = (By.CLASS_NAME, "user-name-div")
        self.custom_button = (By.XPATH,"//button[@class='custom-close-button']")
        self.logout_button_locator = (By.XPATH, "//div[text()='Log out']")

    def login(self, username, password):
        self.wait.until(expected_conditions.presence_of_element_located(self.username_locator)).send_keys(username)
        self.driver.find_element(*self.password_locator).send_keys(password)
        self.driver.find_element(*self.login_button_locator).click()

    def get_error(self):
        return self.wait.until(expected_conditions.presence_of_element_located(self.error_msg)).text


    def validate_username_password(self):
        username_field = self.driver.find_element(*self.username_locator).is_displayed()
        password_field = self.driver.find_element(*self.password_locator).is_displayed()
        if username_field and password_field is True:
            return True
        else:
            return False

    def validate_submit_functionality(self):
        self.driver.find_element(*self.username_locator).send_keys("vnmmagesh@gmail.com")
        self.driver.find_element(*self.password_locator).send_keys("Siddhu@oct10")
        self.driver.find_element(*self.login_button_locator).click()
        page_title = self.driver.title
        return page_title

    def is_logout_displayed(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((self.custom_button))).click()
            self.wait.until(expected_conditions.presence_of_element_located(self.user_profile_locator)).click()
            return True
        except:
            return False

    def logout(self):
        self.driver.find_element(*self.logout_button_locator).click()

