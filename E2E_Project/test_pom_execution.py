import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from E2E_Project.Page_Object_Module.Homepage import Homepage
from E2E_Project.Page_Object_Module.Register import Register


def test_scenario():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    homepage = Homepage()
    # homepage.Login_(pdriver=driver)
    homepage.Click_register(pdriver=driver)
    register = Register()
    register.register_user(pdriver=driver)

