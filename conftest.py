import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # If you want to run headless, uncomment:
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
