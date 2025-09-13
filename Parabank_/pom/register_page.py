from selenium.webdriver.common.by import By
class Register():

    def __init__(self,pdriver):
        self.driver = pdriver
        self._first_name = (By.NAME, 'customer.firstName')
        self._last_name = (By.NAME, 'customer.lastName')
        self._address = (By.NAME, 'customer.address.street')
        self._street_city = (By.NAME, 'customer.address.city')
        self._state = (By.NAME, 'customer.address.state')
        self._zipcode = (By.NAME, 'customer.address.zipCode')
        self._ssn = (By.NAME, 'customer.ssn')
        self._username = (By.NAME, 'customer.username')
        self._password = (By.NAME, 'customer.password')
        self._repeat_password = (By.NAME, 'repeatedPassword')
        self._confirm_registeration = (By.XPATH, '//input[@value="Register"]')

    def fill_userdetails(self,firstname,lastname,address,city,state,phnumber,ssn,username,password,rptpwd):
        self.driver.find_element(*self._first_name).send_keys(firstname)
        self.driver.find_element(*self._last_name).send_keys(lastname)
        self.driver.find_element(*self._address).send_keys(address)
        self.driver.find_element(*self._street_city).send_keys(city)
        self.driver.find_element(*self._state).send_keys(state)
        self.driver.find_element(*self._zipcode).send_keys(phnumber)
        self.driver.find_element(*self.ssn).send_keys(ssn)
        self.driver.find_element(*self._username).send_keys(username)
        self.driver.find_element(*self._password).send_keys(password)
        self.driver.find_element(*self._repeat_password).send_keys(rptpwd)

    def click_register_btn(self):
        self.driver.find_element(*self._confirm_registeration).click()
