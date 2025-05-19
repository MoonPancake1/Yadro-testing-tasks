# Используем официальный образ Ubuntu 22.04
FROM ubuntu:22.04

# Устанавливаем Python и зависимости
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и скрипт
COPY requirements.txt .
COPY task_1.py .

# Устанавливаем зависимости из requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Запускаем скрипт при старте контейнера
CMD ["python3", "task_1.py"]