# Используем официальный образ Python 3.10
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app


# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install django psycopg2-binary

# Копируем остальные файлы проекта
COPY . .

# Устанавливаем переменные окружения для Django
ENV DJANGO_SETTINGS_MODULE=myproject.settings
ENV PYTHONUNBUFFERED=1

# Открываем порт для приложения
EXPOSE 8000

# Запускаем сервер Django
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]
