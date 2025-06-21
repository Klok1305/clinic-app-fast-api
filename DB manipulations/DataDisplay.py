import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('clinic.db')
cursor = conn.cursor()

# Выполняем SQL-запрос для просмотра содержимого таблицы appointments
cursor.execute("SELECT * FROM appointments")
appointments_data = cursor.fetchall()
print("Appointments table:")
for row in appointments_data:
    print(row)

# Выполняем SQL-запрос для просмотра содержимого таблицы analyses
cursor.execute("SELECT * FROM analyses")
analyses_data = cursor.fetchall()
print("\nAnalyses table:")
for row in analyses_data:
    print(row)

# Выполняем SQL-запрос для просмотра содержимого таблицы past_appointments
cursor.execute("SELECT * FROM past_appointments")
past_appointments_data = cursor.fetchall()
print("\nPast appointments table:")
for row in past_appointments_data:
    print(row)

cursor.execute("SELECT * FROM surveys")
analyses_data = cursor.fetchall()
print("\nSurveys table:")
for row in analyses_data:
    print(row)
# Закрываем соединение с базой данных
conn.close()
