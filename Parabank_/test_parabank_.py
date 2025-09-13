import pytest
from Parabank_.pom.homepage import Homepage
from Parabank_.pom.register_page import Register
from Parabank_.read_data_from_excel import read_data
import time
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
link_title = config['ParabankURL']
link = link_title.get('url')

@pytest.mark.parametrize('firstname,lastname,address,city,state,phnumber,ssn,username,password,rptpwd',read_data())
def test_register_new_user(firstname,lastname,address,city,state,phnumber,ssn,username,password,rptpwd,driver):
    # Opening Chrome Browser
    # Opening Parabank webpage
    driver.get(link)
    driver.maximize_window()

    # Clicking for new registeration
    homePage = Homepage(pdriver=driver)
    homePage.register_new_user()

    # Register new users
    registerPage = Register(pdriver=driver)
    registerPage.fill_userdetails(firstname,lastname,address,city,state,phnumber,ssn,username,password,rptpwd)