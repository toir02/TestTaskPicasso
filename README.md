## Тестовое задание по загрузке и обработке файлов
Этот проект реализует REST API для загрузки и обработки файлов с использованием фреймворка django rest framework

## Используемый стек:
- python
- django
- django rest framework
- postgresql
- jwt
- celery
- redis
- drf-yasg
- docker
- docker-compose

## Документация API
Документация для API реализована с помощью drf-yasg и находится на следующем адресе:
* http://localhost:8000/redoc/

## CORS
Для безопасности API реализован CORS с помощью django-cors-headers. 

В модуле ``settings.py`` необходимо внести изменения в следующие настройки, если у вас есть сторонние домены, обращающиеся к вашему API:

```
CORS_ALLOWED_ORIGINS = [
    "https://read-only.example.com",
    "https://read-and-write.example.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://read-and-write.example.com",
]
```

## Сущности системы
### Пользователь
- имя пользователя
- почта (опционально)
- пароль
### Файл
- файл
- время и дата загрузки
- признак обработки файла

## Как использовать данный проект?
- Убедитесь, что у вас установлен docker и docker-compose
- Склонировать репозиторий и перейти в директорию
  
  В терминале ввести команды
  ```
  git clone https://github.com/toir02/TestTaskPicasso
  ```
  ```
  cd TestTaskPicasso/
  ```
- Создать файл ``.env``, который необходимо заполнить данными из файла ``env.local``
- Запустить проект
  
  В терминале ввести команду
  ```
  sudo docker-compose up --build
  ```
- Откройте браузер и перейдите по адресу http://localhost:8000 для доступа к приложению.

## Тестирование
Проект покрыт тестами на 91%
Для того, чтобы посмотреть процент прокрытия тестами, необходимо ввести команду:
```
coverage run --source='.' manage.py test && coverage report
```

## Контакты

Если у вас возникли вопросы или проблемы при использовании проекта, свяжитесь со мной.

tg: @toir02
