import sqlite3
import os

# Путь к файлу базы данных
db_file = 'clinic.db'

# Проверяем, существует ли файл базы данных
if os.path.exists(db_file):
    # Удаляем файл базы данных
    os.remove(db_file)
    print("Database removed successfully.")
else:
    print("Database file not found.")

# Создание подключения к базе данных (если базы данных нет, она будет создана)
conn = sqlite3.connect(db_file)

# Создание объекта курсора для выполнения SQL-запросов
cursor = conn.cursor()

# Создание таблицы appointments
cursor.execute('''CREATE TABLE appointments
                (id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                user TEXT,
                visit_date DATETIME, 
                email Text)''')
  # Добавление столбца visit_date

cursor.execute('''CREATE TABLE IF NOT EXISTS admins (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password_hash TEXT
                    )''')

# Создание таблицы users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        UID INTEGER PRIMARY KEY AUTOINCREMENT,
        Login TEXT NOT NULL UNIQUE,
        PasswordHash TEXT NOT NULL
    )
''')

# Создание таблицы analyses
cursor.execute('''CREATE TABLE analyses
                (id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                user TEXT)''')

# Создание таблицы past_appointments
cursor.execute('''CREATE TABLE past_appointments
                (id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                user TEXT)''')

# Создание таблицы surveys
cursor.execute('''CREATE TABLE surveys
                (id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                user TEXT)''')

# Сохранение изменений
conn.commit()

# Закрытие соединения
conn.close()
