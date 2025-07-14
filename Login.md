
# Flask Login Page Design and Implementation

This document outlines the design and implementation steps for the Flask login page, which supports both email and LDAP authentication.

## Design

### Frontend

- **Framework:** Bootstrap 5.3.0 is used for styling to create a modern and responsive user interface.
- **Pages:**
    - **Login Page (`login.html`):** A simple and clean login form that allows users to enter their credentials and choose between email and LDAP authentication.
    - **Main Page (`main.html`):** A protected page displayed after successful login. It features a top title bar, a left-hand navigation menu, and a main content area.
    - **Base Template (`base.html`):** A base template that provides a consistent layout for the application. It includes the header, sidebar navigation, and main content block.

### Backend

- **Framework:** Flask is used as the web framework.
- **Authentication:**
    - **Email Authentication:** User credentials are stored in a SQLite3 database (`users.db`). The application queries this database to validate user logins.
    - **LDAP Authentication:** The `ldap3` library is used to authenticate users against an LDAP server. The server address is configurable in `app.py`.
- **Session Management:** Flask-Login is used to manage user sessions, including logging users in, logging them out, and protecting routes.

## Implementation Steps

1. **Project Setup:**
   - Created a new directory for the project: `flask_ldap_login_app`.
   - Installed the required Python packages: `Flask`, `ldap3`, and `Flask-Login`.

2. **Initial Application:**
   - Created the main application file, `app.py`, with a basic Flask app structure.
   - Implemented the login logic for both email and LDAP authentication.
   - Created a simple login page using HTML.

3. **Frontend Enhancement:**
   - Modified the login page to use Bootstrap for a more modern look and feel.
   - Created a new `dashboard.html` template for authenticated users.

4. **Database Integration:**
   - Created a `setup_database.py` script to create a SQLite3 database (`users.db`) and populate it with a test user.
   - Modified `app.py` to use the SQLite database for email authentication instead of an in-memory dictionary.

5. **Main Page Creation:**
   - Created a `base.html` template with a top title bar, left navigation, and main content area.
   - Created a `main.html` template that extends `base.html` to display the main page content.
   - Updated `app.py` to render the new `main.html` page after login.

6. **Styling and Refinements:**
   - Adjusted the font size of the title in the header.
   - Removed the redundant title from the main content area.
   - Matched the font size of the main content text to the "Menu" title for consistency.
