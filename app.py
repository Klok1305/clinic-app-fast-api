import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import mylibrary

app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if mylibrary.authenticate_admin(username, password):
            session['admin'] = True
            return redirect(url_for('admin_panel'))
        else:
            return render_template('admin_login.html', error='Invalid username or password')
    return render_template('admin_login.html', error=None)


@app.route('/admin-panel')
def admin_panel():
    if 'admin' in session:
        appointment_columns = mylibrary.get_table_columns('appointments')
        analysis_columns = mylibrary.get_table_columns('analyses')
        past_appointment_columns = mylibrary.get_table_columns('past_appointments')
        survey_columns = mylibrary.get_table_columns('surveys')

        appointments_data = mylibrary.get_appointments_data()
        analyses_data = mylibrary.get_analyses_data()
        past_appointments_data = mylibrary.get_past_appointments_data()
        surveys_data = mylibrary.get_surveys_data()

        return render_template('admin_panel.html', appointments=appointments_data, analyses=analyses_data,
                               past_appointments=past_appointments_data, surveys=surveys_data,
                               appointment_columns=appointment_columns, analysis_columns=analysis_columns,
                               past_appointment_columns=past_appointment_columns, survey_columns=survey_columns)
    else:
        return redirect(url_for('admin_login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('clinic.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Login FROM users WHERE Login = ?", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            conn.close()
            return render_template('register.html', error='Пользователь с таким именем уже существует')

        password_hash = generate_password_hash(password)

        cursor.execute("INSERT INTO users (Login, PasswordHash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template('register.html', error=None)


@app.route('/')
def home():
    if 'username' in session:
        return f'Hello, {session["username"]}! <a href="/logout">Logout</a>'
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if mylibrary.authenticate(username, password):
            session['username'] = username
            return redirect(url_for('profile'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html', error=None)


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        mylibrary.update_fake_database(username)
        user_data = mylibrary.get_data_for_user(username)
        next_appointment = mylibrary.get_next_appointment(username)
        return render_template('profile.html', username=username, user_data=user_data, next_appointment=next_appointment)
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
