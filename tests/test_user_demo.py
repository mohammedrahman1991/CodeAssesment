import pytest
import time

from conftest import driver
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage
from utils.api_utils import get_user_records_from_api
from utils.db_utils import user_exists_in_db
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def setup_test_env(request, driver):
    """
    Logs in and navigates to the User Management screen.
    """
    login_page = LoginPage(driver)
    user_mgmt_page = UserManagementPage(driver)

    # Log in
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login("Admin", "admin123")
    time.sleep(3)

    # Navigate to User Management
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    time.sleep(2)

    # Attach page objects to the class instance
    request.cls.login_page = login_page
    request.cls.user_mgmt_page = user_mgmt_page


@pytest.mark.usefixtures("driver", "setup_test_env")
class TestUserManagement:

    def test_full_scenario(self):
        """
        1. Validate via search
        2. Reset
        3. Delete testUser2
        4. Validate API and UI data
        """
        # ------------------------------
        # # STEP 1: Add testUser1 (Admin, Enabled)
        # # ------------------------------
        self.user_mgmt_page.click_add_button()
        self.user_mgmt_page.click_top_dropdown_in_form()
        self.user_mgmt_page.select_option_in_form("Admin")
        self.user_mgmt_page.click_bottom_dropdown_in_form()
        self.user_mgmt_page.select_option_in_form("Enabled")

        # Use a fixed employee name, e.g. "Orange Test"
        self.user_mgmt_page.fill_employee_name("Orange Test")
        # Use a fixed username => "testUser1"
        self.user_mgmt_page.fill_username("testUser1")
        # Use a fixed password => "Passw0rd123!"
        self.user_mgmt_page.fill_password("Passw0rd123!")
        self.user_mgmt_page.fill_confirm_password("Passw0rd123!")
        self.user_mgmt_page.click_save_button()
        time.sleep(2)

        # ------------------------------
        # STEP 2: Add testUser2 (ESS, Disabled)
        # ------------------------------
        self.user_mgmt_page.click_add_button()
        self.user_mgmt_page.click_top_dropdown_in_form()
        self.user_mgmt_page.select_option_in_form("ESS")
        self.user_mgmt_page.click_bottom_dropdown_in_form()
        self.user_mgmt_page.select_option_in_form("Disabled")

        self.user_mgmt_page.fill_employee_name("Orange Test")
        self.user_mgmt_page.fill_username("testUser2")
        self.user_mgmt_page.fill_password("Passw0rd123!")
        self.user_mgmt_page.fill_confirm_password("Passw0rd123!")
        self.user_mgmt_page.click_save_button()
        time.sleep(2)

        # Validate via search
        self.user_mgmt_page.type_username_filter("testUser1")
        self.user_mgmt_page.click_search_button_filter()
        time.sleep(1)
        assert self.user_mgmt_page.is_user_in_table1("testUser1"), "testUser1 not found after creation"

        # Check testUser2 as well
        self.user_mgmt_page.type_username_filter("testUser2")
        self.user_mgmt_page.click_search_button_filter()
        time.sleep(3)
        assert self.user_mgmt_page.is_user_in_table1("testUser2"), "testUser2 not found after creation"

        # Delete testUser2
        self.user_mgmt_page.delete_user("testUser2")
        assert not self.user_mgmt_page.is_user_in_table("testUser2"), "testUser2 still found after deletion"


    def test_validate_users_api_and_ui(self):
        """
        Validate that user data from the API matches the UI data.
        """
        # Fetch API data
        api_data = get_user_records_from_api(self.user_mgmt_page.driver)

        # Fetch UI data
        ui_data = self.get_user_records_from_ui()

        # # Debugging output
        # print(f"API User Records: {api_data}")
        # print(f"UI User Records: {ui_data}")
        #
        # # Validate API and UI data
        assert self.validate_api_and_ui_data(api_data, ui_data), "API and UI data mismatch!"

    def get_user_records_from_ui(self):
        """
        Extract user records displayed on the User Management screen.
        """
        wait = WebDriverWait(self.user_mgmt_page.driver, 10)
        table_body = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-table-body")))
        rows = table_body.find_elements(By.XPATH, "./div[@role='row']")

        user_records = []
        for row in rows:
            columns = row.find_elements(By.XPATH, ".//div[@role='cell']")
            user_data = {
                "username": columns[1].text.strip(),
                "role": columns[2].text.strip(),
                "status": columns[3].text.strip()
            }
            user_records.append(user_data)

        # Debugging print statement
        print(f"Extracted UI User Records: {user_records}")
        return user_records

    def validate_api_and_ui_data(self, api_data, ui_data):
        """
        Compares user records from API and UI to ensure they match.
        """
        api_usernames = {user["username"] for user in api_data}
        ui_usernames = {user["username"] for user in ui_data}

        # Identify mismatches
        missing_in_api = ui_usernames - api_usernames
        missing_in_ui = api_usernames - ui_usernames

        # Debugging logs
        print(f"Users missing in API: {missing_in_api}")
        print(f"Users missing in UI: {missing_in_ui}")

        return not missing_in_api and not missing_in_ui
