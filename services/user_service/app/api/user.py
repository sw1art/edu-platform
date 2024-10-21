from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import CreateUser, UpdateUser, UserResponse
from app.models import User
from app.db import get_db
from app.utils import hash_password, is_username_unique, is_email_unique

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
async def create_user(user: CreateUser, db: AsyncSession = Depends(get_db)):
    # Проверка уникальности username
    if not await is_username_unique(db, user.username):
        raise HTTPException(status_code=400, detail="Username already exists")

    # Проверка уникальности email
    if not await is_email_unique(db, user.email):
        raise HTTPException(status_code=400, detail="Email already exists")

    # Хеширование пароля
    hashed_password = hash_password(user.password)
    
    # Создание нового пользователя
    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        avatar_url=user.avatar_url
    )
    
    # Добавление нового пользователя в БД
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user

@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UpdateUser, db: AsyncSession = Depends(get_db)):
    existing_user = await db.get(User, user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Проверка уникальности username, если он изменен
    if user.username and user.username != existing_user.username:
        if not await is_username_unique(db, user.username):
            raise HTTPException(status_code=400, detail="Username already exists")

    # Проверка уникальности email, если он изменен
    if user.email and user.email != existing_user.email:
        if not await is_email_unique(db, user.email):
            raise HTTPException(status_code=400, detail="Email already exists")

    # Обновление данных пользователя в БД
    if user.first_name:
        existing_user.first_name = user.first_name
    if user.last_name:
        existing_user.last_name = user.last_name
    if user.username:
        existing_user.username = user.username
    if user.email:
        existing_user.email = user.email
    if user.password:
        existing_user.hashed_password = hash_password(user.password)
    if user.avatar_url:
        existing_user.avatar_url = user.avatar_url

    await db.commit()
    await db.refresh(existing_user)

    return existing_user


@router.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    existing_user = await db.get(User, user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(existing_user)
    await db.commit()

    return {"detail": "User deleted successfully"}