# QA Selenium Automation with Python

## Objective
Create a Selenium automation script in Python to validate search functionality on the **Selenium Playground** website.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture(scope="module")
def driver():
    # Initialize the WebDriver (using Chrome here)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Test case to perform search for "New York"
def test_table_search(driver):
    driver.get("https://www.selenium.dev/selenium-playground/table-search-demo")
    search_box = driver.find_element(By.ID, "example_filter")
    search_box.clear()  # Clear any existing text in the search box
    search_box.send_keys("New York")
    time.sleep(2)

    # Validate the 5 entries are shown after performing search
    table_rows = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr")
    assert len(table_rows) == 5, f"Expected 5 rows, but found {len(table_rows)} rows."

    # Validates that there are 24 entries in total (before search)
    total_entries = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr")
    assert len(total_entries) == 24, f"Expected 24 entries, but found {len(total_entries)} entries."
