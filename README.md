# OrangeHRM Test Automation

This project automates a series of tests for the OrangeHRM user management workflow using **Selenium + Pytest**.

## 1. Features Tested

1. **Login** with username="Admin" and password="admin123".
2. **Add**:
   - `testUser1` (Admin, Enabled)
   - `testUser2` (ESS, Disabled)
3. **Search** & verify that both users are added.
4. **Reset** the search and check if the field is cleared.
5. **Delete** `testUser2` and validate:
   - Removed from front-end.
   - Removed from the **DB** (sample SQL check).
6. **API GET** request assumption: We call an endpoint that returns a list of user objects. We verify `testUser1` is in that response.

## 2. Setup & Prerequisites

- **Python 3.8+**
- **Chrome** browser & **ChromeDriver** in your PATH (or update `conftest.py` as needed).
- (Optional) A local or remote **MySQL** DB with `users` table for the SQL check.
- (Optional) A mock or real **API endpoint** returning user data.

## 3. Installation

1. **Clone** this repository:
   ```bash
   git clone https://github.com/<your-username>/orangehrm-test-automation.git
   cd orangehrm-test-automation
