# Notes-REST


## Description
В контейнере создано веб-приложение для создания заметок Django REST, подключённое к базе данных Postgres, находящейся в другом контейнере.

## Endpoints

Адрес сервера: ```localhost:8000```

* GET ```/api/v1/notes/``` - Получить список заметок.
* POST ```/api/v1/notes/``` - Создать заметку.

* GET ```/api/v1/notes/<int:pk>/``` - Получить заметку по id.
* DELETE ```/api/v1/notes/<int:pk>/``` - Удалить заметку по id.
* PATCH ```/api/v1/notes/<int:pk>/``` - Обновить заметку по id.

Авторизация
* POST ```/api/v1/token/``` - Получить refresh и access токены.
* POST ```/api/v1/token/refresh``` - Refresh the token.

## Authorization

Авторизация для API реализована через simple-jwt токены и сессии.

## Installation
Поднимаем все контейнеры с помощью команды `docker compose up`.

После этого необходимо зайти в контейнер с Django,

 с помощью команды `docker exec -it [*ID Контейнера*] sh`

и прописать следующие команды:
```
python manage.py makemigrations
python manage.py migrate
```

