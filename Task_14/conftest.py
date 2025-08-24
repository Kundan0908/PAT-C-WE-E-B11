import pytest
from selenium import webdriver

# Test fixture
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()