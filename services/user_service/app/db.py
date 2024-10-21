import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение URL базы данных из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL_ALEMBIC")

# Создание асинхронного движка для подключения к базе данных
engine = create_async_engine(DATABASE_URL, echo=True)

# Асинхронная сессия для выполнения запросов
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
)

# Базовый класс для моделей
Base = declarative_base()

# Асинхронная функция для получения сессии базы данных
async def get_db():
    async with AsyncSessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()
