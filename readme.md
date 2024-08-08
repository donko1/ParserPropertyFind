Привет! Инструкция по установке на все ОС. Рекомендуемая версия python: 3.12.3(https://www.python.org/downloads/release/python-3123/)
1. Windows:
- Установите python по ссылке python.org или ссылке выше. При установке обязательно галочку в Add Python to PATH!!!
- Открываем терминал в папке проекта. Можно правой кнопки мыши -> открыть в терминале ИЛИ win + R -> cmd -> cd путь\до\проекта . Далее вводим команды ниже
	pip install virtualenv      
	python -m venv venv
	.\venv\Scripts\activate.bat
	pip install -r requirements.txt 
	python parser.py
- В следующий раз для запуска потребуеться вводить следующие команды:
	cd путь\до\проекта
	.\venv\Scripts\activate.bat
	python parser.py
2. Linux(Ubuntu, Mint):
- Вводим следующие команды
	sudo apt update && sudo apt upgrade -y
	sudo apt install python3-pip -y
	sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config libssl-dev libffi-dev 
	sudo apt install python3-venv -y
	cd path/to/project
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt 
	python3 parser.py
- В следующий раз для запуска вводить следующие команды:
	cd path/to/project
	source venv/bin/activate
	python3 parser.py