import time

import pytest
from loginpage import LoginPage

BASE_URL = "https://www.zenclass.in/login"
VALID_USER = "vnmmagesh@gmail.com"
VALID_PASS = "Siddhu@oct10"
INVALID_USER = "cnmmagesh@gmail.com"
INVALID_PASS = "Siddhu@dec10"

def test_login_success(driver):
    driver.get(BASE_URL)
    loginpage = LoginPage(driver)
    loginpage.login(VALID_USER,VALID_PASS)
    assert loginpage.is_logout_displayed() == True, "Login Failed"
    loginpage.logout()
    assert "https://www.zenclass.in/" in driver.current_url

def test_login_unsuccess(driver):
    driver.get(BASE_URL)
    loginpage=LoginPage(driver)
    loginpage.login(INVALID_USER,INVALID_PASS)
    assert "https://www.zenclass.in/login" in driver.current_url.lower()

def test_validate_username_and_password_inputbox(driver):
    driver.get(BASE_URL)
    login = LoginPage(driver)
    result = login.validate_username_password()
    assert result is True, "Username/password not visible"

def test_submit_button(driver):
    driver.get(BASE_URL)
    login = LoginPage(driver)
    page_title = login.validate_submit_functionality()
    assert page_title == "GUVI", "login unsuccessfull"
