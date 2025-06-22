FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Собираем базу данных внутри контейнера
RUN python "DB manipulations/TableCreate.py" \
    && python "DB manipulations/DataAdd.py"

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]