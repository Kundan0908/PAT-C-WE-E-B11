import pytest
from selenium import webdriver
import logging

# Test fixture
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def pytest_configure():
    logger = logging.getLogger() # Debug,Info,Warning,Error,Critical,Fatal
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


    file_handler = logging.FileHandler("test_logs.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
