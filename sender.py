import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

# Конфигурация SMTP
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'email@example.com'
SMTP_PASSWORD = 'email_password'
FROM_EMAIL = 'email@example.com'

# Подключение к базе данных
conn = sqlite3.connect('clients.db')
cursor = conn.cursor()

# Получение завтрашней даты
tomorrow = datetime.now() + timedelta(days=1)
tomorrow_str = tomorrow.strftime('%Y-%m-%d')

# SQL запрос для получения записей на завтра
cursor.execute("""
    SELECT id, visit_date, doctor, email 
    FROM appointments 
    WHERE date(visit_date) = ?
""", (tomorrow_str,))

appointments = cursor.fetchall()

# Закрытие соединения с базой данных
conn.close()

# Отправка уведомлений по email
for appointment in appointments:
    appointment_id, visit_date, doctor, email = appointment
    
    # Создание email сообщения
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = email
msg['Subject'] = 'Appointment reminder'
    
    body = f"Dear patient,\n\nThis is a reminder for your appointment with {doctor} scheduled on {visit_date}.\n\nBest regards,\nYour clinic"
    msg.attach(MIMEText(body, 'plain'))
    
    # Подключение к SMTP серверу и отправка email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        text = msg.as_string()
        server.sendmail(FROM_EMAIL, email, text)
        server.quit()
        print(f"Notification sent: {email}")
    except Exception as e:
        print(f"Error sending notification: {e}")

# Для Windows (Task Scheduler):
# Открыть Task Scheduler.
# Создать новую задачу, настроим ее на ежедневное выполнение в определенное время.
# В качестве действия выберем выполнение программы `python.exe` и укажем путь к вашему скрипту `sender.py`.

# Этот скрипт будет ежедневно проверять базу данных на наличие записей о приемах на следующий день и отправлять соответствующие уведомления по email.
# Не забудьте заменить параметры SMTP-сервера на актуальные данные вашего почтового провайдера.