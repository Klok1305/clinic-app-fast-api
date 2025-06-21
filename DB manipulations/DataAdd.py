import sqlite3

# Функция для добавления записей в таблицу с учетом пользователя
def add_records_to_table(table_name, records, user1, user2):
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()

    for i, record in enumerate(records, start=1):
        if i % 2 == 1:
            user = user1
        else:
            user = user2
        cursor.execute(f"INSERT INTO {table_name} (title, description, user) VALUES (?, ?, ?)",
                       (record['title'], record['description'], user))

    conn.commit()
    conn.close()

def add_records_to_table_app(table_name, records, user1, user2):
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()

    for i, record in enumerate(records, start=1):
        if i % 2 == 1:
            user = user1
        else:
            user = user2
        cursor.execute(f"INSERT INTO {table_name} (title, description, user, visit_date, email) VALUES (?, ?, ?, ?, ?)",
                       (record['title'], record['description'], user, record['visit_date'], record['email']))

    conn.commit()
    conn.close()




appointments = [
    {'title': 'Dermatologist', 'description': 'Doctor 1', 'user': 'user1', 'visit_date': '2025-07-01 10:00', 'email': 'm2007102@edu.misis.ru'},
    {'title': 'Endocrinologist', 'description': 'Doctor 2', 'user': 'user2', 'visit_date': '2025-07-02 11:00', 'email': 'm2007102@edu.misis.ru'},
    {'title': 'Psychiatrist', 'description': 'Doctor 3', 'user': 'user2', 'visit_date': '2025-07-03 12:00', 'email': 'm2007102@edu.misis.ru'},
    {'title': 'Cosmetologist', 'description': 'Doctor 4', 'user': 'user1', 'visit_date': '2025-07-04 13:00', 'email': 'm2007102@edu.misis.ru'}
]


# Записи для таблицы analyses
analyses = [
    {'title': 'CBC', 'description': 'Description 1'},
    {'title': 'Ultrasound', 'description': 'Ultrasound description'},
    {'title': 'TSH', 'description': 'TSH description'},
    {'title': 'Vitamin D', 'description': 'Description D'}
    # Добавьте другие записи о анализах
]

# Записи для таблицы past_appointments
past_appointments = [
    {'title': 'Cosmetologist', 'description': 'Description of previous visit to cosmetologist'},
    {'title': 'Psychiatrist', 'description': 'Description of previous consultation with psychiatrist'},
    {'title': 'Endocrinologist', 'description': 'Description of previous consultation with endocrinologist'},
    {'title': 'Dermatologist', 'description': 'Description of previous visit to dermatologist'}
    # Добавьте другие записи о прошлых приемах
]

surveys = [
    {'title': 'Survey for first visit to psychiatrist', 'description': 'description'},
    {'title': 'Survey for first visit to neurologist', 'description': 'description'},
    {'title': 'Survey for first visit to cosmetologist', 'description': 'description'},
    {'title': 'Survey for first visit to orthopedist', 'description': 'description'}
    # Добавьте другие записи о прошлых приемах
]

# Добавление записей в соответствующие таблицы
add_records_to_table_app('appointments', appointments, 'user1', 'user2')
add_records_to_table('analyses', analyses, 'user1', 'user2')
add_records_to_table('past_appointments', past_appointments, 'user1', 'user2')
add_records_to_table('surveys', surveys, 'user1', 'user2')

