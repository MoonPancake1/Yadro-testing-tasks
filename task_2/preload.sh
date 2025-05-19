#!/bin/bash

# Проверяем, передан ли аргумент с версией
if [ -z "$1" ]; then
    read -p "Введите версию образа (например, 0.0.0.1): " version
else
    version=$1
fi

# Пути к файлам
TASK1_DIR="../task_1"
DOCKERFILE_DIR="."
REQUIREMENTS="$TASK1_DIR/requirements.txt"
PYTHON_SCRIPT="$TASK1_DIR/task_1.py"

# Проверяем существование файлов
if [ ! -f "$REQUIREMENTS" ] || [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Ошибка: Не найдены файлы requirements.txt или task_1.py в директории $TASK1_DIR"
    exit 1
fi

# Функция для проверки изменений файлов
files_changed() {
    # Если файлы в текущей директории отсутствуют, значит они новые
    if [ ! -f "requirements.txt" ] || [ ! -f "task_1.py" ]; then
        return 0
    fi
    
    # Сравниваем хеши файлов
    if ! cmp -s "$REQUIREMENTS" "requirements.txt" || ! cmp -s "$PYTHON_SCRIPT" "task_1.py"; then
        return 0
    fi
    
    return 1
}

# Проверяем, изменились ли файлы
if files_changed; then
    echo "Обнаружены изменения в файлах, копируем актуальные версии..."
    cp "$REQUIREMENTS" "$DOCKERFILE_DIR"
    cp "$PYTHON_SCRIPT" "$DOCKERFILE_DIR"
else
    echo "Файлы не изменились, используем существующие версии."
fi

# Собираем Docker-образ
echo "Сборка Docker-образа task_1:$version и task_1:latest..."
docker build -t "task_1:$version" -t "task_1:latest" .

# Проверяем успешность сборки
if [ $? -ne 0 ]; then
    echo "Ошибка при сборке Docker-образа"
    exit 1
fi

# Запускаем контейнер
echo "Запуск контейнера из образа task_1:latest..."
docker run -d task_1

echo "Готово! Контейнер запущен в фоновом режиме."