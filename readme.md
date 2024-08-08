## Установка и запуск проекта

Привет! Данная инструкция поможет вам установить и запустить проект на различных операционных системах.

Рекомендуемая версия Python: 3.12.3 ([https://www.python.org/downloads/release/python-3123/](https://www.python.org/downloads/release/python-3123/))

### 1. Windows

1. Установка Python:
    * Загрузите и установите Python с [официального сайта](https://www.python.org/downloads/) или по ссылке выше.
    * Важно! При установке убедитесь, что отмечена опция "Add Python to PATH".

2. Создание виртуального окружения:
    * Откройте терминал в папке проекта. 
        * Можно щелкнуть правой кнопкой мыши по папке и выбрать "Открыть в терминале".
        * Или используйте комбинацию клавиш Win + R, введите cmd и перейдите к папке проекта с помощью команды cd путь\до\проекта.
    * Выполните следующие команды:
        - pip install virtualenv
        - python -m venv venv
        - .\venv\Scripts\activate.bat
        - pip install -r requirements.txt
        - python parser.py 
        

3. Запуск проекта:
    * Чтобы запустить проект в следующий раз, вам необходимо:
        * Перейти в папку проекта: cd путь\до\проекта
        * Активировать виртуальное окружение: .\venv\Scripts\activate.bat
        * Запустить скрипт: python parser.py

### 2. Linux (Ubuntu, Mint)

1. Установка зависимостей:
    * Откройте терминал и выполните следующие команды:
        - sudo apt update && sudo apt upgrade -y
        - sudo apt install python3-pip -y
        - sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config libssl-dev libffi-dev 
        - sudo apt install python3-venv -y
        

2. Создание виртуального окружения:
    * Перейдите в папку проекта: cd path/to/project
    * Выполните следующие команды:
        - python3 -m venv venv
        - source venv/bin/activate
        - pip install -r requirements.txt
        - python3 parser.py 
        

3. Запуск проекта:
    * Чтобы запустить проект в следующий раз, вам необходимо:
        * Перейти в папку проекта: cd path/to/project
        * Активировать виртуальное окружение: source venv/bin/activate
        * Запустить скрипт: python3 parser.py

Важно: 
* Замените path/to/project на фактический путь к вашей папке проекта.

Приятного использования!