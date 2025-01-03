# import pytest
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from utils.api_utils import get_user_records_from_api
#
#
# @pytest.mark.usefixtures("driver", "setup_test_env")
# class TestUserManagement:
#
#     def test_validate_users_api_and_ui(self):
#         """
#         1. Fetch user records from the API.
#         2. Fetch user records from the UI.
#         3. Validate that the API and UI data match.
#         """
#         # Step 1: Fetch user records from the API
#         api_data = get_user_records_from_api(self.user_mgmt_page.driver)
#
#         # Step 2: Fetch user records from the UI
#         ui_data = self.get_user_records_from_ui()
#
#         # Step 3: Validate API and UI data match
#         assert self.validate_api_and_ui_data(api_data, ui_data), "API and UI data mismatch!"
#
#     def get_user_records_from_ui(self):
#         """
#         Extract user records displayed on the User Management screen.
#         """
#         wait = WebDriverWait(self.user_mgmt_page.driver, 10)
#         table_body = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-table-body")))
#         rows = table_body.find_elements(By.XPATH, "./div[@role='row']")
#
#         user_records = []
#         for row in rows:
#             columns = row.find_elements(By.XPATH, ".//div[@role='cell']")
#             user_data = {
#                 "username": columns[1].text.strip(),  # Update based on column order
#                 "role": columns[2].text.strip(),
#                 "status": columns[3].text.strip()
#             }
#             user_records.append(user_data)
#         return user_records
#
#     def validate_api_and_ui_data(self, api_data, ui_data):
#         """
#         Compares user records from API and UI to ensure they match.
#         """
#         # Convert API and UI data to sets of usernames for easier comparison
#         api_usernames = {user["username"] for user in api_data}
#         ui_usernames = {user["username"] for user in ui_data}
#
#         # Identify mismatches
#         missing_in_api = ui_usernames - api_usernames
#         missing_in_ui = api_usernames - ui_usernames
#
#         # Log any mismatches
#         if not missing_in_api and not missing_in_ui:
#             print("Validation successful: API and UI data match!")
#             return True
#         else:
#             print(f"Users missing in API: {missing_in_api}")
#             print(f"Users missing in UI: {missing_in_ui}")
#             return False
