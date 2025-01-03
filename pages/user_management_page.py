# pages/user_management_page.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class UserManagementPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # 1) Clicking the green Add button
    def click_add_button(self):
        add_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']"))
        )
        add_btn.click()

    # 2) Selecting user role & status from Add User form
    def click_top_dropdown_in_form(self):
        """
        For the Add User form, user role dropdown:
        (//div[@class='oxd-select-text--after'])[1]
        """
        role_dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='oxd-select-text--after'])[1]"))
        )
        role_dropdown.click()

    def click_bottom_dropdown_in_form(self):
        """
        For the Add User form, status dropdown:
        (//div[@class='oxd-select-text--after'])[2]
        """
        status_dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='oxd-select-text--after'])[2]"))
        )
        status_dropdown.click()

    def select_option_in_form(self, option_text):
        """
        After opening a dropdown in the form, pick the visible text (Admin, ESS, Enabled, Disabled, etc.)
        """
        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='listbox']//span[normalize-space()='{option_text}']"))
        )
        option.click()

    def fill_employee_name(self, text):
        emp_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Employee Name']/following::input[1]"))
        )
        emp_field.clear()
        emp_field.send_keys(text)
        time.sleep(2)
        emp_field.send_keys(Keys.ARROW_DOWN)
        emp_field.send_keys(Keys.ENTER)
        time.sleep(1)

    def fill_username(self, username):
        user_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Username']/following::input[1]"))
        )
        user_field.clear()
        user_field.send_keys(username)

    def fill_password(self, password):
        pass_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Password']/following::input[1]"))
        )
        pass_field.clear()
        pass_field.send_keys(password)

    def fill_confirm_password(self, password):
        conf_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Confirm Password']/following::input[1]"))
        )
        conf_field.clear()
        conf_field.send_keys(password)

    def click_save_button(self):
        save_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))
        )
        save_btn.click()
        time.sleep(2)

    # 3) Searching in the top filter area
    def type_username_filter(self, username):
        """
        Clears the username filter field and types the given username.
        """
        username_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]"))
        )

        # Click the field to focus
        username_field.click()

        # Clear using JavaScript in case .clear() doesn't work
        self.driver.execute_script("arguments[0].value = '';", username_field)

        # Ensure any residual text is cleared with Keys
        username_field.send_keys(Keys.CONTROL + 'a')  # Select all text
        username_field.send_keys(Keys.DELETE)  # Delete selected text

        # Finally, type the new username
        username_field.send_keys(username)

    def clear_field(self):

        field_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]"))
        )
        field_element.click()
        """
        Clears the input field using keyboard shortcuts.
        """
        field_element.send_keys(Keys.CONTROL + 'a')  # Select all text
        field_element.send_keys(Keys.DELETE)  # Delete selected text

    def click_search_button_filter(self):
        search_btn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']")
        search_btn.click()

    def click_reset_button_filter(self):
        reset_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Reset']"))
        )
        reset_btn.click()

    # 3b) Searching by user role or status in the filter area
    def click_role_dropdown_filter(self):
        """
        The locator you gave for user role in the filter area:
        //div[@class='oxd-table-filter-area']//div[2]//div[1]//div[2]//div[1]//div[1]//div[2]//i[1]
        """
        dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='oxd-table-filter-area']//div[2]//div[1]//div[2]//div[1]//div[1]//div[2]//i[1]"))
        )
        dropdown.click()

    def click_status_dropdown_filter(self):
        """
        The locator for status in the filter area:
        //div[4]//div[1]//div[2]//div[1]//div[1]//div[2]//i[1]
        """
        dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[4]//div[1]//div[2]//div[1]//div[1]//div[2]//i[1]"))
        )
        dropdown.click()

    def pick_filter_option(self, text):
        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='listbox']//span[normalize-space()='{text}']"))
        )
        option.click()

    # 4) Deleting a user
    def delete_user(self, username):
        """
        We'll do a quick search by username, then click the delete icon.
        """
        self.type_username_filter(username)
        self.click_search_button_filter()
        time.sleep(2)

        # Click the trash icon
        delete_icon = self.driver.find_element(
            By.XPATH,
            f"//div[@class='oxd-table-body']//div[contains(text(),'{username}')]/ancestor::div[@role='row']//button[@title='Delete']"
        )
        delete_icon.click()

        confirm_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes, Delete']"))
        )
        confirm_btn.click()
        time.sleep(2)

    # Checking if user is in the table
    def is_user_in_table(self, username):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-table-body")))
        rows = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']/div[@role='row']")
        for row in rows:
            if username in row.text:
                return True
        return False

    def is_user_in_table1(self, username):
        """
        Validates if a user with the specified username exists in the table.
        Uses XPath: //*[text()='username']
        """
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-table-body")))
        try:
            # Search for the exact username text in the table
            user_element = self.driver.find_element(By.XPATH, f"//*[text()='{username}']")
            return user_element.is_displayed()  # Return True if the element is visible
        except Exception:
            return False  # Return False if the element is not found



