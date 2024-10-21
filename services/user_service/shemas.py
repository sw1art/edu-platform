from pydantic import BaseModel, EmailStr
from typing import Optional, List

class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr

class UserCreate(UserBase):
    hashed_password: str

class UserUpdate(UserBase):
    is_active: Optional[bool] = True
    is_admin: Optional[bool] = False

class User(UserBase):
    id: int
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True
