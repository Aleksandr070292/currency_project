# Currency Exchange Rate Project

## Описание
Этот проект предоставляет текущий курс доллара США к рублю через API по эндпоинту `/get-current-usd/`. Также он хранит историю последних 10 запросов.

## Функциональность
- Возвращает актуальный курс USD к RUB в формате JSON.
- Хранит последние 10 запросов на курс.
- Ограничивает частоту запросов: между запросами должен быть интервал не менее 10 секунд.

## Установка и запуск

### Предварительные требования
- Python 3.8 или выше

### Установка
1. Клонируйте репозиторий:
    git clone
    cd currency_project


2. Создайте и активируйте виртуальное окружение:
    python3 -m venv env
    source env/bin/activate  # для Linux/macOS
    env\Scripts\activate     # для Windows


3. Установите зависимости:
    pip install -r requirements.txt

4. Выполните миграции базы данных:
    python manage.py migrate


5. Запустите сервер разработки:
    python manage.py runserver


### Использование
После запуска сервера перейдите по адресу [http://127.0.0.1:8000/get-current-usd/](http://127.0.0.1:8000/get-current-usd/) для получения текущего курса доллара к рублю.