from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    bio: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    name: Optional[str]
    bio: Optional[str]

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    bio: Optional[str]
    is_active: bool

    class Config:
        orm_mode = True
