# Clinic roductivity Mini Flask App

## Setup Instructions

1. **Clone or unzip the project:**
    ```
    git clone https://github.com/amhendrix/clinic_app.git
    cd clinic_app
    ```
    *or unzip the project folder and cd into it.*

2. **(Recommended) Use a virtual environment:**
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```
    *(Or simply run `./setup.sh` if using the provided script.)*

4. **Run the app:**
    ```
    python3 app.py
    ```
    - The app auto-creates `clinic.db` with the required table.

5. **Visit:** [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## Folder Structure

clinic_app/
├── app.py
├── requirements.txt
├── setup.sh
├── templates/
│ ├── form.html
│ └── confirmation.html
├── static/
│ └── custom.css
├── README.md
├── .gitignore


---

## Questions & Answers

### 1. **How does your app handle form validation?**
- All fields are required and validated on the server.
- Date of Birth must be in the past.
- If validation fails, the user is shown error messages above the form and the form is re-rendered with their previous input preserved.
- If all inputs are valid, data is saved to SQLite and a confirmation page is shown.

---

### 2. **How would you extend the app to support therapist logins?**
- **Database:** Add a `therapists` table with hashed passwords.
- **Auth:** Use Flask’s session management and add login/logout routes.
- **Blueprints:** Refactor into modules (`auth.py`, `routes.py`) for scalability.
- **Decorators:** Protect routes with `@login_required`.
- **Optional:** Use Flask-Login or similar for robust authentication management.
- **User Experience:** Each therapist can only see/add patients associated with their account.

---

### 3. **How would you deploy this app to a HIPAA-compliant cloud environment?**
- Use a HIPAA-compliant cloud provider (AWS, Azure, GCP with BAA signed).
- Serve only via HTTPS (TLS certificates).
- Store environment variables and secrets securely (AWS Secrets Manager, etc.).
- Use managed, encrypted databases (e.g., AWS RDS with encryption at rest).
- No PHI in logs. Ensure logging is audit-friendly but never logs patient data.
- Limit access via security groups/firewalls and use role-based IAM.
- Backup policies and disaster recovery plans in place.
- Routine security reviews and vulnerability scanning.

---

### 4. **Where would you place the code that initializes the database and why?**
- In `init_db()` function, called **before** the app starts in the `__main__` block **inside an application context**:
    ```python
    if __name__ == "__main__":
        with app.app_context():
            init_db()
        app.run(debug=True)
    ```
- This ensures tables are always created before any web request is processed, avoids race conditions, and keeps setup logic clear and centralized.

---

## Security Notes

- All inputs are validated and sanitized.
- No PHI is logged.
- SQLite database is stored locally for demo purposes only—use managed databases for production.

---

## Commit messages (suggested history)

- `Initial project structure and documentation`
- `Add Flask app and SQLite database initialization`
- `Implement patient intake form and confirmation template`
- `Add form submission, validation, and error handling`
- `Finalize documentation and answer add-on questions`
- `Add requirements.txt and setup.sh`

---
Future Feature Idea
Modality- and Insurance-Specific Note Templates
Idea:
Enhance the app by allowing therapists to select from modality-specific note templates (e.g., for OT, PT, Speech, ABA, feeding therapy, etc.), either by plugging in a modality or choosing from a dropdown. Instead of a generic SOAP note, therapists would receive a pre-filled template tailored to the treatment modality.

Benefits:

Saves time: Therapists start documentation with context-appropriate prompts, reducing repetitive entry.

Custom for insurance: Selecting an insurance plan could load a template that prompts for all required reimbursement information, reducing claim denials.

Maintains individuality: Templates would support customization, ensuring each note remains individualized for the patient.

Supports compliance: By structuring notes for both modality and payer, documentation quality and audit-readiness are improved.

Example Workflow:

Therapist selects the patient and session type.

Chooses the modality (from dropdown or search).

(Optional) Chooses the insurance provider.

The app generates a note template containing:

Modality-specific goals/fields (not just SOAP)

Payer-required sections

Prompts for therapist to individualize details

Long-term vision:
This could extend to analytics, billing checks, and compliance dashboards, as documentation patterns could be tracked for quality improvement.


