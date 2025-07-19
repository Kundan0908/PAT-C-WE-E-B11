
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

import time

# Setup WebDriver (Make sure to set the path to your WebDriver)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open the target website
    driver.implicitly_wait(10)
    driver.get("https://demoqa.com/automation-practice-form")

    # Maximize browser window
    driver.maximize_window()

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstName")))

    # Fill out the form:

    # First Name
    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("John")

    # Last Name
    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("Doe")

    # Email
    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("johndoe@example.com")

    # Gender (e.g., Select Male)
    gender_male = driver.find_element(By.XPATH, "//label[contains(text(),'Male')]")
    gender_male.click()

    # Mobile Number
    mobile = driver.find_element(By.ID, "userNumber")
    mobile.send_keys("1234567890")

    time.sleep(10)
    # Date of Birth (Select 15th August 2000 as an example)
    dob = driver.find_element(By.ID, "dateOfBirthInput")
    dob.click()

    # Select the month (e.g., August)
    month_dropdown = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
    month_dropdown.click()
    month_dropdown.send_keys("August")  # Use the full month name

    # Select the year (e.g., 2000)
    year_dropdown = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
    year_dropdown.click()
    year_dropdown.send_keys("2000")  # Type out the specific year

    # Select the day of the month (e.g., 15th)
    date = driver.find_element(By.XPATH, "(//div[contains(@class,'react-datepicker__day react-datepicker__day')])[19]")
    date.click()
    time.sleep(5)

    # Subjects (e.g., Type and select 'Maths')
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("Maths")
    time.sleep(5)
    subjects.send_keys(Keys.ENTER)

    # Hobbies (e.g., Select Sports)
    hobby_sports = driver.find_element(By.XPATH, "//label[contains(text(),'Sports')]")
    hobby_sports.click()
    time.sleep(5)

    # Upload Picture
    picture_upload = driver.find_element(By.ID, "uploadPicture")
    picture_upload.send_keys("C:/users/kundan_kumar/Downloads/code_v2025-02-23/s3/beach.jpg")

    # Current Address
    current_address = driver.find_element(By.ID, "currentAddress")
    current_address.send_keys("123 Main Street, New York, NY")

    # State and City (select Haryana and Karnal)
    state_dropdown = driver.find_element(By.ID, "react-select-3-input")
    state_dropdown.send_keys("Haryana")
    state_dropdown.send_keys(Keys.RETURN)

    city_dropdown = driver.find_element(By.ID, "react-select-4-input")
    city_dropdown.send_keys("Karnal")
    city_dropdown.send_keys(Keys.RETURN)

    time.sleep(5)
    # Submit the form
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # Wait for the submission response
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()