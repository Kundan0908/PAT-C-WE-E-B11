from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Page Object Model for Login Page
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()

    def is_login_successful(self):
        try:
            # Check for successful login element (inventory container)
            self.wait.until(
                EC.presence_of_element_located((By.ID, "inventory_container"))
            )
            return True
        except:
            return False

    def is_login_failed(self):
        try:
            # Check for error message on failed login
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
            )
            return True
        except:
            return False

