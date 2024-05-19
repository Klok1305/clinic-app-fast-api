import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


def get_next_appointment(username):
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT title, description, visit_date 
        FROM appointments 
        WHERE user = ? 
        ORDER BY visit_date ASC
        LIMIT 1
    ''', (username,))

    next_appointment = cursor.fetchone()
    conn.close()
    return next_appointment


def authenticate(username, password):
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()

    cursor.execute("SELECT PasswordHash FROM users WHERE Login = ?", (username,))
    user_data = cursor.fetchone()

    if user_data:
        stored_password_hash = user_data[0]
        if check_password_hash(stored_password_hash, password):
            return True

    conn.close()
    return False


def get_data_for_user(username):
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()

    cursor.execute("SELECT title, description FROM appointments WHERE user = ?", (username,))
    appointments_data = cursor.fetchall()

    cursor.execute("SELECT title, description FROM analyses WHERE user = ?", (username,))
    analyses_data = cursor.fetchall()

    cursor.execute("SELECT title, description FROM past_appointments WHERE user = ?", (username,))
    past_appointments_data = cursor.fetchall()

    cursor.execute("SELECT title, description FROM surveys WHERE user = ?", (username,))
    surveys_data = cursor.fetchall()

    conn.close()

    return {
        'appointments': appointments_data,
        'analyses': analyses_data,
        'past_appointments': past_appointments_data,
        'surveys': surveys_data
    }


def authenticate_admin(username, password):
    return username == 'admin' and password == 'adminpassword'


def get_table_columns(table_name):
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    conn.close()
    return [column[1] for column in columns]


def update_fake_database(username):
    real_data = get_data_for_user(username)

    global appointments, analyses, past_appointments, surveys
    appointments = real_data['appointments']
    analyses = real_data['analyses']
    past_appointments = real_data['past_appointments']
    surveys = real_data['surveys']


def get_appointments_data():
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments")
    appointments_data = cursor.fetchall()
    conn.close()
    return appointments_data


def get_analyses_data():
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM analyses")
    analyses_data = cursor.fetchall()
    conn.close()
    return analyses_data


def get_past_appointments_data():
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM past_appointments")
    past_appointments_data = cursor.fetchall()
    conn.close()
    return past_appointments_data


def get_surveys_data():
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM surveys")
    surveys_data = cursor.fetchall()
    conn.close()
    return surveys_data