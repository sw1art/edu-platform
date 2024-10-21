from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User
from passlib.context import CryptContext

# Настройка контекста хеширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Функция для хеширования пароля
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

async def is_username_unique(db: AsyncSession, username: str) -> bool:
    existing_user = await db.execute(select(User).where(User.username == username))
    return existing_user.scalars().first() is None

async def is_email_unique(db: AsyncSession, email: str) -> bool:
    existing_user = await db.execute(select(User).where(User.email == email))
    return existing_user.scalars().first() is None
