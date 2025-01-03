import requests
def get_user_records_from_api(driver):
    """
    Fetch user records from the OrangeHRM API using the current session's cookies.
    """
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users?limit=50&offset=0&sortField=u.userName&sortOrder=ASC"
    headers = {"Content-Type": "application/json"}

    # Extract cookies from Selenium driver for authentication
    cookies = driver.get_cookies()
    session_cookie = {cookie['name']: cookie['value'] for cookie in cookies}

    # Make the API request
    response = requests.get(url, headers=headers, cookies=session_cookie)
    response.raise_for_status()

    # Parse the API response and extract relevant fields
    api_data = response.json()["data"]
    user_records = []

    for user in api_data:
        user_data = {
            "username": user["userName"],
            "role": user["userRole"]["name"],  # Extract the user role
            "status": "Enabled" if user["status"] else "Disabled"  # Convert boolean to string
        }
        user_records.append(user_data)

        # Print each user record to confirm extraction, focusing on "testUser1"
        if user_data["username"] == "testUser1":
            print(f"Found testUser1 in API response: {user_data}")

    return user_records


def test_validate_users_api_and_ui(self):
    """
    Fetch user records from the API and UI, then validate that they match.
    """
    # Step 1: Fetch user records from the API
    api_data = get_user_records_from_api(self.user_mgmt_page.driver)

    # Step 2: Fetch user records from the UI
    ui_data = self.get_user_records_from_ui()

    # Step 3: Validate API and UI data
    assert self.validate_api_and_ui_data(api_data, ui_data), "API and UI data mismatch!"


