import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def setup(request):
    print("I am a function for opening browser")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = driver
    yield
    print("I am a function for closing browser")
    driver.quit()