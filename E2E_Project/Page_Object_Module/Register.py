from selenium.webdriver.common.by import By

class Register():
    def __init__(self):
        self.first_name = (By.NAME,'customer.firstName')
        self.last_name = (By.NAME, 'customer.lastName')
        self.address = (By.NAME, 'customer.address.street')
        self.city = (By.NAME, 'customer.address.city')
        self.state = (By.NAME, 'customer.address.state')
        self.zipcode = (By.NAME, 'customer.address.zipCode')
        self.ssn = (By.NAME, 'customer.ssn')
        self.cust_username =(By.NAME, 'customer.username')
        self.cust_password = (By.NAME, 'customer.password')
        self.confirm_password = (By.NAME, 'repeatedPassword')
        self.click_register = (By.XPATH,'//input[@value="Register"]')

    def register_user(self,pdriver):
        pdriver.find_element(*self.first_name).send_keys('testuser')
        pdriver.find_element(*self.last_name).send_keys('testuser')
        pdriver.find_element(*self.address).send_keys('430,street road')
        pdriver.find_element(*self.city).send_keys('Bangalore')
        pdriver.find_element(*self.state).send_keys('karnataka')
        pdriver.find_element(*self.zipcode).send_keys('1234238')
        pdriver.find_element(*self.ssn).send_keys('1234238')
        pdriver.find_element(*self.cust_username).send_keys('testuser123')
        pdriver.find_element(*self.cust_password).send_keys('testuser')
        pdriver.find_element(*self.confirm_password).send_keys('testuser')
        pdriver.find_element(*self.click_register).click()