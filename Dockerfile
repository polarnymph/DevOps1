# Используем официальный образ Python 3.10
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app


# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Устанавливаем переменные окружения для Django
ENV DJANGO_SETTINGS_MODULE=myproject.settings
ENV PYTHONUNBUFFERED=1

# Выполняем миграции и собираем статику
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Открываем порт для приложения
EXPOSE 8000

# Запускаем сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
