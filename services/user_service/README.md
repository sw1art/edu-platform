# Сервис авторизации и распределения ролей

## Архитектура сервиса 

user_service/
├── app/
│   ├── __init__.py              # Инициализация приложения
│   ├── main.py                  # Точка входа FastAPI приложения
│   ├── models/
│   │   ├── user.py              # Модели данных для пользователя
│   ├── api/
│   │   ├── endpoints/
│   │   │   ├── user.py          # API endpoints для пользователей
│   ├── services/
│   │   ├── user_service.py      # Логика работы с пользователями (CRUD операции)
│   ├── utils/
│   │   ├── security.py          # Утилиты для безопасности (хэширование паролей, JWT)
├── tests/
│   ├── test_user.py             # Тесты для микросервиса пользователей
├── requirements.txt             # Python-зависимости (например, FastAPI, SQLAlchemy)
├── Dockerfile                   # Конфигурация Docker
├── config.py                    # Переменные окружения (например, базы данных)
└── README.md                    # Описание микросервиса


## Запуск через Docker

'Собираем Docker-образ
docker build -t user_service .'

'# Запускаем контейнер
docker run -d -p 8000:8000 user_service'
