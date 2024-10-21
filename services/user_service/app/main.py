from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware
from app.db import Base
from app.api import user  # Предполагается, что маршруты пользователей находятся в user.py
from dotenv import load_dotenv
import os

# Загрузка переменных окружения
load_dotenv()

# Создание приложения FastAPI
app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение к базе данных
DATABASE_URL = os.getenv("DATABASE_URL_ALEMBIC")
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
)

# Создание всех таблиц в базе данных
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()

# Подключение маршрутов пользователей
app.include_router(user, prefix="/users", tags=["users"])

# Корневая страница
@app.get("/")
async def root():
    return {"message": "Welcome to the User Service API!"}
