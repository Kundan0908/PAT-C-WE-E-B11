import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestClass():
    def test_register(self):
        print("I am register function")
        try:
            # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
            self.driver.find_element(By.XPATH, '//a[text()="Register"]').click()
            self.driver.find_element(By.NAME, 'customer.firstName').send_keys('testuser')
            self.driver.find_element(By.NAME, 'customer.lastName').send_keys('testuser')
            self.driver.find_element(By.NAME, 'customer.address.street').send_keys('430,street road')
            self.driver.find_element(By.NAME, 'customer.address.city').send_keys('Bangalore')
            self.driver.find_element(By.NAME, 'customer.address.state').send_keys('karnataka')
            self.driver.find_element(By.NAME, 'customer.address.zipCode').send_keys('1234238')
            self.driver.find_element(By.NAME, 'customer.ssn').send_keys('1234238')
            self.driver.find_element(By.NAME, 'customer.username').send_keys('testuser123')
            self.driver.find_element(By.NAME, 'customer.password').send_keys('testuser')
            self.driver.find_element(By.NAME, 'repeatedPassword').send_keys('testuser')
            self.driver.find_element(By.XPATH, '//input[@value="Register"]').click()
            actual_output = self.driver.find_element(By.XPATH, "//*[@id='rightPanel']//child::p").text
            expected_output = 'Your account was created successfully. You are now logged in.'
            self.driver.save_screenshot('image.png')
            assert expected_output == actual_output, "Account not created due to some problem"

        except:
            raise Exception

    # def test_login(self):
    #     print("I am login function")
    #
    # def test_check_balance(self):
    #     print("I am a function for checking account balance")
    #
    # def test_transfer_fund(self):
    #     print("I am a function for transferring fund to another account")