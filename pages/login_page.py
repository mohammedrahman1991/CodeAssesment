from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self, url):
        self.driver.get(url)

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)

        # Username
        username_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        username_input.send_keys(username)

        # Password
        password_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys(password)

        # Login button
        login_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_button.click()
