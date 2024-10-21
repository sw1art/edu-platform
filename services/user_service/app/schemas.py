from pydantic import BaseModel, EmailStr, Field

class CreateUser(BaseModel):
    first_name: str = Field(..., title="Имя", max_length=50)
    last_name: str = Field(..., title="Last Name", max_length=50)
    username: str = Field(..., title="Username", min_length=2, max_length=20)
    email: EmailStr = Field(..., title="Email", max_length=100)
    password: str = Field(..., title="Password", min_length=8, max_length=100)
    avatar_url: str = Field(None, title="Avatar URL")

class UpdateUser(BaseModel):
    first_name: str = Field(None, title="Имя", max_length=50)
    last_name: str = Field(None, title="Last Name", max_length=50)
    username: str = Field(None, title="Username", min_length=2, max_length=20)
    email: EmailStr = Field(None, title="Email", max_length=100)
    password: str = Field(None, title="Password", min_length=8, max_length=100)
    avatar_url: str = Field(None, title="Avatar URL")

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    avatar_url: str

    class Config:
        orm_mode = True
