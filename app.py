""""
app.py
Clinic Productivity Mini Flask App

A minimal, production-quality Flask app for patient intake.
"""
import os
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, g, flash

# Configuration
DATABASE = "clinic.db"
SECRET_KEY = "replace-this-with-a-secure-random-string"

app = Flask(__name__)
app.config['DATABASE'] = DATABASE
app.config['SECRET_KEY'] = SECRET_KEY

# --- Database Helpers ---

def get_db():
    """
    Opens a new database connection per request.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    """
    Closes the database again at the end of the request.
    """
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """
    Creates the patients table if it does not exist.
    """
    db = get_db()
    db.execute(
        """CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            dob DATE NOT NULL,
            therapist_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
    )
    db.commit()

@app.before_first_request
def initialize():
    """
    Ensures the database and patients table exist before first use.
    """
    init_db()

# --- Routes ---

@app.route("/", methods=["GET"])
def index():
    """
    Display patient intake form.
    """
    return render_template("form.html", errors=[], data={})

@app.route("/submit", methods=["POST"])
def submit():
    """
    Handle form submission, validate input, and store patient in the database.
    """
    errors = []
    # Extract data from form
    first_name = request.form.get("first_name", "").strip()
    last_name = request.form.get("last_name", "").strip()
    dob_str = request.form.get("dob", "").strip()
    therapist_name = request.form.get("therapist_name", "").strip()

    # Store previous input for user feedback
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "dob": dob_str,
        "therapist_name": therapist_name,
    }

    # --- Validation ---
    if not first_name:
        errors.append("Patient First Name is required.")
    if not last_name:
        errors.append("Patient Last Name is required.")
    if not dob_str:
        errors.append("Date of Birth is required.")
    else:
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
            if dob >= datetime.today().date():
                errors.append("Date of Birth must be in the past.")
        except ValueError:
            errors.append("Date of Birth must be a valid date (YYYY-MM-DD).")
    if not therapist_name:
        errors.append("Therapist Name is required.")

    # If errors, redisplay the form
    if errors:
        return render_template("form.html", errors=errors, data=data), 400

    # Store in DB
    db = get_db()
    db.execute(
        "INSERT INTO patients (first_name, last_name, dob, therapist_name) VALUES (?, ?, ?, ?)",
        (first_name, last_name, dob_str, therapist_name)
    )
    db.commit()

    # Render confirmation
    return render_template("confirmation.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
""
app.p
Clinic Productivity Mini Flask App

A minimal, production-quality Flask app for patient intake.
"""
import os
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, g, flash

# Configuration
DATABASE = "clinic.db"
SECRET_KEY = "replace-this-with-a-secure-random-string"

app = Flask(__name__)
app.config['DATABASE'] = DATABASE
app.config['SECRET_KEY'] = SECRET_KEY

# --- Database Helpers ---

def get_db():
    """
    Opens a new database connection per request.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    """
    Closes the database again at the end of the request.
    """
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """
    Creates the patients table if it does not exist.
    """
    db = get_db()
    db.execute(
        """CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            dob DATE NOT NULL,
            therapist_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
    )
    db.commit()

@app.before_first_request
def initialize():
    """
    Ensures the database and patients table exist before first use.
    """
    init_db()

# --- Routes ---

@app.route("/", methods=["GET"])
def index():
    """
    Display patient intake form.
    """
    return render_template("form.html", errors=[], data={})

@app.route("/submit", methods=["POST"])
def submit():
    """
    Handle form submission, validate input, and store patient in the database.
    """
    errors = []
    # Extract data from form
    first_name = request.form.get("first_name", "").strip()
    last_name = request.form.get("last_name", "").strip()
    dob_str = request.form.get("dob", "").strip()
    therapist_name = request.form.get("therapist_name", "").strip()

    # Store previous input for user feedback
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "dob": dob_str,
        "therapist_name": therapist_name,
    }

    # --- Validation ---
    if not first_name:
        errors.append("Patient First Name is required.")
    if not last_name:
        errors.append("Patient Last Name is required.")
    if not dob_str:
        errors.append("Date of Birth is required.")
    else:
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
            if dob >= datetime.today().date():
                errors.append("Date of Birth must be in the past.")
        except ValueError:
            errors.append("Date of Birth must be a valid date (YYYY-MM-DD).")
    if not therapist_name:
        errors.append("Therapist Name is required.")

    # If errors, redisplay the form
    if errors:
        return render_template("form.html", errors=errors, data=data), 400

    # Store in DB
    db = get_db()
    db.execute(
        "INSERT INTO patients (first_name, last_name, dob, therapist_name) VALUES (?, ?, ?, ?)",
        (first_name, last_name, dob_str, therapist_name)
    )
    db.commit()

    # Render confirmation
    return render_template("confirmation.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)

