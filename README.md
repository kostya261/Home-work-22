# 🐍 Домашняя работа 22

Домашняя работа по основам Django

## 📦 Установка и настройка


1. Клонируйте репозиторий:
   [ссылка](https://github.com/kostya261/Home-work-22/pull/1)
   
2. Зависимости указанные в файле: *pyproject.toml*

```
[tool.poetry]
name = "homework-22"
version = "0.1.0"
description = "Домашняя работа 22"
authors = ["Konstantin Kosarew"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.13"
django = "^5.2.7"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

```

## Использование:

Откройте проект например в PyCharm, запустите локальный сервер командой: python manage.py runserver

Перейдите по ссылке в консоли или введите в строке браузера: 127.0.0.1:8000


## Структура проекта

HomeWork_21_2/
├── catalog/                # непосредственно приложение
│   ├── home.html           # основная тестовая страница
│   └── contacts.html       # страница контактов и для отправки post 
├── config/                 # конфигурационные файлы django
├── css/                    # файлы bootstrap
├── js/                     # и его JavaScript`ы
└── README.md               # Этот файл

👨‍💻 Автор
Константин

GitHub: https://github.com/kostya261

Email: kos261@yandex.ru


## Лицензия:
📄 Лицензия
Этот проект является курсовой работой и распространяется по лицензии MIT.В
