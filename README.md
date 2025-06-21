# Clinic App (FastAPI)

This project is a small demo application that uses **FastAPI** with a SQLite database.
It contains a simple user login/registration flow and an admin panel for viewing
information about appointments, analyses and surveys.

## Requirements

* Python 3.9+
* Packages listed in `requirements.txt`

## Setup

1. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Initialize the database (creates `clinic.db` and fills it with sample data):

   ```bash
   python "DB manipulations/TableCreate.py"
   python "DB manipulations/DataAdd.py"
   ```

3. Start the development server:

   ```bash
   uvicorn app:app --reload
   ```

   The application will be available at <http://127.0.0.1:8000>.

## Usage

* Visit `/register` to create a new account.
* Log in via `/login`.
* After logging in you will be redirected to `/profile` where information from
  the database is shown.
* The admin interface is available at `/admin-login` with default credentials
  `admin`/`adminpassword`.

This should give you a basic local setup of the application running with
FastAPI.
