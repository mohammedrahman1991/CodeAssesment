# # tests/test_user_management.py
#
# import pytest
# import time
#
# from pages.login_page import LoginPage
# from pages.user_management_page import UserManagementPage
# from utils.api_utils import get_user_records_from_api
# from utils.db_utils import user_exists_in_db
#
# @pytest.fixture(scope="class")
# def setup_test_env(request, driver):
#     login_page = LoginPage(driver)
#     user_mgmt_page = UserManagementPage(driver)
#
#     # 1) Log in
#     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     login_page.login("Admin", "admin123")
#     time.sleep(3)
#
#     # 2) Navigate to Admin -> User Management
#     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
#     time.sleep(2)
#
#     request.cls.login_page = login_page
#     request.cls.user_mgmt_page = user_mgmt_page
#
# @pytest.mark.usefixtures("driver", "setup_test_env")
# class TestUserManagement:
#
#     def test_full_scenario(self, driver):
#         """
#         1. Add testUser1 (Admin role, Enabled)
#         2. Add testUser2 (ESS role, Disabled)
#         3. Validate via search
#         4. Reset
#         5. Delete ESS user (testUser2)
#         6. Check front-end & DB
#         7. API GET check
#         """
#
#         # ------------------------------
#         # # STEP 1: Add testUser1 (Admin, Enabled)
#         # # ------------------------------
#         # self.user_mgmt_page.click_add_button()
#         # self.user_mgmt_page.click_top_dropdown_in_form()
#         # self.user_mgmt_page.select_option_in_form("Admin")
#         # self.user_mgmt_page.click_bottom_dropdown_in_form()
#         # self.user_mgmt_page.select_option_in_form("Enabled")
#         #
#         # # Use a fixed employee name, e.g. "Orange Test"
#         # self.user_mgmt_page.fill_employee_name("Orange Test")
#         # # Use a fixed username => "testUser1"
#         # self.user_mgmt_page.fill_username("testUser1")
#         # # Use a fixed password => "Passw0rd123!"
#         # self.user_mgmt_page.fill_password("Passw0rd123!")
#         # self.user_mgmt_page.fill_confirm_password("Passw0rd123!")
#         # self.user_mgmt_page.click_save_button()
#         # time.sleep(2)
#         #
#         # # ------------------------------
#         # # STEP 2: Add testUser2 (ESS, Disabled)
#         # # ------------------------------
#         # self.user_mgmt_page.click_add_button()
#         # self.user_mgmt_page.click_top_dropdown_in_form()
#         # self.user_mgmt_page.select_option_in_form("ESS")
#         # self.user_mgmt_page.click_bottom_dropdown_in_form()
#         # self.user_mgmt_page.select_option_in_form("Disabled")
#         #
#         # self.user_mgmt_page.fill_employee_name("Orange Test")
#         # self.user_mgmt_page.fill_username("testUser2")
#         # self.user_mgmt_page.fill_password("Passw0rd123!")
#         # self.user_mgmt_page.fill_confirm_password("Passw0rd123!")
#         # self.user_mgmt_page.click_save_button()
#         # time.sleep(2)
#
#         # ------------------------------
#         # STEP 3: Validate via search
#         #    - Let's check for testUser1
#         # ------------------------------
#         self.user_mgmt_page.type_username_filter("testUser1")
#         self.user_mgmt_page.click_search_button_filter()
#         time.sleep(1)
#         assert self.user_mgmt_page.is_user_in_table1("testUser1"), "testUser1 not found after creation"
#
#         # Check testUser2 as well
#         self.user_mgmt_page.type_username_filter("testUser2")
#         self.user_mgmt_page.click_search_button_filter()
#         time.sleep(3)
#         assert self.user_mgmt_page.is_user_in_table1("testUser2"), "testUser2 not found after creation"
#
#         # ------------------------------
#         # STEP 4: Reset
#         # ------------------------------
#         # self.user_mgmt_page.click_reset_button_filter()
#         # time.sleep(1)
#         # # Confirm top filter is cleared. Could check the search field is empty:
#         # # We'll assume it's fine if no error occurs.
#         #
#         # # ------------------------------
#         # # STEP 5: Delete testUser2 (ESS)
#         # # ------------------------------
#         # self.user_mgmt_page.delete_user("testUser2")
#         # # Confirm in the UI
#         # assert not self.user_mgmt_page.is_user_in_table("testUser2"), "testUser2 still found after deletion"
#         #
#         # # ------------------------------
#         # # STEP 6: Check DB
#         # # ------------------------------
#         # still_in_db = user_exists_in_db("testUser2")
#         # assert not still_in_db, "testUser2 still found in DB after deletion"
#         #
#         # # ------------------------------
#         # STEP 7: API GET check
#         #    Suppose the endpoint returns all users in JSON
#         # ------------------------------
#         # users_from_api = get_user_records_from_api(driver)  # might fail if api.example.com isn't real
#         # # Let's see if testUser1 is present in the API
#         # api_usernames = [u.get("username") for u in users_from_api]
#         # if users_from_api:  # only check if we got data
#         #     assert "testUser1" in api_usernames, "testUser1 not found in API response"
#         #
#         # # End of scenario
#         # print("Full scenario test completed successfully.")
#         #
#
#
#     def test_validate_users_api_and_ui(self):
#         """
#         Validate that user data from the API matches the UI data.
#         """
#         # Fetch API data
#         api_data = get_user_records_from_api(self.user_mgmt_page.driver)
#
#         # Fetch UI data
#         ui_data = self.get_user_records_from_ui()
#
#         # Debugging output
#         print(f"API User Records: {api_data}")
#         print(f"UI User Records: {ui_data}")
#
#         # Validate API and UI data
#         assert self.validate_api_and_ui_data(api_data, ui_data), "API and UI data mismatch!"
