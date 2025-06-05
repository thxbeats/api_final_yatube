# Как запустить проект
Скопировать репозиторий и перейти в диресторию с ним:
``` 
git clone https://github.com/dableshevich/api_final_yatube.git
```
```
cd api_final_yatube/
```
Создать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activation
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Перейти в директорию с django проектом и выполнить миграции:
```
cd yatube_api/
```
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

# Примеры запросов
> Ниже представлено лишь несколько примеров запросов. Чтобы ознакомиться с полным функционалом API, перейдите по ссылке `[http://127.0.0.1:8000/redoc/]` после запуска сервера
1) Получение списка всех постов:
    ```
    curl --location --request GET 'http://127.0.0.1:8000/api/v1/follow/'
    ```
    Полученный ответ:
    ```
    [
        {
            "id": 1,
            "author": "admin",
            "image": null,
            "text": "text",
            "pub_date": "2025-03-29T16:48:13.804075Z",
            "group": null
        },
        {
            "id": 2,
            "author": "admin",
            "image": null,
            "text": "text",
            "pub_date": "2025-03-29T16:48:14.632129Z",
            "group": null
        },
        {
            "id": 3,
            "author": "admin",
            "image": null,
            "text": "text",
            "pub_date": "2025-03-29T16:48:15.270055Z",
            "group": null
        }
    ]
    ```
2) Получение всех комментариев к посту:
    ```
    curl --location --request GET 'http://127.0.0.1:8000/api/v1/posts/1/comments/'
    ```
    Полученный ответ:
    ```
    [
        {
            "id": 1,
            "author": "admin",
            "text": "text",
            "created": "2025-03-29T16:50:27.234394Z",
            "post": 1
        },
        {
            "id": 2,
            "author": "admin",
            "text": "text",
            "created": "2025-03-29T16:50:28.013182Z",
            "post": 1
        },
        {
            "id": 3,
            "author": "admin",
            "text": "text",
            "created": "2025-03-29T16:50:28.620059Z",
            "post": 1
        },
        {
            "id": 4,
            "author": "admin",
            "text": "text",
            "created": "2025-03-29T16:50:29.094426Z",
            "post": 1
        }
    ]
    ```
3) Получение всех подписок текущего пользователя:
    ```
    curl --location 'http://127.0.0.1:8000/api/v1/follow/' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQzMzUwODYzLCJpYXQiOjE3NDMyNjQ0NjMsImp0aSI6IjdkZmUwMWNhZjRlNTQ2OGNhNjllZDlmNmIxNGZiODNjIiwidXNlcl9pZCI6MX0.Hzj0SwcW2RkxWMijRNX6r7xlPDOwZixFwGuakQ1lRas'
    ```
    Полученный ответ:
    ```
    [
        {
            "user": "admin",
            "following": "dablek"
        }
    ]
    ```