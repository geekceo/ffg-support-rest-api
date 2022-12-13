![Python](https://img.shields.io/badge/-Python-222222?style=flat&logo=python)&nbsp;
![Django](https://img.shields.io/badge/-Django-222222?style=flat&logo=django&logoColor=0b593c)
![DjangoRestFramework](https://img.shields.io/badge/-DjangoRestFramework-222222?style=flat&logo=django&logoColor=0b593c)&nbsp;
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-222222?style=flat&logo=postgresql)
![Docker](https://img.shields.io/badge/-Docker-222222?style=flat&logo=docker)

### Пути
```json
api/v1/token - создание получение токена для пользователя
```

В тело запроса отправляем JSON вида:
```JSON
{
    "username": "user",
    "password": "pass"    
}
```

```json
api/v1/user/ticket/all_tickets - отображение списка всех тикетов
api/v1/user/ticket/answer - ответ саппорта на тикет путем передачи GET-парамера с id и description в теле запроса
api/v1/user/ticket/create - создание тикета
api/v1/user/ticket/all_answers - получение всех ответов на тикет по id
api/v1/user/ticket/status -  смена статуса тикета, запрос вида:
```

```HTTP
http://localhost/api/v1/user/ticket/status?id=4&Close
```