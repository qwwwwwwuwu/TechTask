FROM python:3.12.8

WORKDIR /app

COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Собираем статические файлы
RUN python manage.py collectstatic --noinput
RUN mkdir -p /app/logs

CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
