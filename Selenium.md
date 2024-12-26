# QA Selenium Test for Table Search Demo

This project contains a test script (`qa_selenium_test.py`) that automates the following steps using Python's Selenium:

- Navigates to the Selenium Playground Table Search Demo.
- Locates and interacts with the search box to search for "New York".
- Validates that the search results show exactly 5 entries out of 24 total entries.

## Requirements

To run this test, you need to have the following installed:

1. ChromeDriver (or any other WebDriver for your browser)
   - [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
   - Ensure the `chromedriver` is in your system's PATH or specify its location in the `qa_selenium_test.py` script.
2. Install required Python packages:
   ```bash
   pip install selenium pytest
