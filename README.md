# Clinic Productivity Mini Flask App

A simple, production-quality Flask app for patient intake, using SQLite and Jinja2 templates.

## Setup & Run

1. **Clone the repository:**
    ```
    git clone <your-repo-url>
    cd clinic_app
    ```

2. **Install dependencies:**
    ```
    pip install flask
    ```

3. **Run the app:**
    ```
    python app.py
    ```
    - The app auto-creates `clinic.db` with the required table.
    - Visit `http://127.0.0.1:5000/` in your browser.

---

## Folder Structure


---

## Add-On Questions

### 1. How does your app handle form validation?
- **Server-side validation:** All fields are required. Date of Birth must be in the past.
- If validation fails, errors are displayed above the form, and the user’s input is preserved.
- **If a required field is missing or DOB is in the future:** The form is re-rendered with appropriate error messages and a `400 Bad Request` status code.

---

### 2. How would you extend the app to support therapist logins?
- **Add User Authentication:**
    - Create a `therapists` table for users with hashed passwords (e.g., using Werkzeug’s `generate_password_hash`).
    - Add login/logout routes and use Flask’s session management.
    - Protect patient intake and admin routes with `@login_required` decorators.
- **Folder Structure Changes:**
    - Modularize the app (e.g., with `auth.py`, `models.py`) for scalability.
    - Add registration, password reset, and session management.
- **Example commit:**  
    `Implement therapist authentication and session handling`

---

### 3. How would you deploy this app to a HIPAA-compliant cloud environment?
- **Key steps:**
    - Use a HIPAA-compliant provider (e.g., AWS with BAA).
    - Serve the app via HTTPS with managed SSL.
    - Use managed database (e.g., RDS, encrypted at rest).
    - Store secrets using environment variables or a secrets manager.
    - Log access and errors, but never PHI.
    - Enable daily automated backups and role-based access control.
    - Review and sign a BAA with the provider.
    - Consider deploying with Docker, behind a secure WSGI server (gunicorn/uwsgi) and reverse proxy (nginx).
    - Enforce least-privilege access, vulnerability scans, and regular audits.

---

### 4. Where would you place the code that initializes the database and why?
- The code that creates the table (if not present) is in `init_db()`, called via `@before_first_request`.
- **Why:** Ensures the database and required table are ready before any user interaction, avoids redundant checks per request, and keeps initialization logic out of route handlers for clarity and maintainability.

---

## Example Git Commit Messages

- `Initial project structure and documentation`
- `Add Flask app and SQLite database initialization`
- `Implement patient intake form route and template`
- `Add form submission route, validation, and error handling`
- `Add confirmation template`
- `Finalize documentation and clean up code`

---

**Thank you for reviewing!**

---

## Security Notes

- All inputs are sanitized and validated.
- No PHI is logged.
- Do not use in production without further security review and environment-specific configuration.

---

