import os

# Параметры подключения к базе данных
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/edu_platform_db")
