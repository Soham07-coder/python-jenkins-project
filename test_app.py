from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_welcome_page():
    # The app must be running for this test to pass
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5001")

    # Give the page a moment to load
    time.sleep(1) 

    # Find the h1 element and get its text
    heading_text = driver.find_element(By.TAG_NAME, 'h1').text

    # Assert that the text is correct
    assert "Welcome to the Test Page" in heading_text

    driver.quit()