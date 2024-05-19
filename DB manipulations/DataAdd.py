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
    {'title': 'Дерматолог', 'description': 'Врач 1', 'user': 'user1', 'visit_date': '2024-06-01 10:00', 'email' : 'm2007102@edu.misis.ru'},
    {'title': 'Эндокринолог', 'description': 'Врач 2', 'user': 'user2', 'visit_date': '2024-06-02 11:00', 'email' : 'm2007102@edu.misis.ru'},
    {'title': 'Психиатр', 'description': 'Врач 3', 'user': 'user2', 'visit_date': '2024-06-03 12:00', 'email' : 'm2007102@edu.misis.ru'},
    {'title': 'Косметолог', 'description': 'Врач 4', 'user': 'user1', 'visit_date': '2024-06-04 13:00', 'email' : 'm2007102@edu.misis.ru'}
]


# Записи для таблицы analyses
analyses = [
    {'title': 'ОАК', 'description': 'Описание 1'},
    {'title': 'УЗИ', 'description': 'Описание УЗИ'},
    {'title': 'ТТГ', 'description': 'Описание ттг'},
    {'title': 'Витамин D', 'description': 'Описание D'}
    # Добавьте другие записи о анализах
]

# Записи для таблицы past_appointments
past_appointments = [
    {'title': 'Косметолог', 'description': 'Описание прошлого приема у косметолога'},
    {'title': 'Психиатр', 'description': 'Описание прошлой консультации у психиатора'},
    {'title': 'Эндокринолог', 'description': 'Описание прошлой консультации у эндокринолога'},
    {'title': 'Дерматолог', 'description': 'Описание прошлого приема у дерматолога'}
    # Добавьте другие записи о прошлых приемах
]

surveys = [
    {'title': 'Опрос для первичного приема у психиатора', 'description': 'описание'},
    {'title': 'Опрос для первичного приема у невролога', 'description': 'описание'},
    {'title': 'Опрос для первичного приема у косметолога', 'description': 'описание'},
    {'title': 'Опрос для первичного приема у ортопеда', 'description': 'описание'}
    # Добавьте другие записи о прошлых приемах
]

# Добавление записей в соответствующие таблицы
add_records_to_table_app('appointments', appointments, 'user1', 'user2')
add_records_to_table('analyses', analyses, 'user1', 'user2')
add_records_to_table('past_appointments', past_appointments, 'user1', 'user2')
add_records_to_table('surveys', surveys, 'user1', 'user2')

